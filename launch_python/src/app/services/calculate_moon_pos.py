from skyfield.api import Topos, load
import requests



class CalculatePos:
    def __init__(self):
        self.location = {
            'latitude': 0,
            'longitude': 0,
            'city': '',
            'country': ''
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
        else:
            print(f"Error: Unable to get the location. Status code: {response.status_code}")

        return self.location

    def calculate_moon_position(self):
        # Load ephemeris data to get positions of celestial objects
        eph = load('de421.bsp')
        moon = eph['moon']

        # Get the current time
        ts = load.timescale()
        t = ts.now()

        # Use the location retrieved from the API
        lat = self.location['latitude']
        lon = self.location['longitude']

        # Handle missing location data
        if lat == 0 or lon == 0:
            return {'error': 'Invalid location data'}

        # Define your location
        location = Topos(f'{lat} N', f'{lon} W')

        # Calculate Moon's position relative to the location
        astrometric = eph['earth'].at(t).observe(moon)
        alt, az, d = astrometric.apparent().altaz()

        return {
            'azimuth': az.degrees,
            'elevation': alt.degrees
        }
