import os
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
if not API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY environment variable not set")
API_URL = "https://api-inference.huggingface.co/models/gpt3/"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api', methods=['POST'])
def api_call():
    user_input = request.json.get('inputs', '')
    payload = {
        "inputs": user_input,
        "options": { "use_cache": True } # You can customize the API call with additional options here
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"HTTP error: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
