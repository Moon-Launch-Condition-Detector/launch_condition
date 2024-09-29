import random 
from launch_window import calculate_pos 


def check_fuel(): 
    return random.uniform(50.0, 100.00)

def check_temperature(): 
    return random.uniform(0.0, 1000.00)

def check_vibration(): 
    return random.uniform(0.0, 100.00)

def check_speed(): 
    gather_speed = 0
    return random.uniform(0.0,10000.00)

def check_latency(): 
    pass 

def check_launch_window(): 
    ccalc = calculate_pos() 
    calc.get_current_location()

def get_launch_window(): 
    pass 

def get_system_status():

    return {
        "fuel": check_fuel(),
        "temperature": check_temperature(),
        "vibration": check_vibration() 
    }
