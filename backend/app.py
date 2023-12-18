# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://192.168.49.2:30001'])

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return 400
        else:
            return 400
        return jsonify(result=result)
    else:
        return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')