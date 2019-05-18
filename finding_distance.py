import googlemaps
import json
from pprint import pprint

gmaps = googlemaps.Client(key='AIzaSyBsXB2cuyBBiieIafWGzNPmOKfiPvsARLM')

with open('location.json') as read_file:
    data = json.load(read_file)
    latitude_origin = data["origin"][0]["lat"]
    longitude_origin = data["origin"][0]["lon"]
    origin = (latitude_origin , longitude_origin)

    latitude_dest = data["location"][0]["lat"]
    longitude_dest = data["location"][0]["lon"]
    destination = (latitude_dest , longitude_dest)
    pprint(destination)
# result = gmaps.distance_matrix(origins, destination, mode='walking')["rows"][0]["elements"][0]["distance"]["value"]
