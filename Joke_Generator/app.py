from flask import Flask, render_template, jsonify, request
import requests
import json
import sseclient  # Ensure sseclient-py is installed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fact')
def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    if response.status_code == 200:
        fact = response.json().get('text', 'No fact found.')
        return jsonify({'fact': fact})
    else:
        return jsonify({'error': 'Could not retrieve a fact.'}), 500

@app.route('/generate_joke', methods=['POST'])
def generate_joke():
    fact = request.json.get('fact')
    # Simulate processing the fact to generate a joke
    joke = generate_joke_from_api(fact)
    return jsonify({'joke': joke})


def generate_joke_from_api(fact):
    url = "http://127.0.0.1:5000/v1/chat/completions"
	
    headers = {"Content-Type": "application/json"}

    # Use the fact as part of the user message for joke generation
    user_message = f"give me a one-liner complete joke about {fact}"
    history = [{"role": "user", "content": user_message}]

    data = {
        "mode": "instruct",
        "stream": True,
        "messages": history
    }

    try:
        stream_response = requests.post(url, headers=headers, json=data, verify=False, stream=True)
        client = sseclient.SSEClient(stream_response)

        assistant_message = ''
        for event in client.events():
            payload = json.loads(event.data)
            if 'choices' in payload and len(payload['choices']) > 0 and 'delta' in payload['choices'][0]:
                delta = payload['choices'][0]['delta']
                if delta['role'] == 'assistant':
                    content = delta['content']
                    assistant_message += content
            else:
                print("Error: Unexpected response structure:", payload)
        return assistant_message
    except KeyError as e:
        print(f"KeyError encountered: {e}. Payload might not have the expected structure.")
        return "An error occurred while generating the joke."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
