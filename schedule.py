def find_class_combinations(class_schedule_info, personal_schedule):
    def backtrack(index, current_combination):
        if index == len(class_schedule_info):
            combinations.append(current_combination.copy())
            return

        class_name, class_sections = list(class_schedule_info.items())[index]

        for section in class_sections:
            if all(not overlap(sect, section) for sect in current_combination) and not overlap_personal_schedule(section):
                current_combination.append(section)
                backtrack(index + 1, current_combination)
                current_combination.pop()

    def overlap(section1, section2):
        time1, day1 = section1
        time2, day2 = section2
        return day1 == day2 and (time1[0] <= time2[1] and time2[0] <= time1[1])

    def overlap_personal_schedule(section):
        for personal_section in personal_schedule:
            if overlap(section, personal_section):
                return True
        return False

    combinations = []
    backtrack(0, [])

    return combinations

class_schedule_info = {
    "341": [
        [[1200, 1430], "Friday"],
        [[800, 81030], "Saturday"],
    ],
    "325": [
        [[1800, 1915], "Monday"],
        [[1700, 1815], "Tuesday"],
    ],
    "491A": [
        [[1400, 1515], "Monday"],
        [[1930, 2045], "Tuesday"],
        [[1830, 1945], "Monday"],
        [[2000, 2115], "Tuesday"],
    ],
    "326": [
        [[1700, 1815], "Tuesday"],
        [[1400, 1515], "Monday"],
    ],
    "342": [
        [[1230, 1345], "Tuesday"],
        [[1400, 1515], "Monday"],
        [[1300, 1530], "Friday"],
        [[1800, 1915], "Monday"],
        [[930, 1045], "Tuesday"],
        [[800, 1045], "Friday"],
        [[1830, 1945], "Tuesday"],
    ],
}

personal_schedule = [
    [[1000, 2000], "Saturday"],
    [[1000, 2000], "Sunday"],
]

def print_combinations():
    combinations = find_class_combinations(class_schedule_info, personal_schedule)
    for i, combination in enumerate(combinations):
        print(f"Combination {i + 1}:")
        for i, section in enumerate(combination):
            print(f"  Class: { list(class_schedule_info.keys())[i]}, Day: {section[1]}, Time: {section[0]}")
        print()

def main():
    print_combinations()

if __name__ == "__main__":
    main()