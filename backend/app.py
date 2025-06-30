from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful resume and cover letter writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )
        return jsonify({"content": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def serve_html():
    return send_from_directory('../frontend', 'ibm.html')

if __name__ == '__main__':
    app.run(debug=True)

