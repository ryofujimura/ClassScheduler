from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the JSON data from the client
        data = request.get_json()

        # Save the JSON data as personal_schedule.json in the static folder
        output_path = os.path.join(app.static_folder, 'personal_schedule.json')
        with open(output_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        return jsonify(success=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
