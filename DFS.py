from collections import defaultdict
import json
from geopy.distance import geodesic
from flask import Flask, render_template, request
import decimal
import plot_map
import wordfreq




app = Flask(__name__)


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.graph = defaultdict(list)
        self.best_distance=[]
        self.path_travel = []
        self.dictionary = {'malaysia': 0,
                           'singapore': 1,
                           'indonesia': 2,
                           'hongkong': 3,
                           'australia': 4,
                           'china': 5,
                           'taiwan': 6,
                           'japan': 7,
                           'brunei': 8,
                           'thailand': 9}
        #number list
        self.best_route_country = []
        self.route = []
        #country name list
        self.best_route_country_name = []
        self.route = []
        self.transit= []
        self.transit_temp= []
        #kepp items dictionary
        self.items = []


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def printAllPathsUtil(self, u, d, visited, path):
        totalDistance = 0
        paths_name = []


        visited[u] = True
        path.append(u)
        if u == d:
            # print(path)
            for i in path:
                for k, v in self.dictionary.items():
                    if i==v:
                        paths_name.append(k)
            string = " > ".join(paths_name)
            # print(string)


            for i in range(len(path)-1):
                totalDistance += self.findDistance(path[i], path[i + 1])

            self.best_distance.append(totalDistance)
            self.path_travel.append([totalDistance,string])
            # print(totalDistance)


        else:

            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):

        self.addEdge(0, 8)
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(0, 9)
        self.addEdge(0, 3)
        self.addEdge(1, 2)
        self.addEdge(1, 4)
        self.addEdge(1, 8)
        self.addEdge(2, 4)
        self.addEdge(2, 9)
        self.addEdge(9, 5)
        self.addEdge(9, 7)
        self.addEdge(3, 6)
        self.addEdge(3, 5)
        self.addEdge(3, 9)
        self.addEdge(8, 6)
        self.addEdge(8, 9)
        self.addEdge(6, 7)
        # print("Following are all different paths from %d to %d :" % (s, d))

        visited = [False] * (self.V)

        path = []
        self.printAllPathsUtil(s, d, visited, path)

    def findDistance(self, location1, location2):
        with open('location.json') as read_file:
            data = json.load(read_file)
            latitude_origin = data["location"][location1]["lat"]
            longitude_origin = data["location"][location1]["lon"]
            origin = (latitude_origin, longitude_origin)

            latitude_dest = data["location"][location2]["lat"]
            longitude_dest = data["location"][location2]["lon"]
            destination = (latitude_dest, longitude_dest)

        result = (geodesic(origin, destination).km)

        result = decimal.Decimal(result)
        rounded = result.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
        return rounded


    def sortDistances(self):
        self.path_travel.sort()
        for i in range (len(self.path_travel)):
            self.path_travel[i][0]=float(self.path_travel[i][0])

        print(self.path_travel)

    def get_best_route_distance(self):
        print("Best Route distance : ", self.path_travel[0][0])
        return self.path_travel[0][0]

    def get_best_route(self):
        best_route_list = []
        country_list = []
        print("Best route : ",self.path_travel[0][1])
        best_route_list.append(self.path_travel[0][1].split(' > '))
        for i in range(len(best_route_list[0])):
            country_list.append(best_route_list[0][i])

        #matching key in country list with dict
        for country in country_list:
            for k,v in self.dictionary.items():
                if country==k:
                    self.best_route_country.append(v)
                    # self.best_route_country_name.append(k)

        return self.best_route_country

    def draw_dynamic_map(self):
        plot_map.plot_dynamic_map(self.best_route_country)

    #initial word file
    # def initialize_file(self):
        # initialize()
        # for i in range(len(self.path_travel)):
        #     self.route.append(self.path_travel[i][1].split(' > '))
        #
        # print(self.route)
        # for i in range(len(self.route)):
        #     for j in range(1,len(self.route[i])):
        #         self.transit.append(self.route[i][j])

            # print("Transit :", self.transit)
            # # print("Transit :" , self.transit)
        # print(self.route)

    def find_transit(self):
        distance = []
        result =[]
        longest = self.path_travel[len(self.path_travel)-1][0]
        fenmu= self.path_travel[len(self.path_travel)-1][0]-self.path_travel[0][0]

        for i in range(len(self.path_travel)):

            temp = []
            self.route.append(self.path_travel[i][1].split(' > '))
            temp.append(longest)
            temp.append(self.path_travel[i][0])
            distance.append(temp)
            if distance[i][0] == distance[i][1]:
                result.append(0)
            else:
                final = (distance[i][0] - distance[i][1]) / fenmu
                result.append(final)

        print(distance)
        print("Result:",result)

        # print('route', route)
        for i in range(len(self.route)):
            self.route[i].remove('malaysia')
        print('routedeleted', self.route)

        sentimenscore = []
        for i in range(len(self.route)):
            num = len(self.route[i])
            # temp=
            sum = 0
            for item in self.route[i]:
                # print("this is the word ",wordfreq.get_nation(item))
                sum += wordfreq.get_nation(item)
                # print("sum :",sum )
            sum = sum/num
            # temp = sum(temp)
            sentimenscore.append(sum)

        print(sentimenscore)

        score = []
        for i in range(len(self.path_travel)):
            temp = (result[i]*70)+(((sentimenscore[i]+100)/200)*30)
            score.append(temp)
            self.path_travel[i].append(round(score[i],2))

        return score

    def save_item(self):

        for i in range(len(self.path_travel)):
            an_item = dict(distance =self.path_travel[i][0] , route=self.path_travel[i][1] , score=self.path_travel[i][2])
            self.items.append(an_item)

        print(self.items)
        return self.items

    # def route(self):
    #     return self.path_travel[0][]

@app.route('/', methods=['GET', 'POST'])
def algo():
    if request.method == 'POST':

        destination = request.form['destination']
        g = Graph(15)
        print(g.printAllPaths(0, int(destination)))
        g.sortDistances()

        # g.initialize_file()
        g.get_best_route_distance()
        g.get_best_route()
        g.find_transit()
        g.save_item()
        g.draw_dynamic_map()
        # route = g.route[0][0]
        # print("route :",route)
        return render_template('myResult.html', airports=get_airport_names(), items=g.save_item())
    else:
        return render_template('myMap.html', airports=get_airport_names(),)

@app.route('/serviceidlookup', methods=["GET", "POST"])
def serviceidlookup(self):
    if request.method == 'POST':
        pyindex = request.form.get('pyindex')
        print('index', pyindex)

        # if pyindex is not None:
        #     for i in range(len())
    return render_template('myMap.html', airports=get_airport_names())



def get_airport_names():
    airport_list = []
    with open('location.json')as read_file:
        airport_names = json.load(read_file)
        for i in range(1,len(airport_names["location"])):
            s = airport_names["location"][i]["display_name"]
            s = s[:s.find(",")]
            airport_list.append(s)
    return airport_list

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)