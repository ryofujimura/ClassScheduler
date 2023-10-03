from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_square(number):
    return number * number

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            user_input = float(request.form['number'])
            result = calculate_square(user_input)
        except ValueError:
            result = "Invalid input. Please enter a valid number."

        return str(result)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
