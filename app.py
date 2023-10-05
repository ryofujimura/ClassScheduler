# app.py
from flask import Flask, render_template, request, jsonify
from scripts.calculator import square_number
from scripts.calculator import create_personal_schedule

app = Flask(__name__)

# Define a dictionary to map day names to their numeric representation (e.g., Monday: 0, Tuesday: 1, etc.)
day_mapping = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
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
    data = request.get_json()
    start_time = data['startTime']
    end_time = data['endTime']
    days_of_week = data['daysOfWeek']
    result = create_personal_schedule(start_time, end_time, days_of_week)
    
    # Calculate the result (you can customize this calculation)
    # result = f"Schedule from {start_time} to {end_time} on {', '.join(days_of_week)}"

    return jsonify({'personal_schedule': result})

if __name__ == '__main__':
    app.run(debug=True)
