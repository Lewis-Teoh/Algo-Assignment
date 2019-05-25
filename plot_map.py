import googlemaps
import json
from pprint import pprint
import gmplot
import pygmaps


gmaps = googlemaps.Client(key='AIzaSyBsXB2cuyBBiieIafWGzNPmOKfiPvsARLM')

with open('location.json') as read_file:
    data = json.load(read_file)
    mymap = pygmaps.maps(2.743998, 101.685219, 3)
    location_lat = []
    location_lon = []
    for i in range(len(data["location"])):
        location_lat.append(float(data["location"][i]["lat"]))
        location_lon.append(float(data["location"][i]["lon"]))
        mymap.addpoint(float(data["location"][i]["lat"]),float(data["location"][i]["lon"]),"#FF0000")

    path = ([
        (float(data["location"][0]["lat"]),float(data["location"][0]["lon"])),
       (float(data["location"][8]["lat"]),float(data["location"][8]["lon"])),

        (float(data["location"][0]["lat"]), float(data["location"][0]["lon"])),
        (float(data["location"][1]["lat"]), float(data["location"][1]["lon"])),

        (float(data["location"][0]["lat"]), float(data["location"][0]["lon"])),
        (float(data["location"][2]["lat"]), float(data["location"][2]["lon"])),

        (float(data["location"][0]["lat"]), float(data["location"][0]["lon"])),
        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),

        (float(data["location"][0]["lat"]), float(data["location"][0]["lon"])),
        (float(data["location"][3]["lat"]), float(data["location"][3]["lon"])),
    ])
    mymap.addpath(path, "#00FF00")
    path=([
        (float(data["location"][1]["lat"]), float(data["location"][1]["lon"])),
        (float(data["location"][2]["lat"]), float(data["location"][2]["lon"])),

        (float(data["location"][1]["lat"]), float(data["location"][1]["lon"])),
        (float(data["location"][4]["lat"]), float(data["location"][4]["lon"])),

        (float(data["location"][1]["lat"]), float(data["location"][1]["lon"])),
        (float(data["location"][8]["lat"]), float(data["location"][8]["lon"])),
        ])
    mymap.addpath(path, "#00FF00")
    path = ([
        (float(data["location"][2]["lat"]), float(data["location"][2]["lon"])),
        (float(data["location"][4]["lat"]), float(data["location"][4]["lon"])),

        (float(data["location"][2]["lat"]), float(data["location"][2]["lon"])),
        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),
    ])
    mymap.addpath(path, "#00FF00")
    path = ([
        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),
        (float(data["location"][5]["lat"]), float(data["location"][5]["lon"])),

        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),
        (float(data["location"][7]["lat"]), float(data["location"][7]["lon"])),
    ])
    mymap.addpath(path, "#00FF00")
    path = ([
        (float(data["location"][3]["lat"]), float(data["location"][3]["lon"])),
        (float(data["location"][6]["lat"]), float(data["location"][6]["lon"])),

        (float(data["location"][3]["lat"]), float(data["location"][3]["lon"])),
        (float(data["location"][5]["lat"]), float(data["location"][5]["lon"])),

        (float(data["location"][3]["lat"]), float(data["location"][3]["lon"])),
        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),
    ])
    mymap.addpath(path, "#00FF00")

    path=([
        (float(data["location"][8]["lat"]), float(data["location"][8]["lon"])),
        (float(data["location"][6]["lat"]), float(data["location"][6]["lon"])),

        (float(data["location"][8]["lat"]), float(data["location"][8]["lon"])),
        (float(data["location"][9]["lat"]), float(data["location"][9]["lon"])),
    ])
    mymap.addpath(path ,"#00FF00" )
    path = ([
        (float(data["location"][6]["lat"]), float(data["location"][6]["lon"])),
        (float(data["location"][7]["lat"]), float(data["location"][7]["lon"])),
    ])
    mymap.addpath(path, "#00FF00")

    mymap.apiKey = "AIzaSyDV7uQWBpXuERBDI_-yKYuDvb5MGazeBNA"
    mymap.draw("static/map.html")

def plot_dynamic_map(list):
    dynamicmap = pygmaps.maps(2.743998, 101.685219, 3)
    #plot marker
    for i in range(len(list)):
        dynamicmap.addpoint(float(data["location"][list[i]]["lat"]), float(data["location"][list[i]]["lon"]), "#FF0000")
    #add path
    for j in range(len(list)-1):
        path = ([
            (float(data["location"][list[j]]["lat"]), float(data["location"][list[j]]["lon"])),
            (float(data["location"][list[j+1]]["lat"]), float(data["location"][list[j+1]]["lon"])),
        ])
        dynamicmap.addpath(path, "#00FF00")
    print("API is requested")
    dynamicmap.apiKey = "AIzaSyDV7uQWBpXuERBDI_-yKYuDvb5MGazeBNA"
    dynamicmap.draw("static/dynamic_map.html")