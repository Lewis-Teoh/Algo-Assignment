
from main import PlotMap

import json
if __name__=="__main__":



   data={}
   data['location'] = []

   origin = PlotMap()
   origin.add_location('Kuala Lumpur International Airport')
   data['location'].append(origin.display_raw_location())

   location1 = PlotMap()
   location1.add_location('Changi Airport')
   data['location'].append(location1.display_raw_location())

   location2 = PlotMap()
   location2.add_location('Soekarno-Hatta International Airport')
   data['location'].append(location2.display_raw_location())

   location3 = PlotMap()
   location3.add_location('Hong Kong International Airport')
   data['location'].append(location3.display_raw_location())

   location4 = PlotMap()
   location4.add_location('Perth Airport')
   data['location'].append(location4.display_raw_location())

   location5 = PlotMap()
   location5.add_location('Beijing Capital International Airport')
   data['location'].append(location5.display_raw_location())

   location6 = PlotMap()
   location6.add_location('Taoyuan International Airport')
   data['location'].append(location6.display_raw_location())

   location7 = PlotMap()
   location7.add_location('Fukuoka Airport, Fukuoka, Japan')
   data['location'].append(location7.display_raw_location())

   location8 = PlotMap()
   location8.add_location('Brunei International Airport, Bandar Seri Begawan, Brunei')
   data['location'].append(location8.display_raw_location())

   location9 = PlotMap()
   location9.add_location('Phuket International Airport')
   data['location'].append(location9.display_raw_location())



with open('location.json', 'w') as outputfile:
    json.dump(data , outputfile , indent=4)