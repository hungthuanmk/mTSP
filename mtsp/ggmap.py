import googlemaps as ggm
from excel import *
from datetime import datetime
# api_key = 'AIzaSyDSbtA0_Tz3jt215tYXIOTKArJR5zHWfYI'
api_key = 'AIzaSyCD8Re4ImmDd539r4kjOT8ev0hPNxEeKVI'
gm = ggm.Client(key=api_key)

distances = dict()

def get_distance_dict():
    return distances

def get_coordinate(address):
    geocode_result = gm.geocode(address)[0]
    location = geocode_result['geometry']['location']
    lat = location['lat']
    long = location['lng']
    print('get_position(', address, ') \t= ', lat, ' | ', long)
    return lat, long

def get_direction_distance(dustbin1, dustbin2):
    if dustbin1.id == dustbin2.id:
        return 0.0

    key = str(dustbin1.id) + '|' + str(dustbin2.id)

    if key in distances.keys():
        return distances[key]
    else:
        now = datetime.now()
        # directions_results = gm.directions(str(lat1)+', '+str(long1),
        #                                str(lat2)+', '+str(long2),
        #                                mode='driving',
        #                                avoid='ferries',
        #                                departure_time=now
        #                                 )[0]['legs'][0]['distance']['value']

        directions_results = gm.distance_matrix(
                                                    # origins=str(lat1) + ', ' + str(long1),
                                                    # destinations=str(lat2)+', '+str(long2)
            origins=dustbin1.address,
            destinations=dustbin2.address
                                               )['rows'][0]['elements'][0]['distance']['value']
                                           # departure_time=now,
        # print(directions_results)
        distances[key] = directions_results
        print(distances)

        return directions_results
