# calculator.py
# def square_number(number):
#     return number * number


def create_personal_schedule(start_time, end_time, days_of_week):
    personal_schedule = []
    for day in days_of_week:
        personal_schedule.append([[int(start_time), int(end_time)], [day]])
    return personal_schedule


def create_class_schedule_info(start_time, end_time, days_of_week):
    pass


def find_class_combinations(class_schedule_info, personal_schedule):
    def backtrack(index, current_combination):
        if index == len(class_schedule_info):
            combinations.append(current_combination.copy())
            return
        class_name, class_sections = list(class_schedule_info.items())[index]
        for section in class_sections:
            if all(
                not overlap(sect, section) for sect in current_combination
            ) and not overlap_personal_schedule(section):
                current_combination.append(section)
                backtrack(index + 1, current_combination)
                current_combination.pop()

    def overlap(section1, section2):
        time1, day1 = section1
        time2, day2 = section2
        return day1 == day2 and (time1[0] <= time2[1] and time2[0] <= time1[1])

    def overlap_personal_schedule(section):
        time, day = section
        for personal_section in personal_schedule:
            for d in day:
                if d in personal_section[1] and (
                    time[0] <= personal_section[0][1]
                    and personal_section[0][0] <= time[1]
                ):
                    return True
        return False

    combinations = []
    backtrack(0, [])
    return combinations


def output_combinations(class_schedule_info, personal_schedule):
    combinations = find_class_combinations(class_schedule_info, personal_schedule)
    output = []
    for i, combination in enumerate(combinations):
        combination_dict = {}
        for j, section in enumerate(combination):
            combination_dict[list(class_schedule_info.keys())[j]] = {
                "day": section[1],
                "time": section[0],
            }
            
        output.append(combination_dict)
    return output
