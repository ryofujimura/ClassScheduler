# app.py
from flask import Flask, render_template, request, jsonify
from scripts.calculator import (
    create_personal_schedule,
    create_class_schedule_info,
    output_combinations,
)

app = Flask(__name__)
class_schedule = {
    "341": [
        [[1300, 1530], ["Friday"]],
        [[800, 1030], ["Saturday"]]
    ],
    "325": [
        [[1800, 1915], ["Monday", "Wednesday"]],
        [[1700, 1815], ["Tuesday", "Thursday"]]
    ],
    "491A": [
        [[1400, 1515], ["Monday", "Wednesday"]],
        [[1930, 2045], ["Tuesday", "Thursday"]],
        [[1830, 1945], ["Monday", "Wednesday"]],
        [[2000, 2115], ["Tuesday", "Thursday"]]
    ],
    "326": [
        [[1700, 1815], ["Tuesday", "Thursday"]],
        [[1400, 1515], ["Monday", "Wednesday"]]
    ],
    "342": [
        [[1400, 1515], ["Tuesday", "Thursday"]],
        [[1400, 1515], ["Monday", "Wednesday"]],
        [[1800, 1915], ["Monday", "Wednesday"]],
        [[1530, 1645], ["Monday", "Wednesday"]]
    ]
}
x = 10


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/calculate", methods=["POST"])
# def calculate():
#     data = request.get_json()
#     input_number = data["inputt"]
#     result = square_number(input_number)
#     return jsonify({"calculation": result})


# @app.route("/create_schedule", methods=["POST"])
# def create_schedule():
#     class_name = request.form.get("class_name")
#     class_data = []
#     sections = []

#     for key, value in request.form.items():
#         if key.startswith("section_name_"):
#             section_name = value
#             start_time = request.form.get("start_time_" + key.split("_")[-1])
#             end_time = request.form.get("end_time_" + key.split("_")[-1])
#             weekdays = request.form.getlist("weekdays_" + key.split("_")[-1])

#             section = {
#                 "section_name": section_name,
#                 "start_time": start_time,
#                 "end_time": end_time,
#                 "weekdays": weekdays,
#             }

#             sections.append(section)

#     class_entry = {
#         "class_name": class_name,
#         "sections": sections,
#     }

#     class_data.append(class_entry)

#     return class_data


@app.route("/calculate_schedule", methods=["POST"])
def calculate_schedule():
    try:
        data = request.get_json()
        start_time = data["startTime"]
        end_time = data["endTime"]
        days_of_week = data["daysOfWeek"]
        result = output_combinations(
            class_schedule, create_personal_schedule(start_time, end_time, days_of_week)
        )
        
        return jsonify({"result": result})
    except Exception as e:
        return (jsonify({"error": str(e)}),)


if __name__ == "__main__":
    app.run(debug=True)