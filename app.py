from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/simpleCalc', methods=['GET', 'POST'])
def simpleCalc():
    total = ""
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        
        # Check if numbers are provided
        if num1 and num2:
            try:
                if request.form.get('add') == 'add':
                    total = int(num1) + int(num2)
                elif request.form.get('sub') == 'sub':
                    total = int(num1) - int(num2)
            except ValueError:
                total = "Invalid input"

    return render_template('simpleCalc.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)