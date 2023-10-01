import json

'''
This function generates all possible combinations of class sections that do not overlap with each other or the personal schedule using a backtracking approach. It calls the backtrack function to explore different combinations.
'''
def find_class_combinations(class_schedule_info, personal_schedule):
    '''
    This is a recursive function that explores possible combinations of class sections. It keeps track of the current combination and adds valid sections to it. When it reaches the end of the class schedule information, it appends the current combination to the list of combinations
    '''
    def backtrack(index, current_combination):
        if index == len(class_schedule_info):
            combinations.append(current_combination.copy())
            return
        class_name, class_sections = list(class_schedule_info.items())[index]
        # print(class_name,"------" ,class_sections)
        for section in class_sections:
            if all(not overlap(sect, section) for sect in current_combination) and not overlap_personal_schedule(section):
                current_combination.append(section)
                backtrack(index + 1, current_combination)
                current_combination.pop()

    '''
    This function checks whether two class sections overlap in terms of day and time.
    '''
    def overlap(section1, section2):
        time1, day1 = section1
        time2, day2 = section2
        return day1 == day2 and (time1[0] <= time2[1] and time2[0] <= time1[1])
    '''
    This function checks whether a class section overlaps with the personal schedule.
    '''
    def overlap_personal_schedule(section):
        time, day = section
        for personal_section in personal_schedule:
            for d in day:
                if d in personal_section[1] and (time[0] <= personal_section[0][1] and personal_section[0][0] <= time[1]):
                    return True
        return False

    combinations = []
    backtrack(0, [])

    return combinations

'''
This function loads the class schedule information from a JSON file.
'''
def load_class_schedule_info(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

'''
This function calls find_class_combinations to find all combinations and then prints them to the console.
'''
def print_combinations(class_schedule_info, personal_schedule):
    combinations = find_class_combinations(class_schedule_info, personal_schedule)
    for i, combination in enumerate(combinations):
        print(f"Combination {i + 1}:")
        for j, section in enumerate(combination):
            print(f"  Class: {list(class_schedule_info.keys())[j]}, Day: {section[1]}, Time: {section[0]}")
        print()
'''
It stores the combinations in a JSON file named "output.json" instead of printing them.
'''
def output_combinations(class_schedule_info, personal_schedule):
    # output combinations as a json file just like print_combinations()
    combinations = find_class_combinations(class_schedule_info, personal_schedule)
    output = []
    for i, combination in enumerate(combinations):
        combination_dict = {}
        for j, section in enumerate(combination):
            combination_dict[list(class_schedule_info.keys())[j]] = {"day": section[1], "time": section[0]}
        output.append(combination_dict)
    with open("output.json", "w") as f:
        json.dump(output, f)


def main():
    # class_schedule_info = load_class_schedule_info("class_schedule_info.json")
    # personal_schedule = load_class_schedule_info("static/personal_schedule.json")
    class_schedule_info = load_class_schedule_info("scripts/class_schedule_info.json")
    personal_schedule = load_class_schedule_info("static/personal_schedule.json")
    print_combinations(class_schedule_info, personal_schedule)
    output_combinations(class_schedule_info, personal_schedule)

if __name__ == "__main__":
    main()