# calculator.py
def square_number(number):
    return number * number

def create_personal_schedule(start_time, end_time, days_of_week):
    print("createprsonalschedule")
    json_personal_schedule = []
    for day in days_of_week:
        json_personal_schedule.append([[int(start_time), int(end_time)], [day]])

    print(json_personal_schedule)
    return json_personal_schedule

