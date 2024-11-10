# scheduler.py

import sqlite3
import os
from itertools import product

# Constants
DAYS = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
START_TIME = 8 * 60    # 8:00 AM in minutes
END_TIME = 22 * 60     # 10:00 PM in minutes
TIME_INCREMENT = 5     # 5-minute increments
TOTAL_TIME_SLOTS = ((END_TIME - START_TIME) // TIME_INCREMENT)  # Total time slots in a day

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'class_schedule.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def time_str_to_minutes(time_str):
    """
    Convert military time string or integer (e.g., "0900" or 900) to minutes since midnight.
    """
    try:
        time_str = str(time_str).zfill(4)  # Ensure it's a 4-character string with leading zeros
        hours = int(time_str[:-2])
        minutes = int(time_str[-2:])
        return hours * 60 + minutes
    except Exception as e:
        print(f"Error converting time_str '{time_str}' to minutes: {e}")
        raise

def fetch_classes(class_ids):
    """
    Fetch classes and their time slots from the database.
    Returns a dictionary with class IDs as keys and a list of sections as values.
    Each section includes its time slots represented as bitsets.
    """
    conn = get_db_connection()
    classes = {}

    for class_id in class_ids:
        # Fetch class name
        class_info = conn.execute(
            'SELECT class_id FROM class_offered WHERE id = ?',
            (class_id,)
        ).fetchone()
        if not class_info:
            print(f"No class found with id {class_id}")
            continue
        class_name = class_info['class_id']

        # Fetch class times
        times = conn.execute(
            'SELECT start_time, end_time, days FROM class_times WHERE class_offered_id = ?',
            (class_id,)
        ).fetchall()

        sections = []
        for time in times:
            # Check for missing or invalid data
            if not time['start_time'] or not time['end_time'] or not time['days']:
                print(f"Invalid time data for class {class_name}: {time}")
                continue
            try:
                bitset = create_bitset(time['start_time'], time['end_time'], time['days'])
                section = {
                    'class_id': class_id,
                    'class_name': class_name,
                    'start_time': time['start_time'],
                    'end_time': time['end_time'],
                    'days': time['days'],
                    'bitset': bitset
                }
                sections.append(section)
            except Exception as e:
                print(f"Error creating bitset for class {class_name}: {e}")
                continue
        if sections:
            classes[class_id] = sections
        else:
            print(f"No valid sections found for class {class_name}")

    conn.close()
    return classes

def create_bitset(start_time_str, end_time_str, days_str):
    """
    Create a bitset representing the class time slots.
    """
    print(f"Creating bitset for: start_time={start_time_str}, end_time={end_time_str}, days={days_str}")  # Debug statement
    bitset = 0
    start_time = time_str_to_minutes(start_time_str)  # Convert to minutes since midnight
    end_time = time_str_to_minutes(end_time_str)
    days = parse_days(days_str)

    for day in days:
        if day not in DAYS:
            print(f"Invalid day '{day}' encountered. Skipping.")
            continue
        day_index = DAYS.index(day)  # Correctly define day_index
        for minute in range(start_time, end_time, TIME_INCREMENT):
            time_slot = ((minute - START_TIME) // TIME_INCREMENT)
            if time_slot < 0 or time_slot >= TOTAL_TIME_SLOTS:
                continue  # Skip times outside the schedule range
            bit_position = day_index * TOTAL_TIME_SLOTS + time_slot
            bitset |= 1 << bit_position
    return bitset

def create_bitset_minutes(start_time, end_time, days_str):
    """
    Create a bitset using times already converted to minutes since midnight.
    """
    bitset = 0
    days = parse_days(days_str)

    for day in days:
        if day not in DAYS:
            print(f"Invalid day '{day}' encountered in personal schedule. Skipping.")
            continue
        day_index = DAYS.index(day)  # Ensure day_index is defined
        for minute in range(start_time, end_time, TIME_INCREMENT):
            time_slot = ((minute - START_TIME) // TIME_INCREMENT)
            if time_slot < 0 or time_slot >= TOTAL_TIME_SLOTS:
                continue  # Skip times outside the schedule range
            bit_position = day_index * TOTAL_TIME_SLOTS + time_slot
            bitset |= 1 << bit_position
    return bitset

def parse_days(days_str):
    """
    Parse the days string into a list of days.
    Supports both one-letter and two-letter day abbreviations.
    """
    two_letter_days = ['Tu', 'Th', 'Su', 'Sa']  # Added 'Sa' for Saturday
    days = []
    i = 0
    while i < len(days_str):
        # Check for two-letter day abbreviations
        if any(days_str.startswith(day, i) for day in two_letter_days):
            for day in two_letter_days:
                if days_str.startswith(day, i):
                    days.append(day)
                    i += len(day)
                    break
        else:
            # Assume one-letter day abbreviations
            days.append(days_str[i])
            i += 1
    return days

def create_time_slot_class_for_personal(personal_schedule):
    """
    Create a mapping of time slots to personal schedule blocks.
    """
    time_slot_class = {}
    for block in personal_schedule:
        start_time = time_str_to_minutes(block['start_time'])
        end_time = time_str_to_minutes(block['end_time'])
        days = parse_days(block['days'])
        for day in days:
            if day not in DAYS:
                print(f"Invalid day '{day}' in personal schedule. Skipping.")
                continue
            day_index = DAYS.index(day)
            for minute in range(start_time, end_time, TIME_INCREMENT):
                time_slot = ((minute - START_TIME) // TIME_INCREMENT)
                if time_slot < 0 or time_slot >= TOTAL_TIME_SLOTS:
                    continue
                bit_position = day_index * TOTAL_TIME_SLOTS + time_slot
                time_slot_class[bit_position] = {
                    'class_name': 'Personal Time',
                    'start_time': block['start_time'],
                    'end_time': block['end_time']
                }
    return time_slot_class

def create_personal_bitset(personal_schedule):
    """
    Create a bitset representing the user's personal schedule blocks.
    personal_schedule is a list of dicts with 'start_time', 'end_time', and 'days'.
    """
    bitset = 0
    for block in personal_schedule:
        start_time = time_str_to_minutes(block['start_time'])
        end_time = time_str_to_minutes(block['end_time'])
        bitset |= create_bitset_minutes(start_time, end_time, block['days'])
    return bitset

def generate_schedules(classes, personal_bitset, personal_schedule):
    """
    Generate all possible schedules without time conflicts.
    """
    # Get all sections for each class
    class_sections = list(classes.values())

    # Generate all combinations of class sections
    all_combinations = list(product(*class_sections))
    print(f"Total combinations: {len(all_combinations)}")  # Debug statement

    valid_schedules = []

    # Create time_slot_class mapping for personal schedule blocks
    personal_time_slot_class = create_time_slot_class_for_personal(personal_schedule)

    for combination in all_combinations:
        total_bitset = personal_bitset
        time_slot_class = {}  # Map time slots to class details (name and time)
        conflict = False
        for section in combination:
            # Check for conflict
            if total_bitset & section['bitset']:
                conflict = True
                break
            else:
                # Update the bitset and time_slot_class mapping
                section_bitset = section['bitset']
                total_bitset |= section_bitset
                # Get start and end times in minutes
                start_time = time_str_to_minutes(section['start_time'])
                end_time = time_str_to_minutes(section['end_time'])
                days = parse_days(section['days'])
                for day in days:
                    if day not in DAYS:
                        print(f"Invalid day '{day}' in class section. Skipping.")
                        continue
                    day_index = DAYS.index(day)
                    for minute in range(start_time, end_time, TIME_INCREMENT):
                        time_slot = ((minute - START_TIME) // TIME_INCREMENT)
                        if time_slot < 0 or time_slot >= TOTAL_TIME_SLOTS:
                            continue  # Skip times outside the schedule range
                        bit_position = day_index * TOTAL_TIME_SLOTS + time_slot
                        time_slot_class[bit_position] = {
                            'class_name': section['class_name'],
                            'start_time': section['start_time'],
                            'end_time': section['end_time']
                        }
        if not conflict:
            # Merge time_slot_class with personal_time_slot_class
            combined_time_slot_class = {**time_slot_class, **personal_time_slot_class}
            # Convert the combined_time_slot_class mapping into a matrix with class titles and times
            schedule_matrix = bitset_to_matrix_with_classes(combined_time_slot_class)
            valid_schedules.append({
                'sections': combination,
                'matrix': schedule_matrix
            })

    print(f"Total valid schedules: {len(valid_schedules)}")  # Debug statement

    return valid_schedules

def bitset_to_matrix_with_classes(time_slot_class):
    """
    Convert the time_slot_class mapping into a 2D list (matrix) with class titles and times.
    """
    matrix = [['' for _ in DAYS] for _ in range(TOTAL_TIME_SLOTS)]
    for bit_position, class_info in time_slot_class.items():
        day_index = bit_position // TOTAL_TIME_SLOTS
        time_slot = bit_position % TOTAL_TIME_SLOTS
        matrix[time_slot][day_index] = class_info
    return matrix
