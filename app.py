from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 🔑 Your OpenRouter API key
API_KEY = "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"  # Replace with your key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data.get('topic', 'life')

    prompt = f"Generate 10 short and beautiful Instagram captions about '{topic}'. Keep them simple and unique."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:5000",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",  # ✅ Free model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body
    )

    try:
        data = response.json()
        print("API Response:", data)  # Debug print
        captions_raw = data["choices"][0]["message"]["content"]
        captions = [line.strip("-•1234567890. ").strip() for line in captions_raw.split('\n') if line.strip()]
    except Exception as e:
        captions = [f"Error: {str(e)}"]

    return jsonify({"captions": captions})

if __name__ == '__main__':
    app.run(debug=True)

