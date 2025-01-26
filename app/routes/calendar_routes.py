from flask import Blueprint, jsonify
from app.services.calendar_service import get_free_slots

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/free-slots', methods=['GET'])
def free_slots():
    try:
        slots = get_free_slots()
        return jsonify(slots), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
