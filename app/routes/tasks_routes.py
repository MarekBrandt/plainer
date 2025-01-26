from flask import jsonify, Blueprint, request

from app.models.task import TaskInput
import app.services.task_service as ts

from marshmallow import Schema, fields, ValidationError

class TaskSchema(Schema):
    name = fields.String(required=True)

task_schema = TaskSchema()

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = ts.get_all_tasks()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = task_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    new_task = ts.create_task(TaskInput(name=data['name']))

    return jsonify(new_task), 201

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        deleted_task = ts.delete_task(task_id)
        if deleted_task is None:
            return jsonify({"error": f"Task {task_id} not found"}), 404
        else:
            return jsonify({"message": f"Task {task_id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
