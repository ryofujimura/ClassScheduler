import json

class_schedule_info = {
    "341": [
        [[1200, 1430], ["Friday"]],
        [[800, 1030], ["Saturday"]],
    ],
    "325": [
        [[1800, 1915], ["Monday", "Wednesday"]],
        [[1700, 1815], ["Tuesday", "Thursday"]],
    ],
    "491A": [
        [[1400, 1515], ["Monday", "Wednesday"]],
        [[1930, 2045], ["Tuesday", "Thursday"]],
        [[1830, 1945], ["Monday", "Wednesday"]],
        [[2000, 2115], ["Tuesday", "Thursday"]],
    ],
    "326": [
        [[1700, 1815], ["Tuesday", "Thursday"]],
        [[1400, 1515], ["Monday", "Wednesday"]],
    ],
    "342": [
        [[1230, 1345], ["Tuesday", "Thursday"]],
        [[1400, 1515], ["Monday", "Wednesday"]],
        [[1300, 1530], ["Friday"]],
        [[1800, 1915], ["Monday", "Wednesday"]],
        [[930, 1045], ["Tuesday", "Thursday"]],
        [[800, 1045], ["Friday"]],
        [[1830, 1945], ["Tuesday", "Thursday"]],
    ],
}

personal_schedule = [
    # [[800, 2000], ["Saturday"]],
    # [[1000, 2000], ["Sunday"]],
]

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
        for personal_section in personal_schedule:
            if overlap(section, personal_section):
                return True
        return False

    combinations = []
    backtrack(0, [])

    return combinations

'''
This function calls find_class_combinations to find all combinations and then prints them to the console.
'''
def print_combinations():
    combinations = find_class_combinations(class_schedule_info, personal_schedule)
    for i, combination in enumerate(combinations):
        print(f"Combination {i + 1}:")
        for j, section in enumerate(combination):
            print(f"  Class: {list(class_schedule_info.keys())[j]}, Day: {section[1]}, Time: {section[0]}")
        print()
'''
It stores the combinations in a JSON file named "output.json" instead of printing them.
'''
def output_combinations():
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
    print_combinations()
    output_combinations()

if __name__ == "__main__":
    main()