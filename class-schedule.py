import json

timetable = {
    "Monday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Tuesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Wednesday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Thursday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Friday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Saturday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0},
    "Sunday": {800: 0, 815: 0, 830: 0, 845: 0, 900: 0, 915: 0, 930: 0, 945: 0, 1000: 0, 1015: 0, 1030: 0, 1045: 0, 1100: 0, 1115: 0, 1130: 0, 1145: 0, 1200: 0, 1215: 0, 1230: 0, 1245: 0, 1300: 0, 1315: 0, 1330: 0, 1345: 0, 1400: 0, 1415: 0, 1430: 0, 1445: 0, 1500: 0, 1515: 0, 1530: 0, 1545: 0, 1600: 0, 1615: 0, 1630: 0, 1645: 0, 1700: 0, 1715: 0, 1730: 0, 1745: 0, 1800: 0, 1815: 0, 1830: 0, 1845: 0, 1900: 0, 1915: 0, 1930: 0, 1945: 0, 2000: 0, 2015: 0, 2030: 0, 2045: 0, 2100: 0, 2115: 0}
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
    #     2: [[1930, 1945, 2000, 2015, 2030, 2045], "Tuesday"],
    #     3: [[1830, 1845, 1900, 1915, 1930, 1945], "Monday"],
    #     4: [[2000, 2015, 2030, 2045, 2100, 2115], "Tuesday"]
    },
    "326": {
        1: [[1700, 1715, 1730, 1745, 1800, 1815], "Tuesday"],
    #     2: [[1400, 1415, 1430, 1445, 1500, 1515], "Monday"]
    },
    "342": {
        1: [[1230, 1245, 1300, 1315, 1330, 1345], "Tuesday"],
    #     2: [[1400, 1415, 1430, 1445, 1500, 1515], "Monday"],
    #     3: [[1300, 1315, 1330, 1345, 1400, 1415, 1430, 1445, 1500, 1515, 1530], "Friday"],
    #     4: [[1800, 1815, 1830, 1845, 1900, 1915], "Monday"],
    #     5: [[930, 945, 1000, 1015, 1030, 1045], "Tuesday"],
    #     6: [[800, 815, 830, 845, 900, 915, 930, 945, 1000, 1015, 1030, 1045], "Friday"],
        # 7: [[1830, 1845, 1900, 1915, 1930, 1945], "Tuesday"]
    }
}

def busy_schedule(day, time, whichtimetable):
    if time in whichtimetable[day]:
        whichtimetable[day][time] += 1

def is_not_overlapping(start_time1, start_time2, end_time1, end_time2):
    for time in range(start_time1, end_time1 + 1, 15):
        if time in range(start_time2, end_time2 + 1, 15):
            return False
    return True

def personal_schedule():
    # ask for INPUT days busy, then ask for each days busy times
    days_busy = []
    personal_timetable = {}
    personal_timetable = timetable
    for day in timetable:
        if input("Are you busy on " + day + "? (y/n): ") == "y":
            days_busy.append(day)
    
    for day in days_busy:
        start_time = int(input("Start time for " + day + ": "))
        end_time = int(input("End time for " + day + ": "))
        for time in range(start_time, end_time + 1, 15):
            busy_schedule(day, time, personal_timetable)        

    return personal_timetable

def generate_combinations(class_schedule_info, combinations = []):
    for i in range(1, len(class_schedule_info[list(class_schedule_info.keys())[0]]) + 1):
        for j in range(1, len(class_schedule_info[list(class_schedule_info.keys())[1]]) + 1):
            for k in range(1, len(class_schedule_info[list(class_schedule_info.keys())[2]]) + 1):
                for l in range(1, len(class_schedule_info[list(class_schedule_info.keys())[3]]) + 1):
                    for m in range(1, len(class_schedule_info[list(class_schedule_info.keys())[4]]) + 1):
                        combinations.append([i, j, k, l, m])
    # print(len(combinations))
    # print(combinations)
    return combinations
    
def schedule_class(combinations, personal_timetable):
    # for all combinations, use def busy_schedule(day, time, whichtimetable) to check if the class is overlapping with personal_timetable
    # if not overlapping, add to new list, and personal_timetable to original
    # return new list
    
    valid_combinations = []
    for combination in combinations:
        class_timetable = personal_timetable
        for i, section in enumerate(combination):
            # i is class number by index
            # section is class section number
            for time_slots in class_schedule_info[list(class_schedule_info.keys())[i]][section][0]:
                busy_schedule(class_schedule_info[list(class_schedule_info.keys())[i]][section][1], time_slots, class_timetable)
        # if every time slot in class_timetable is < 2, then append combinaiton to valid_combinations
        print(class_timetable)
        print(combination)
        if all(all(time_slot < 2 for time_slot in class_timetable[day].values()) for day in class_timetable):
            valid_combinations.append(combination)
            

    print(valid_combinations) 


def combination_x_school(combinations):
    schedules = []
    for i, classnumber in enumerate(combinations):
        schedule_name = "Schedule " + str(i + 1)
        schedule_data = []

        for j, classsection in enumerate(classnumber):
            course_code = "CECS " + list(class_schedule_info.keys())[j]
            course_name = "Section " + str(classsection)
            days = class_schedule_info[list(class_schedule_info.keys())[j]][classsection][1]
            times = class_schedule_info[list(class_schedule_info.keys())[j]][classsection][0]
            schedule_data.append([course_code, course_name, days, times])

        schedule = {
            "scheduleName": schedule_name,
            "scheduleData": schedule_data
        }
        schedules.append(schedule)

    return schedules

def create_outputfile(json_data):
    output_file = "output.json"
    with open(output_file, 'w') as json_file:
        json.dump(json_data, json_file)

def main():
    personal_timetable = personal_schedule()
    combinations = generate_combinations(class_schedule_info)
    class_combinations = schedule_class(combinations, personal_timetable)
    # schedules = combination_x_school(class_combinations)
    # print(schedules)
    # create_outputfile(schedules)n

if __name__ == "__main__":
    main()

# generate_combinations(class_schedule_info)