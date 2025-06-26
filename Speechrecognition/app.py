from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# ✅ OpenRouter API Key (yours)
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json['message']
    try:
        response = openai.ChatCompletion.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({'response': reply})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
