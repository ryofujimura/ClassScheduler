# app.py

from flask import Flask, render_template, request, jsonify
import os
import scheduler  # Import the scheduler module

app = Flask(__name__)

# Route to display available classes
@app.route('/')
def index():
    conn = scheduler.get_db_connection()
    classes = conn.execute('SELECT * FROM class_offered').fetchall()
    conn.close()
    return render_template('index.html', classes=classes)

# Route to fetch possible schedules dynamically
@app.route('/generate_schedules', methods=['POST'])
def generate_schedules():
    data = request.json
    print('Data received from client:', data)  # Debug statement
    class_ids = data.get('class_ids', [])
    personal_schedule = data.get('personal_schedule', [])
    print('Class IDs:', class_ids)
    print('Personal Schedule:', personal_schedule)

    # Fetch classes and their sections
    classes = scheduler.fetch_classes(class_ids)

    # Create personal bitset
    personal_bitset = scheduler.create_personal_bitset(personal_schedule)

    # Generate valid schedules
    valid_schedules = scheduler.generate_schedules(classes, personal_bitset, personal_schedule)

    # Prepare the response data
    schedules_data = []
    for schedule in valid_schedules:
        schedule_info = []
        for section in schedule['sections']:
            schedule_info.append({
                'class_id': section['class_id'],       # Include class_id
                'class_name': section['class_name'],
                'start_time': section['start_time'],
                'end_time': section['end_time'],
                'days': section['days']
            })
        # Add the matrix and class_ids to the schedule data
        schedules_data.append({
            'sections': schedule_info,
            'matrix': schedule['matrix']
        })

    print('Schedules Data to be sent to client:', schedules_data)  # Debug statement

    return jsonify(schedules_data)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
