from flask import request, jsonify
from flask_jwt_extended import jwt_required
from bson.objectid import ObjectId
from datetime import datetime
from app import app, db
from models import todo_schema

def validate_todo_data(data):
    if not data.get('name') or not data.get('description'):
        return False
    return True

@app.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    data = request.get_json()
    if not validate_todo_data(data):
        return jsonify({'msg': 'Invalid data'}), 400
    data['created_at'] = datetime.utcnow()
    result = db.todos.insert_one(data)
    todo = db.todos.find_one({'_id': result.inserted_id})
    return jsonify(todo_schema(todo)), 201

@app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    todos = db.todos.find()
    return jsonify([todo_schema(todo) for todo in todos]), 200

@app.route('/todos/<id>', methods=['GET'])
@jwt_required()
def get_todo_by_id(id):
    todo = db.todos.find_one({'_id': ObjectId(id)})
    if not todo:
        return jsonify({'msg': 'ToDo not found'}), 404
    return jsonify(todo_schema(todo)), 200

@app.route('/todos/<id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    data = request.get_json()
    if not validate_todo_data(data):
        return jsonify({'msg': 'Invalid data'}), 400
    db.todos.update_one({'_id': ObjectId(id)}, {'$set': data})
    todo = db.todos.find_one({'_id': ObjectId(id)})
    return jsonify(todo_schema(todo)), 200

@app.route('/todos/<id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    result = db.todos.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({'msg': 'ToDo not found'}), 404
    return jsonify({'msg': 'ToDo deleted successfully'}), 200
