# scheduler.py

import sqlite3
import os
from itertools import product

# Constants for time representation
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
        class_name = class_info['class_id']

        # Fetch class times
        times = conn.execute(
            'SELECT start_time, end_time, days FROM class_times WHERE class_offered_id = ?',
            (class_id,)
        ).fetchall()

        sections = []
        for time in times:
            section = {
                'class_id': class_id,
                'class_name': class_name,
                'start_time': time['start_time'],
                'end_time': time['end_time'],
                'days': time['days'],
                'bitset': create_bitset(time['start_time'], time['end_time'], time['days'])
            }
            sections.append(section)
        classes[class_id] = sections

    conn.close()
    return classes

def create_bitset(start_time_str, end_time_str, days_str):
    """
    Create a bitset representing the class time slots.
    """
    bitset = 0
    start_time = int(start_time_str)
    end_time = int(end_time_str)
    days = parse_days(days_str)

    for day in days:
        day_offset = DAYS.index(day) * TOTAL_TIME_SLOTS
        for minute in range(start_time, end_time, TIME_INCREMENT):
            time_slot = ((minute - START_TIME) // TIME_INCREMENT)
            bit_position = day_offset + time_slot
            bitset |= 1 << bit_position
    return bitset

def parse_days(days_str):
    """
    Parse the days string into a list of days.
    """
    days = []
    i = 0
    while i < len(days_str):
        if days_str[i:i+2] in ['Tu', 'Th', 'Su']:
            days.append(days_str[i:i+2])
            i += 2
        else:
            days.append(days_str[i])
            i += 1
    return days

def generate_schedules(classes, personal_bitset):
    """
    Generate all possible schedules without time conflicts.
    """
    # Get all sections for each class
    class_sections = list(classes.values())

    # Generate all combinations of class sections
    all_combinations = list(product(*class_sections))

    valid_schedules = []

    schedule_number = 1  # Counter for schedule numbering

    for combination in all_combinations:
        total_bitset = personal_bitset
        conflict = False
        for section in combination:
            # Check for conflict
            if total_bitset & section['bitset']:
                conflict = True
                break
            else:
                total_bitset |= section['bitset']
        if not conflict:
            # Add valid schedule
            valid_schedules.append(combination)
            # Print the matrix representation of the schedule
            print(f"\nSchedule Option {schedule_number}:")
            print_schedule_matrix(total_bitset)
            schedule_number += 1

    return valid_schedules

def create_personal_bitset(personal_schedule):
    """
    Create a bitset representing the user's personal schedule blocks.
    personal_schedule is a list of dicts with 'start_time', 'end_time', and 'days'.
    """
    bitset = 0
    for block in personal_schedule:
        bitset |= create_bitset(block['start_time'], block['end_time'], block['days'])
    return bitset

def print_schedule_matrix(bitset):
    """
    Convert the bitset back into a 2D matrix and print it.
    """
    # Initialize the matrix
    matrix = [[' ' for _ in DAYS] for _ in range(TOTAL_TIME_SLOTS)]
    for day_index, day in enumerate(DAYS):
        for time_slot in range(TOTAL_TIME_SLOTS):
            bit_position = day_index * TOTAL_TIME_SLOTS + time_slot
            if bitset & (1 << bit_position):
                matrix[time_slot][day_index] = 'X'

    # Print the matrix with time labels
    print("Time\t\t" + "\t".join(DAYS))
    for time_slot in range(TOTAL_TIME_SLOTS):
        # Calculate the actual time
        minutes = START_TIME + time_slot * TIME_INCREMENT
        hours = minutes // 60
        mins = minutes % 60
        time_label = f"{hours:02d}:{mins:02d}"
        row = matrix[time_slot]
        print(f"{time_label}\t" + "\t".join(row))