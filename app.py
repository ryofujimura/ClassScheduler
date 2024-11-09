from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database connection function with a relative path
def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'class_schedule.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Route to display available classes
@app.route('/')
def index():
    conn = get_db_connection()
    classes = conn.execute('SELECT * FROM class_offered').fetchall()
    conn.close()
    return render_template('index.html', classes=classes)

# Route to fetch selected class time slots dynamically
@app.route('/class_times', methods=['POST'])
def get_class_times():
    class_ids = request.json.get('class_ids', [])
    conn = get_db_connection()
    all_times = {}
    for class_id in class_ids:
        times = conn.execute(
            'SELECT start_time, end_time, days FROM class_times WHERE class_offered_id = ?',
            (class_id,)
        ).fetchall()
        all_times[class_id] = [{'start_time': t['start_time'], 'end_time': t['end_time'], 'days': t['days']} for t in times]
    conn.close()
    return jsonify(all_times)

if __name__ == '__main__':
    app.debug = True
    # use port 5000
    app.run(port=5000)
