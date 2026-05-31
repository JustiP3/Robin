from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data['prompt']

    # Replace this with your actual Gemma interaction code
    response = f"You said: {prompt}.  This is a placeholder response."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) # Use debug=True for development only