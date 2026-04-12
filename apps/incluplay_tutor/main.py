from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# The C++ Engine address
ENDEE_URL = "http://127.0.0.1:8080"

@app.route('/ask', methods=['POST'])
def ask_tutor():
    data = request.json
    query = data.get("query", "")
    
    try:
        # Attempt to get context from the Endee C++ Engine
        # We use a short timeout so the UI doesn't hang
        response = requests.post(f"{ENDEE_URL}/search", json={"text": query}, timeout=2)
        context = response.json().get("results", "Curriculum data")
        answer = f"According to Endee Engine: {context}. Let's solve this!"
    except:
        # Fallback if C++ engine is offline
        answer = f"I'm here to help with your question about: '{query}'. (Engine Offline)"

    return jsonify({"answer": answer})

if __name__ == '__main__':
    print("IncluPlay Backend running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)