'''
Represents the chromosomes in GA's population.
The object is collection of individual routes taken by trucks.
'''
from excel import *
from routemanager import *

class Route:
    # Good old constructor
    def __init__ (self, route=None):
        # 2D array which is collection of respective routes taken by trucks
        self.route = []
        # 1D array having routes in a series - used during crossover operation
        self.base = []
        # 1D array having route lengths
        self.routeLengths = route_lengths()

        for i in range(numTrucks):
            self.route.append([])

        # fitness value and total distance of all routes
        self.fitness = 0
        self.distance = 0

        # creating empty route
        if route == None:
            for i in range(RouteManager.numberOfDustbins()-1):
                self.base.append(Dustbin(None))

        else:
            self.route = route

    def generateIndividual (self):
        k=0
        # put 1st member of RouteManager as it is (It represents the initial node) and shuffle the rest before adding
        for dindex in range(1, RouteManager.numberOfDustbins()):
            self.base[dindex-1] = RouteManager.getDustbin(dindex)
        random.shuffle(self.base)

        for i in range(numTrucks):
            self.route[i].append(RouteManager.getDustbin(0)) # add same first node for each route
            for j in range(self.routeLengths[i]-1):
                self.route[i].append(self.base[k]) # add shuffled values for rest
                k+=1

    # Returns j'th dustbin in i'th route
    def getDustbin(self, i, j):
        return self.route[i][j]

    # Sets value of j'th dustbin in i'th route
    def setDustbin(self, i, j, db):
        self.route[i][j] = db
        #self.route.insert(index, db)
        self.fitness = 0
        self.distance = 0

    # Returns the fitness value of route
    def getFitness(self):
        if self.fitness == 0:
            fitness = 1/self.getDistance()

        return fitness

    # Return total ditance covered in all subroutes
    def getDistance(self):
        if self.distance == 0.0:
            routeDistance = 0.0

            for i in range(numTrucks):
                for j in range(self.routeLengths[i]):
                    fromDustbin = self.getDustbin(i, j)

                    if j+1 < self.routeLengths[i]:
                        destinationDustbin = self.getDustbin(i, j + 1)

                    else:
                        destinationDustbin = self.getDustbin(i, 0)

                    routeDistance += fromDustbin.distanceTo(destinationDustbin)

        distance = routeDistance
        return routeDistance

    # Checks if the route contains a particular dustbin
    def containsDustbin(self, db):
        if db in self.base: #base <-> route
            return True
        else:
            return False

    # Returns route in the form of a string
    def toString (self):
        geneString = '|'
        print (self.routeLengths)
        #for k in range(RouteManager.numberOfDustbins()-1):
        #    print (self.base[k].toString())
        truck1 = []
        truck2 = []
        truck3 = []

        for i in range(numTrucks):
            for j in range(self.routeLengths[i]):
                place = self.getDustbin(i, j).toString()
                geneString += place + '|'

                if i == 0:
                    truck1.append(place)
                elif i == 1:
                    truck2.append(place)
                else:
                    truck3.append(place)

            geneString += '\n'

        save_data('Database.xlsx', 'results3', 2, 2, truck1, truck2, truck3)

        return geneString

    def get_route_distance(self, truck_index):

        place1 = self.getDustbin(truck_index, 0)
        distance = 0.0
        for j in range(self.routeLengths[truck_index] + 1):
            if j == self.routeLengths[truck_index]:
                place2 = self.getDustbin(truck_index, 0)
            else:
                place2 = self.getDustbin(truck_index, j)
            distance = distance + place1.distanceTo(place2)
            print('Distance from ', place1.toString(), ' to ', place2.toString(), ':', place1.distanceTo(place2))
            place1 = place2
        return distance

