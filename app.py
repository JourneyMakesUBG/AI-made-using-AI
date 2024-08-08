from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Load your OpenAI API key from an environment variable
openai.api_key = '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'

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=50
    )

    return jsonify({'answer': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
