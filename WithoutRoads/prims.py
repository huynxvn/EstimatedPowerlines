import copy
import numpy as np
from math import sqrt
import random
import matplotlib.pyplot as plt

def prims(vertices):

    unconnected = copy.copy(vertices)
    connected = [unconnected.pop()]

    connections = []

    while unconnected:

        smallest = float('inf')
        candidate = ()
        for index1,node1 in enumerate(connected):
            for index2,node2 in enumerate(unconnected):

                #find the smallest distance connection

                if distance(node1,node2)<smallest:
                    smallest = distance(node1,node2)
                    candidate = (node1,node2)


        #add the smallest distance to the graph

        connections.append(candidate)
        #remove node2 from unconnected
        unconnected.remove(candidate[1])
        connected.append(candidate[1])


    return connections


def distance(node1,node2):

    return sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)
'''
mylist = [(round(random.uniform(0,100)),round(random.uniform(0,100)))for i in range(100)]


connections = prims(mylist)


for pointPair in connections:

        point1 = pointPair[0]
        point2 = pointPair[1]

        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values,color = 'red')
plt.plot(connections[0][0][0], connections[0][0][1], marker='^', markersize=8, color="green")
plt.show()
'''

