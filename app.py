# app.py
from flask import Flask, request, jsonify, render_template
from logic import play

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def game():
    data = request.json
    user_choice = data.get('choice')
    result = play(user_choice)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
