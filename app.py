# app.py
from flask import Flask, render_template, request, jsonify
from scripts.calculator import square_number

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    input_number = data['input']
    result = square_number(input_number)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
