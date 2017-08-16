# pip install googlemaps
from googlemaps import Client
from datetime import datetime


api_key = ''
gmaps = Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whitehouse_geoloc = gmaps.geocode(whitehouse)
print whitehouse_geoloc

destination = gmaps.reverse_geocode((38.897096, -77.036545))
print destination

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

lat_long = (gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lat'], gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lng'])
print lat_long
duke = gmaps.reverse_geocode(lat_long)[0]['formatted_address']
print duke 

local = gmaps.places('restaurant near ' + duke)
print local['results'][0]['formatted_address']
print local['results'][0]['name']

directions = gmaps.directions(duke, whitehouse)
print directions[0]['legs'][0]['distance']

for step in directions[0]['legs'][0]['steps']:
	print step['html_instructions']

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? 
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

now = datetime.now()
directions_result = gmaps.directions((38.917228,-77.0522365),
                                     (38.897096, -77.036545),
                                     mode="transit",
                                     departure_time=now)
directions_result[0]['legs'][0]['distance']['text']


directions_result1 = gmaps.directions((38.9076502, -77.0370427),
                                     (38.897096, -77.036545),
                                     mode="transit",
                                     departure_time=now)
distance=directions_result1[0]['legs'][0]['distance']['text']
distance_convert=str(distance).split(" ")[0]
distance_km=float(distance_convert)*1609.344
distance_km

destination = gmaps.reverse_geocode((38.9076502,-77.0370427))[0]['formatted_address']
print destination 

directions_result2 = gmaps.directions((38.916944, -77.048739),
                                     (38.897096, -77.036545),
                                     mode="transit",
                                     departure_time=now)
directions_result2[0]['legs'][0]['distance']['text']

def food_options(time,search,location):
    local = gmaps.places(search + location)
    food_list={}
    try:
        for place in range(0,len(local)):
            food_name=local['results'][place]['name']
            food_open=local['results'][place]['opening_hours']['open_now']
            food_price=local['results'][place]['price_level']
            food_address=local['results'][place]['formatted_address']
            food_directions = gmaps.directions(location,
                                     food_address,
                                     mode="transit",
                                     departure_time=time)
            food_distance=food_directions[0]['legs'][0]['distance']['text']
            food_rating=local['results'][place]['rating']
            food_all=[food_open,food_price,food_rating,food_address,food_distance]
            food_list[food_name]=food_all
        return food_list
    except:
        raise Exception,'No Results'
    


evening=1503010800
morning=1502974800

breakfast_choice=food_options(morning,'breakfast',destination)
dinner_choice=food_options(evening,'dinner',destination)

breakfast_choice
dinner_choice
