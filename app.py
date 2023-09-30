from flask import Flask, render_template, request, jsonify
import subprocess
import json
import os
import sys
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the path to the current Python interpreter
        python_executable = sys.executable

        # Run the Python script using the current interpreter
        subprocess.run([python_executable, "scripts/my_script.py"])

        # Read the output JSON file
        with open("output.json", "r") as json_file:
            output_data = json.load(json_file)

        return jsonify(output_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
