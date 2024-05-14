import grpc
import sys
sys.path.append('../')
import pymongo
from concurrent import futures
import todo_pb2
import todo_pb2_grpc
import logging

class todoService(todo_pb2_grpc.todoServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["admin"]
        self.collection = self.db["todolist"]
        logging.info("Connected to MongoDB")

    def Addtodo(self, request, context):
        logging.info("Received Addtodo request: %s", request)
        todo_data = {
            "id": request.id,
            "title": request.title,
            "description": request.description,
            "deadline": request.deadline,
            "completed": request.completed
        }
        self.collection.insert_one(todo_data)
        return request

    def GetAll(self, request, context):
        logging.info("Received GetAll request")
        todo_list = []
        for todo_data in self.collection.find():
            todo = todo_pb2.todo(
                id=todo_data["id"],
                title=todo_data["title"],
                description=todo_data["description"],
                deadline=todo_data["deadline"],
                completed=todo_data["completed"]
            )
            todo_list.append(todo)
        return todo_pb2.todoList(todos=todo_list)

    def Gettodo(self, request, context):
        logging.info("Received Gettodo request for todo title: %s", request.title)
        todo_data = self.collection.find_one({"title": request.title})
        if todo_data:
            todo = todo_pb2.todo(
                id=todo_data["id"],
                title=todo_data["title"],
                description=todo_data["description"],
                deadline=todo_data["deadline"],
                completed=todo_data["completed"]
            )
            return todo
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("todo not found")
            return todo_pb2.todo()

    def GetTodosByCompleted(self, request, context):
        logging.info("Received GetTodosByCompleted request for completed status: %s", request.completed)
        todo_list = []
        for todo_data in self.collection.find({"completed": request.completed}):
            todo = todo_pb2.todo(
                id=todo_data["id"],
                title=todo_data["title"],
                description=todo_data["description"],
                deadline=todo_data["deadline"],
                completed=todo_data["completed"]
            )
            todo_list.append(todo)
        return todo_pb2.todoList(todos=todo_list)

    def Updatetodo(self, request, context):
        logging.info("Received Updatetodo request for todo ID: %s", request.id)
        todo_data = self.collection.find_one({"id": request.id})
        if todo_data:
            update_data = {}
            if request.title:
                update_data["title"] = request.title
            if request.description:
                update_data["description"] = request.description
            if request.deadline:
                update_data["deadline"] = request.deadline
            if request.completed:
                update_data["completed"] = request.completed

            self.collection.update_one({"id": request.id}, {"$set": update_data})
            return todo_pb2.todo(id=request.id, title=request.title, description=request.description, deadline=request.deadline, completed=request.completed)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("todo not found")
            return todo_pb2.todo()

    def Deletetodo(self, request, context):
        logging.info("Received Deletetodo request for todo ID: %s", request.id)
        result = self.collection.delete_one({"id": request.id})
        if result.deleted_count > 0:
            return todo_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("todo not found")
            return todo_pb2.Empty()

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_todoServiceServicer_to_server(todoService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    logging.info("Server started. Listening on port 5000...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
