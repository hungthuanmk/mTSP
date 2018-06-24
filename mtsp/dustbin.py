'''
Represents nodes in the problem graph or network.
Locatin coordinates can be passed while creating the object or they
will be assigned random values.
'''
from globals import *
from ggmap import *
from math import sin, cos, atan2, radians, sqrt

class Dustbin:

    def __init__ (self, _id, _address=None):
        self.address = _address
        self.id = _id
        if _address is None:
            self.lat = self.long = -1
        else:
            self.lat, self.long = get_coordinate(_address)
            # self.lat = 1
            # self.long = 1
        # //print('Created id ', self.id)
    def getlat (self):
        return self.lat

    def getlong (self):
        return self.long

# Returns distance to the dustbin passed as argument
# def distanceTo (self, db):
# 	xDis = abs(self.getX() - db.getX())
# 	yDis = abs(self.getY() - db.getY())
# 	dis = math.sqrt((xDis*xDis) + (yDis*yDis))
# 	return dis

    # def distanceTo(self, db):
    #     lon1, lat1 = self.long, self.lat
    #     lon2, lat2 = db.long, db.lat
    #
    #     R = 6371000  # radius of Earth in meters
    #     phi_1 = radians(lat1)
    #     phi_2 = radians(lat2)
    #
    #     delta_phi = radians(lat2 - lat1)
    #     delta_lambda = radians(lon2 - lon1)
    #
    #     a = sin(delta_phi / 2.0) ** 2 + \
		# 	cos(phi_1) * cos(phi_2) * \
		# 	sin(delta_lambda / 2.0) ** 2
    #     c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #
    #     return R * c

    def distanceTo(self, db):
        return get_direction_distance(self, db)


    # Gives string representation of the Object with coordinates
    def toString (self):
        # s =  '(' + str(self.getlat()) + ',' + str(self.getlong()) + ')'
        # return s
        return self.address

    # Check if cordinates have been assigned or not
    # Dusbins with (-1, -1) as coordinates are created during creation on chromosome objects
    def checkNull(self):
        if self.getlat() == -1:
            return True
        else:
            return False


