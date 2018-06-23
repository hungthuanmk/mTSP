from galogic import *
from excel import *
from route import *
from ggmap import *
import progressbar
from visualizer import *
pbar = progressbar.ProgressBar()

# Add Dustbins
# for i in range(numNodes):
#     RouteManager.addDustbin(Dustbin('Vietnam'))

load_data('Database.xlsx', 2, 31)
# get_direction_distance(10.7826608, 106.695915, 10.7774284, 106.6856664)

random.seed(seedValue)
yaxis = []
# Fittest value (distance)
xaxis = []
# Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print('Initial minimum distance: ' + str(globalRoute.getDistance()))

visualizer = Visualizer(1)
visualizer2 = Visualizer(2)


# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
        visualizer.clear()
        visualizer.draw_route(globalRoute, 0)
        visualizer.draw_route(globalRoute, 1)
        visualizer.draw_route(globalRoute, 2)

    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

    visualizer2.plot(xaxis, yaxis)
    # plt.plot(xaxis, yaxis, 'r-')
    # plt.pause(0.02)
visualizer.show()
visualizer2.show()
print('Global minimum distance: ' + str(globalRoute.getDistance()))
print('Final Route: ' + globalRoute.toString())

print('Route 1 distance: ', globalRoute.get_route_distance(0))
print('Route 2 distance: ', globalRoute.get_route_distance(1))
print('Route 3 distance: ', globalRoute.get_route_distance(2))

# fig = plt.figure()

# plt.plot(xaxis, yaxis, 'r-')

# plt.show()
