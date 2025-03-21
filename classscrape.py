import requests
from bs4 import BeautifulSoup
import sqlite3
import os
import re

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
    Given a string like '12:30 - 1:20PM', split into ('12:30', '1:20PM').
    If no dash is found, return (time_text, '').
    """
    if "-" in time_text:
        parts = time_text.split("-", 1)
        start = parts[0].strip()
        end = parts[1].strip()
        return (start, end)
    else:
        return (time_text, "")

def convert_time_to_numeric(time_str):
    """
    Convert a time string like '12:30PM' to numeric format (HHMM) for database storage.
    Returns 1230 for '12:30PM', 1330 for '1:30PM', etc.
    """
    if not time_str:
        return None
        
    # Remove any spaces
    time_str = time_str.strip()
    
    # Check if AM/PM is specified
    am_pm = ""
    if time_str.endswith("AM") or time_str.endswith("PM"):
        am_pm = time_str[-2:]
        time_str = time_str[:-2]
    
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