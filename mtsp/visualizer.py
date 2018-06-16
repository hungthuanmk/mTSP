from route import *
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, index):
        self.index = index
        self.f = plt.figure(index)
        plt.title('OR mTSP')

    def draw_route(self, route, truck_index):
        place1 = route.getDustbin(truck_index, 0)
        # distance = 0.0
        for j in range(route.routeLengths[truck_index] + 1):
            if j == route.routeLengths[truck_index]:
                place2 = route.getDustbin(truck_index, 0)
            else:
                place2 = route.getDustbin(truck_index, j)
            plt.figure(self.index)

            if truck_index==0:
                color = 'green'
            elif truck_index==1:
                color = 'red'
            else:
                color = 'blue'

            if place1 == route.getDustbin(truck_index, 0):
                color = 'purple'
            plt.plot(place1.getlong(), place1.getlat(), 'o', color=color)
            # plt.arrow(place1.getlat(), place1.getlong(), place2.getlat()-place1.getlat(), place2.getlong()-place1.getlong())
            place1 = place2
            plt.pause(0.0000000000001)

    def plot(self, xaxis, yaxis):
        plt.figure(self.index)
        plt.plot(xaxis, yaxis, 'r-')
        plt.pause(0.0001)

    def show(self):
        self.f.show()


    def clear(self):
        plt.figure(self.index)
        plt.cla()

