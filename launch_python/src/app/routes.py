from flask import Blueprint, jsonify
from services.calculate_moon_pos import CalculatePos

main = Blueprint('main', __name__)

# Root route
@main.route('/')
def home():
    return jsonify({"message": "Welcome to the Launch Control System!"}), 200

@app.route('/moon-position', methods=['GET'])
def get_moon_position():
    calc_pos = CalculatePos()
    calc_pos.get_current_location()  # First get the location
    moon_pos = calc_pos.calculate_moon_position()
    return jsonify(moon_pos)

@app.route('/launch-conditions', methods=['GET'])
def get_launch_conditions():
    calc_pos = CalculatePos()
    calc_pos.get_current_location()
    moon_pos = calc_pos.calculate_moon_position()

    if 'error' in moon_pos:
        return jsonify({'error': 'Invalid data to calculate launch conditions'})

    azimuth = moon_pos['azimuth']
    elevation = moon_pos['elevation']

    # Define some example optimal conditions
    ideal_azimuth_range = (85, 95)
    ideal_elevation_range = (20, 40)

    if ideal_azimuth_range[0] <= azimuth <= ideal_azimuth_range[1] and ideal_elevation_range[0] <= elevation <= ideal_elevation_range[1]:
        return jsonify({'launch': True, 'message': 'Optimal conditions for launch'})
    else:
        return jsonify({'launch': False, 'message': 'Conditions are not optimal for launch'})