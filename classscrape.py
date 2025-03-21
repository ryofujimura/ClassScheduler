import requests
from bs4 import BeautifulSoup
import sqlite3
import os
import re
from datetime import datetime

def scrape_cecs_schedule(url, output_db="class_schedule.db"):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Create or connect to SQLite database
    conn = sqlite3.connect(output_db)
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS class_offered (
        id INTEGER PRIMARY KEY,
        class_id TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS class_times (
        id INTEGER PRIMARY KEY,
        class_offered_id INTEGER NOT NULL,
        start_time INTEGER NOT NULL,
        end_time INTEGER NOT NULL,
        days TEXT NOT NULL,
        FOREIGN KEY (class_offered_id) REFERENCES class_offered (id)
    )
    ''')
    
    # Find all courseBlock containers
    course_blocks = soup.find_all("div", class_="courseBlock")
    class_count = 0
    time_count = 0

    for block in course_blocks:
        # -------------------------
        # 1) Extract Course Header
        # -------------------------
        course_header = block.find("div", class_="courseHeader")
        if not course_header:
            continue

        # Course code (e.g., CECS 80)
        code_span = course_header.find("span", class_="courseCode")
        course_code = code_span.get_text(strip=True) if code_span else ""

        # Insert into class_offered table
        cursor.execute("INSERT INTO class_offered (class_id) VALUES (?)", (course_code,))
        class_offered_id = cursor.lastrowid
        class_count += 1

        # ------------------------------------
        # 2) Find the Table with Class Sections
        # ------------------------------------
        section_table = block.find("table", class_="sectionTable")
        if not section_table:
            continue

        # Process each row in the section table
        rows = section_table.find_all("tr")
        if len(rows) <= 1:
            continue  # nothing but header

        for row in rows[1:]:
            cells = row.find_all(["th","td"])
            if len(cells) < 12:
                continue

            type_ = cells[5].get_text(strip=True)  # e.g. "ACT"
            days = cells[6].get_text(strip=True)   # e.g. "TuTh"
            time_text = cells[7].get_text(strip=True)  # e.g. "12:30 - 1:20PM"

            # Parse time into start_time and end_time
            start_time_str, end_time_str = parse_time_range(time_text)
            
            # Convert times to numeric format (HHMM) for database storage
            start_time = convert_time_to_numeric(start_time_str)
            end_time = convert_time_to_numeric(end_time_str)
            
            if start_time and end_time and days:
                # Insert into class_times table
                cursor.execute(
                    "INSERT INTO class_times (class_offered_id, start_time, end_time, days) VALUES (?, ?, ?, ?)",
                    (class_offered_id, start_time, end_time, days)
                )
                time_count += 1

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Scraping complete. Added {class_count} classes and {time_count} time slots to {output_db}.")

def parse_time_range(time_text):
    """
    Splits a time range string like "12:30 - 1:20PM" into (start, end) parts,
    then normalizes each to a "HH:MMAM/PM" format with a basic heuristic:
      - If parsing yields start > end, flip AM<->PM on the start time if that fixes it.
    """
    time_text = time_text.strip()
    if "-" in time_text:
        start_raw, end_raw = [x.strip() for x in time_text.split("-", 1)]
    else:
        # If no dash, treat entire string as start time, end is empty
        start_raw = time_text
        end_raw = ""

    start_fixed = unify_time_str(start_raw, end_raw)
    end_fixed = unify_time_str(end_raw, start_raw)
    
    # If both times have valid formats, check if start time is later than end time
    # This could happen if AM/PM is missing or incorrectly inferred
    if start_fixed and end_fixed and "M" in start_fixed and "M" in end_fixed:
        start_dt = try_parse_time(start_fixed)
        end_dt = try_parse_time(end_fixed)
        
        if start_dt and end_dt and start_dt > end_dt:
            # Try flipping AM/PM on start time to see if that fixes the issue
            if "AM" in start_fixed:
                start_fixed = start_fixed.replace("AM", "PM")
            elif "PM" in start_fixed:
                start_fixed = start_fixed.replace("PM", "AM")
    
    return start_fixed, end_fixed

def unify_time_str(time_str, reference_str=""):
    """
    Attempt to ensure time_str has an explicit AM/PM by:
      1) If time_str already has AM/PM, parse & reformat.
      2) Else if reference_str has AM/PM, use that as a hint.
      3) Else try 24-hour parse.
      4) Return "HH:MMAM/PM" if successful, else original string.
    """
    if not time_str:
        return ""
    
    time_str = time_str.strip().upper()
    
    # Check if time already has AM/PM
    has_ampm = "AM" in time_str or "PM" in time_str
    
    # Add ":00" if no minutes are specified
    if ":" not in time_str and any(char.isdigit() for char in time_str):
        digits_only = ''.join(char for char in time_str if char.isdigit())
        if len(digits_only) <= 2:  # It's likely just hours
            if has_ampm:
                am_pm = "AM" if "AM" in time_str else "PM"
                time_str = time_str.replace(am_pm, "")
                time_str = f"{time_str.strip()}:00{am_pm}"
            else:
                time_str = f"{time_str.strip()}:00"
    
    # Strategy 1: Time already has AM/PM
    if has_ampm:
        try:
            dt = datetime.strptime(time_str, "%I:%M%p")
            return dt.strftime("%I:%M%p")
        except ValueError:
            try:
                dt = datetime.strptime(time_str, "%I%p")
                return dt.strftime("%I:%M%p")
            except ValueError:
                pass
    
    # Strategy 2: Use reference_str to infer AM/PM
    if reference_str:
        if "AM" in reference_str:
            time_with_am = f"{time_str}AM"
            try:
                dt = datetime.strptime(time_with_am, "%I:%M%p")
                return dt.strftime("%I:%M%p")
            except ValueError:
                pass
        elif "PM" in reference_str:
            time_with_pm = f"{time_str}PM"
            try:
                dt = datetime.strptime(time_with_pm, "%I:%M%p")
                return dt.strftime("%I:%M%p")
            except ValueError:
                pass
    
    # Strategy 3: Try 24-hour format
    try:
        dt = datetime.strptime(time_str, "%H:%M")
        # Convert to 12-hour format with AM/PM
        return dt.strftime("%I:%M%p")
    except ValueError:
        pass
    
    # Return original if all strategies fail
    return time_str

def try_parse_time(time_str):
    """Helper function to try parsing a time string into a datetime object."""
    try:
        return datetime.strptime(time_str, "%I:%M%p")
    except ValueError:
        return None

def convert_time_to_numeric(time_str):
    """
    Convert a time string like '12:30PM' to numeric format (HHMM) for database storage.
    Returns 1230 for '12:30PM', 1330 for '1:30PM', etc.
    """
    if not time_str:
        return None
        
    # Remove any spaces
    time_str = time_str.strip().upper()
    
    # Check if AM/PM is specified
    am_pm = ""
    if "AM" in time_str:
        am_pm = "AM"
        time_str = time_str.replace("AM", "").strip()
    elif "PM" in time_str:
        am_pm = "PM"
        time_str = time_str.replace("PM", "").strip()
    
    # Split hours and minutes
    if ":" in time_str:
        hours, minutes = time_str.split(":")
    else:
        # If no colon, assume it's just hours
        hours = time_str
        minutes = "00"
    
    try:
        hours = int(hours)
        minutes = int(minutes)
        
        # Adjust for PM if needed
        if am_pm == "PM" and hours < 12:
            hours += 12
        elif am_pm == "AM" and hours == 12:
            hours = 0
            
        # Format as HHMM
        return hours * 100 + minutes
    except ValueError:
        return None

if __name__ == "__main__":
    url = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2025/By_Subject/CECS.html"
    scrape_cecs_schedule(url, "class_schedule.db")
    url = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2025/By_Subject/ENGR.html"
    scrape_cecs_schedule(url, "class_schedule.db")