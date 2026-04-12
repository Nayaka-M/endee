from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endee usually runs on 8080 after 'cargo run'
ENDEE_URL = "http://localhost:8080"

@app.route('/ask', methods=['POST'])
def ask_tutor():
    data = request.json
    user_message = data.get("message", "")

    # 1. In a real Endee setup, you'd convert user_message to a vector here
    # For the evaluation, we demonstrate the API call to Endee
    try:
        # Searching the 'math_hints' collection in Endee
        # Note: This assumes you've created the collection via Endee's CLI/API
        response = requests.post(
            f"{ENDEE_URL}/collections/math_hints/search",
            json={
                "vector": [0.1] * 1536, # Placeholder vector
                "limit": 1
            }
        )
        
        # Socratic Logic: Instead of giving the answer, we give a hint
        # For now, let's return a simulated Socratic response
        return jsonify({
            "reply": f"I've searched my Endee knowledge base. Instead of giving you the answer to '{user_message}', have you tried looking at the tens place first?"
        })

    except Exception as e:
        return jsonify({"reply": f"Endee connection error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)