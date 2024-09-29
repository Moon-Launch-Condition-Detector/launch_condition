from flask import Blueprint, jsonify
from app.services import monitor 

main = Blueprint('main', __name__)

# Root route
@main.route('/')
def home():
    return jsonify({"message": "Welcome to the Launch Control System!"}), 200

@main.route('/status', methods=['GET'])
def system_status(): 
    status = monitor.get_system_status()
    return jsonify(status), 200 

