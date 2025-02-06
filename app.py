# app.py

from flask import Flask, render_template, request, jsonify
import scheduler  # Ensure scheduler.py is in the same directory or properly referenced

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page with scraped classes.
    """
    try:
        import csv
        import tempfile

        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
            url = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Summer_2025/By_Subject/CECS.html"
            from classscrape import scrape_cecs_schedule
            scrape_cecs_schedule(url, temp_file.name)

            # Read the temporary file
            temp_file.seek(0)
            reader = csv.DictReader(temp_file)
            classes = list(reader)

        return render_template('index.html', classes=classes)
    except Exception as e:
        return render_template('index.html', classes=[], error=str(e))

@app.route('/generate_schedules', methods=['POST'])
def generate_schedules():
    """
    Handle the generation of schedules based on selected classes and personal schedules.
    """
    data = request.get_json()
    class_ids = data.get('class_ids', [])
    personal_schedule = data.get('personal_schedule', [])
    time_increment = data.get('time_increment', 30)  # Default to 30 if not provided

    # Ensure time_increment is an integer and valid
    try:
        time_increment = int(time_increment)
        if time_increment not in [15, 30, 60, 120]:
            raise ValueError("Invalid time increment selected.")
    except ValueError as ve:
        print(f"Invalid time_increment: {ve}")
        return jsonify({"error": "Invalid time increment selected. Please choose 15, 30, 60, or 120 minutes."}), 400

    # Fetch classes and their sections -  This will need significant changes in scheduler.py
    classes = scheduler.fetch_classes(class_ids)

    # Create bitset for personal schedule
    personal_bitset = scheduler.create_personal_bitset(personal_schedule, time_increment)

    # Generate all valid schedules
    schedules = scheduler.generate_schedules(classes, personal_bitset, personal_schedule, time_increment)

    # Prepare data to send back to client
    schedules_data = []
    for schedule in schedules:
        sections = []
        for section in schedule['sections']:
            sections.append({
                'class_id': section['class_id'],
                'class_name': section['class_name'],
                'start_time': section['start_time'],
                'end_time': section['end_time'],
                'days': section['days']
            })
        schedules_data.append({
            'sections': sections,
            'matrix': schedule['matrix']
        })

    return jsonify(schedules_data)

if __name__ == '__main__':
    app.run(debug=True)