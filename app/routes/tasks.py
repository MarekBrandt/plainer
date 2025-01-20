from flask import jsonify
from flask.sansio.blueprints import Blueprint

from app.services.task_service import get_all_tasks

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = get_all_tasks()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
