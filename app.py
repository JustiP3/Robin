from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()    
    prompt = data.get("prompt")

    try:

        response = requests.post(
            OLLAMA_ENDPOINT,
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            }
        )
        response_data = response.json()
        answer = response_data.get("response", "")
     

    except Exception as e:
        answer = f"Error communicating with Ollama: {e}"
        print(e)

    return jsonify({"response": answer})


if __name__ == "__main__":
    app.run(debug=True)