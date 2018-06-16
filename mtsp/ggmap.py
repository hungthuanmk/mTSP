import googlemaps as ggm
api_key = 'AIzaSyDSbtA0_Tz3jt215tYXIOTKArJR5zHWfYI'
gm = ggm.Client(key=api_key)


def get_coordinate(address):
    geocode_result = gm.geocode(address)[0]
    location = geocode_result['geometry']['location']
    lat = location['lat']
    long = location['lng']
    print('get_position(', address, ') = ', lat, ' | ', long)
    return lat, long

