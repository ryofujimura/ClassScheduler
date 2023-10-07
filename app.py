# app.py
from flask import Flask, render_template, request, jsonify
from scripts.calculator import square_number, create_personal_schedule, output_combinations

app = Flask(__name__)
class_schedule = {
    "341": [
        [[1200, 1430], ["Friday"]],
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
        [[1230, 1345], ["Tuesday", "Thursday"]],
        [[1400, 1515], ["Monday", "Wednesday"]],
        [[1300, 1530], ["Friday"]],
        [[1800, 1915], ["Monday", "Wednesday"]],
        [[930, 1045], ["Tuesday", "Thursday"]],
        [[800, 1045], ["Friday"]],
        [[1830, 1945], ["Tuesday", "Thursday"]]
    ]
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    input_number = data['inputt']
    result = square_number(input_number)
    return jsonify({'calculation': result})

@app.route('/calculate_schedule', methods=['POST'])
def calculate_schedule():
    try:
        data = request.get_json()
        start_time = data['startTime']
        end_time = data['endTime']
        days_of_week = data['daysOfWeek']
        result = output_combinations(class_schedule, create_personal_schedule(start_time, end_time, days_of_week))
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}),

if __name__ == '__main__':
    app.run(debug=True)