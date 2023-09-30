from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('schedule_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    course_name = request.form['course_name']
    day = request.form['day']
    time = request.form['time']

    # Process the form data here (e.g., store it in a database)

    return f'Course Name: {course_name}<br>Day: {day}<br>Time: {time}'

if __name__ == '__main__':
    app.run(debug=True)
