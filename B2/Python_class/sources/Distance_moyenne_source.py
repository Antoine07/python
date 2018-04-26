import math as m

class AverageDistance:

    """
    définir la distance avec une fonction lambda
    """
    def __init__(self, data, distance):
        self.data = data 
        self.distance = distance

    def average(self, point):
        pass

class Center(AverageDistance):

    def build(self):
        pass

# test des classes
euclidean = lambda x,y : m.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
l = [(1,3),(2,0),(0,4),(6,5),(3,4),(3,1)]
a = AverageDistance( l, euclidean )

print(a.average((5,4)))

absolute = lambda x,y : abs(x[0]-y[0]) + abs(x[1]-y[1])
center = Center(l, absolute )

print(center.build())

center = Center(l, euclidean )

print(center.build())


