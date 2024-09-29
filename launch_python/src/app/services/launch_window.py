from skyfield.api import Topos, load
from capture_moon import cap_camera
import requests

class calculate_pos: 
    
    def __init__(self): 
        self.location = { 
            'latitude': 0, 
            'longitude':0, 
            'city':0, 
            'country':0 
        }


    def get_current_location(self):
        # Use ipapi to get the location based on your IP
        response = requests.get('http://ipapi.co/json/')
        
        if response.status_code == 200:
            data = response.json()
            self.location['latitude'] = data.get('latitude')
            self.location['longitude'] = data.get('longitude')
            self.location['city'] = data.get('city')
            self.location['country'] = data.get('country_name')
            
            print(f"Latitude: {self.location['latitude']}")
            print(f"Longitude: {self.location['longitude']}")
            print(f"City: {self.location['city']}")
            print(f"Country: {self.location['country']}")
        else:
            print(f"Error: Unable to get the location. Status code: {response.status_code}")

    def test(self): 
        # Call the function to get the location
        self.get_current_location()


        # Load ephemeris data to get positions of celestial objects
        eph = load('de421.bsp')
        moon = eph['moon']

        # Define your location (latitude and longitude)
        location = Topos('28.5721 N', '80.6480 W')  # Example: Cape Canaveral

        # Get the current time
        ts = load.timescale()
        t = ts.now()

        # Calculate Moon's position relative to the location
        astrometric = eph['earth'].at(t).observe(moon)
        alt, az, d = astrometric.apparent().altaz()

        print(f'Azimuth: {az.degrees}, Elevation: {alt.degrees}')

calc = calculate_pos() 
calc.get_current_location()