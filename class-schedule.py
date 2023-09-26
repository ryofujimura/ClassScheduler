import json


sample_timetable = {
    "Monday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Tuesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Wednesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Thursday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Friday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Saturday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Sunday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    }

class_schedule_info = {
    "341": {
        1: [[1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345, 1400, 1415, 1430], "Friday"],
        2: [[800, 815, 830, 845, 900, 915, 930, 945, 1000, 1015, 1030], "Saturday"]
    },
    "325": {
        1: [[1800, 1815, 1830, 1845, 1900, 1915], "Monday"],
        2: [[1700, 1715, 1730, 1745, 1800, 1815], "Tuesday"]
    },
    "491A": {
        1: [[1400, 1415, 1430, 1445, 1500, 1515], "Monday"],
        2: [[1930, 1945, 2000, 2015, 2030, 2045], "Tuesday"],
        3: [[1830, 1845, 1900, 1915, 1930, 1945], "Monday"],
        4: [[2000, 2015, 2030, 2045, 2100, 2115], "Tuesday"]
    },
    "326": {
        1: [[1700, 1715, 1730, 1745, 1800, 1815], "Tuesday"],
        2: [[1400, 1415, 1430, 1445, 1500, 1515], "Monday"]
    },
    "342": {
        1: [[1230, 1245, 1300, 1315, 1330, 1345], "Tuesday"],
        2: [[1400, 1415, 1430, 1445, 1500, 1515], "Monday"],
        3: [[1300, 1315, 1330, 1345, 1400, 1415, 1430, 1445, 1500, 1515, 1530], "Friday"],
        4: [[1800, 1815, 1830, 1845, 1900, 1915], "Monday"],
        5: [[930, 945, 1000, 1015, 1030, 1045], "Tuesday"],
        6: [[800, 815, 830, 845, 900, 915, 930, 945, 1000, 1015, 1030, 1045], "Friday"],
        7: [[1830, 1845, 1900, 1915, 1930, 1945], "Tuesday"]
    }
}


def reset_timetable():
    for timeslot in timetable:
        for time in timetable[timeslot]:
            timetable[timeslot][time] = 0


def create_schedule():
    # Define the original timetable
    original_timetable = {
        "Monday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Tuesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Wednesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Thursday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Friday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Saturday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
        "Sunday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    }
    
    # Iterate through each day of the week
    for day in original_timetable:
        print(f"Is your schedule busy on {day}? (yes/no):")
        busy_input = input()
        
        # Check if the user is busy on the current day
        if busy_input.lower() == "yes":
            start_time = int(input(f"Enter busy start time for {day} (in military time): "))
            end_time = int(input(f"Enter busy end time for {day} (in military time): "))
            
            # Update the timetable for the specified day and time slots
            for time_slot in range(start_time, end_time + 15, 15):
                original_timetable[day][time_slot] = 1
    
    return original_timetable

# Call the function to create the schedule
updated_timetable = create_schedule()
timetable = sample_timetable
# print(timetable)

data = class_schedule_info


def create_timetable(print_timetable):
    # print(print_timetable)
    print("monday              tuesday             friday              saturday ")
    for time in print_timetable["Monday"]:
        print(str(time) + " - " + str(print_timetable["Monday"][time]) + "            " + str(time) + " - " + str(print_timetable["Tuesday"][time]) + "            " + str(time) + " - " + str(print_timetable["Friday"][time]) + "            " + str(time) + " - " + str(print_timetable["Saturday"][time]))

def classlist(classes):
    schedules = []
    for i, classnumber in enumerate(classes):
        schedule_name = "Schedule " + str(i + 1)
        schedule_data = []

        for j, classsection in enumerate(classnumber):
            course_code = "CECS " + list(data.keys())[j]
            course_name = "Section " + str(classsection)
            days = data[list(data.keys())[j]][classsection][1]
            times = data[list(data.keys())[j]][classsection][0]
            schedule_data.append([course_code + " " + course_name, days, times])

        schedule = {
            "scheduleName": schedule_name,
            "scheduleData": schedule_data
        }
        schedules.append(schedule)

    return schedules


# Recursive function to generate combinations
def generate_combinations(current_combination, current_index):
    if current_index == len(value_lists):
        combinations.append(list(current_combination))
        return
    for value in value_lists[current_index]:
        current_combination.append(value)
        generate_combinations(current_combination, current_index + 1)
        current_combination.pop()

# Start generating combinations
# generate_combinations([], 0)

def schedule_class(time_table):
    classes = []
    for combination in combinations:
        for i, value in enumerate(combination):
            for time_slot in data[list(data.keys())[i]][value][0]:
                time_table[data[list(data.keys())[i]][value][1]][time_slot] += 1

        if all(value < 2 for value in time_table["Monday"].values()) and all(value < 2 for value in time_table["Tuesday"].values()) and all(value < 2 for value in time_table["Friday"].values()) and all(value < 2 for value in time_table["Saturday"].values()):
            classes.append(combination)
        # time_table = updated_timetable

    return classes


            

    # classes = []
    # for combination in combinations:
    #     for i, value in enumerate(combination):
    #         for time_slot in data[list(data.keys())[i]][value][0]:
    #             time_table[data[list(data.keys())[i]][value][1]][time_slot] += 1

    #     # Check if all the time slots value is less than 2
    #     if all(value < 2 for value in time_table["Monday"].values()) and all(value < 2 for value in timetable["Tuesday"].values()) and all(value < 2 for value in timetable["Friday"].values()) and all(value < 2 for value in timetable["Saturday"].values()):
    #         classes.append(combination)
    #     timetable = updated_timetable

    #     # print(timetable)
    #     # print("-----------------------------------")
    # return classes

def create_outputfile(json_data):
    output_file = "output.json"
    with open(output_file, 'w') as json_file:
        json.dump(json_data, json_file)

combinations = []
value_lists = [list(data[key]) for key in data.keys()]
print(generate_combinations([], 0))
print(schedule_class(timetable))
create_outputfile(classlist(schedule_class(timetable)))



