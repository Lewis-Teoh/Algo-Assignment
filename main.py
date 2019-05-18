from geopy.geocoders import Nominatim
import json

class PlotMap:

    def add_location(self , location):
        self.location=location

    def display_raw_location(self):
        geolocator = Nominatim(user_agent="Algo Assignment")
        return geolocator.geocode(self.location , language='en').raw







