# app.py
from flask import Flask, render_template, request, jsonify
from scripts.calculator import (
    create_personal_schedule,
    create_class_schedule_info,
    output_combinations,
)

app = Flask(__name__)
class_schedule = {
    "329": [
        [[800, 915], ["Tuesday", "Thursday"]],
        [[1730, 1845], ["Tuesday", "Thursday"]],
        [[930, 1045], ["Tuesday", "Thursday"]],
        [[1230,1345], ["Monday", "Wednesday"]]
    ],
    "122": [
        [[800, 915], ["Monday", "Wednesday"]],
        [[1200, 1350], ["Friday"]],
        [[800, 950], ["Tuesday", "Thursday"]],
        [[800, 950], ["Friday"]],
        [[1000, 1150], ["Friday"]],
        [[930, 1045], ["Tuesday", "Thursday"]],
        [[1000, 1150], ["Wednesday"]],
        [[1600, 1715], ["Tuesday", "Thursday"]],
        [[1600, 1750], ["Wednesday"]],
        [[1230, 1345], ["Tuesday", "Thursday"]],
        [[800, 950], ["Friday"]],
        [[1000, 1150], ["Friday"]],
        [[1400, 1515], ["Tuesday", "Thursday"]],
        [[1530, 1720], ["Tuesday"]],
        [[1530, 1720], ["Thursday"]],
        [[1100, 1215], ["Monday", "Wednesday"]],
        [[1200, 1350], ["Tuesday"]],
        [[1400, 1550], ["Tuesday"]],
        [[1100, 1215], ["Monday", "Wednesday"]],
        [[800, 950], ["Friday"]],
        [[1000, 1150], ["Friday"]],
        [[1400, 1515], ["Tuesday", "Thursday"]],
        [[1530, 1720], ["Tuesday"]],
        [[1530, 1720], ["Thursday"]],
        [[1100, 1215], ["Tuesday", "Thursday"]],
        [[800, 950], ["Wednesday"]],
        [[1000, 1150], ["Wednesday"]],
        [[930, 1045], ["Monday", "Wednesday"]],
        [[900, 1050], ["Friday"]],
        [[1230, 1345], ["Monday", "Wednesday"]],
        [[1200, 1350], ["Thursday"]],
        [[1400, 1550], ["Thursday"]],
        [[1230, 1345], ["Monday", "Wednesday"]],
        [[800, 950], ["Thursday"]],
        [[1000, 1150], ["Thursday"]],
        [[1100, 1215], ["Tuesday", "Thursday"]],
        [[1000, 1150], ["Wednesday"]],
        [[1530, 1645], ["Monday", "Wednesday"]],
        [[1400, 1550], ["Tuesday"]],
        [[1400, 1550], ["Monday", "Wednesday"]],
        [[1400, 1550], ["Tuesday"]],
        [[1100, 1215], ["Monday", "Wednesday"]],
        [[800, 915], ["Monday", "Wednesday"]],
        [[800, 950], ["Friday"]],
        [[800, 950], ["Tuesday", "Thursday"]],
        [[800, 950], ["Friday"]],
        [[1000, 1150], ["Friday"]],
        [[1230, 1345], ["Tuesday", "Thursday"]],
        [[1400, 1550], ["Tuesday"]],
        [[1400, 1550], ["Thursday"]],
        [[1100, 1215], ["Tuesday", "Thursday"]],
        [[800, 950], ["Wednesday"]],
        [[1000, 1150], ["Wednesday"]],
        [[930, 1045], ["Tuesday", "Thursday"]],
        [[900, 1050], ["Friday"]],
        [[1230, 1345], ["Tuesday", "Thursday"]],
        [[1200, 1350], ["Friday"]],
        [[1400, 1550], ["Friday"]]]
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