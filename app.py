from flask import Flask, render_template, request, send_from_directory
import json
import os
from scripts.schedule import main as run_schedule  # Import the main function from schedule.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        output_path = os.path.join(app.static_folder, 'personal_schedule.json')
        if os.path.exists(output_path):
            with open(output_path, 'w') as json_file:
                # output_data = json.load(json_file)
                output_data = json.dump(data, json_file, indent=2)
        else:
            output_data = []
        # Call the run_schedule function from schedule.py
        run_schedule()

        return "Success"

    return render_template('index.html')
# yourData=output_data

@app.route('/output.json')
def serve_output_json():
    return send_from_directory(app.root_path, 'output.json')

if __name__ == '__main__':
    app.run()