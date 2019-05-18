
from main import PlotMap

import json
if __name__=="__main__":



   data={}
   data['origin'] = []
   data['location'] = []

   origin = PlotMap()
   origin.add_location('Kuala Lumpur')
   data['origin'].append(origin.display_raw_location())

   location1 = PlotMap()
   location1.add_location('Singapore')
   data['location'].append(location1.display_raw_location())

   location2 = PlotMap()
   location2.add_location('Indonesia')
   data['location'].append(location2.display_raw_location())

   location3 = PlotMap()
   location3.add_location('Hong Kong')
   data['location'].append(location3.display_raw_location())

   location4 = PlotMap()
   location4.add_location('Australia')
   data['location'].append(location4.display_raw_location())

   location5 = PlotMap()
   location5.add_location('Beijing')
   data['location'].append(location5.display_raw_location())

with open('location.json', 'w') as outputfile:
    json.dump(data , outputfile , indent=4)