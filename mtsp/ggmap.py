import googlemaps as ggm
from datetime import datetime
# api_key = 'AIzaSyDSbtA0_Tz3jt215tYXIOTKArJR5zHWfYI'
api_key = 'AIzaSyCuHRSGj59pkMXFQVyPcpTX7ORNDBS0hrA'
gm = ggm.Client(key=api_key)

distances = dict()

def get_coordinate(address):
    geocode_result = gm.geocode(address)[0]
    location = geocode_result['geometry']['location']
    lat = location['lat']
    long = location['lng']
    print('get_position(', address, ') = ', lat, ' | ', long)
    return lat, long

def get_direction_distance(lat1, long1, lat2, long2, address1, address2):
    if lat1 == lat2 and long1 == long2:
        return 0.0

    key = str(lat1)+str(long1)+str(lat2)+str(long2);

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
            origins=address1,
            destinations=address2
                                               )['rows'][0]['elements'][0]['distance']['value']
                                           # departure_time=now,
        # print(directions_results)
        distances[key] = directions_results
        print(distances)
        return directions_results

