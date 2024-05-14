from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sys
sys.path.append('../')
import grpc
import todo_pb2
import todo_pb2_grpc
import os

app = Flask(__name__)
CORS(app) 

# gRPC client setup
grpc_channel = grpc.insecure_channel('localhost:5000') 
grpc_stub = todo_pb2_grpc.todoServiceStub(grpc_channel)

# Set the html template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/src/'))
app.template_folder = template_dir

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addtodo", methods=['GET', 'POST'])
def add_todo():
    if request.method == 'GET':
        return render_template("addtodo.html")
    elif request.method == 'POST':
        data = request.json
        todo_request = todo_pb2.todo(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            deadline=data['deadline'],
            completed=data['completed']
        )
        response = grpc_stub.Addtodo(todo_request)
        return jsonify({"message": "todo added successfully"})

@app.route("/alltodo")
def get_all_todos():
    response = grpc_stub.GetAll(todo_pb2.Empty())
    todo_list = [{"id": todo.id, "title": todo.title, "description": todo.description, "deadline": todo.deadline, "completed": todo.completed} for todo in response.todos]
    return jsonify({"todos": todo_list})

@app.route("/todo/<todo_title>")
def get_todo(todo_title):
    response = grpc_stub.Gettodo(todo_pb2.todoTitle(title=todo_title))
    if response.id:
        todo_data = {"id": response.id, "title": response.title, "description": response.description, "deadline": response.deadline, "completed": response.completed}
        return jsonify(todo_data)
    else:
        return jsonify({"message": "todo not found"}), 404
    
@app.route("/updatetodo/<todo_id>", methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo_request = todo_pb2.todo(
        id=todo_id,
        title=data.get('title', ''),
        description=data.get('description', ''),
        deadline=data.get('deadline', ''),
        completed=data.get('completed', 0)
    )
    response = grpc_stub.Updatetodo(todo_request)
    if response.id:
        return jsonify({"message": "todo updated successfully"})
    else:
        return jsonify({"message": "todo not found"}), 404

@app.route("/deletetodo/<todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    grpc_stub.Deletetodo(todo_pb2.todoId(id=todo_id))
    return jsonify({"message": "todo deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)