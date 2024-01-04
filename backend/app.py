# app.py
from flask import Flask, jsonify, request
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['*'])

openai.api_key = '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'

@app.route('/', methods=['POST'])
def generate_content():
    data = request.get_json()
    prompt = data['prompt']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    generated_content = response['choices'][0]['message']['content']

    return jsonify(content=generated_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')