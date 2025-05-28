from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notes = []
todos = []

@app.route('/')
def home():
    return jsonify({"message": "HandyHubTool API running!"})

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    note = request.json.get("note")
    notes.append(note)
    return jsonify(notes)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get("todo")
    todos.append(todo)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
