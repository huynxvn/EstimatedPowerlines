import triangle as tr
import numpy as np

import matplotlib.pyplot as plt
import os
#from WithoutRoads.GreatCircle import *
#from WithoutRoads.prims import *

import copy
import numpy as np
from math import sqrt
import random


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

import math

EARTH_CIRCUMFERENCE = 6378137  # earth circumference in meters

def great_circle_distance(latlong_a, latlong_b):
    """
    >>> coord_pairs = [
    ...     # between eighth and 31st and eighth and 30th
    ...     [(40.750307,-73.994819), (40.749641,-73.99527)],
    ...     # sanfran to NYC ~2568 miles
    ...     [(37.784750,-122.421180), (40.714585,-74.007202)],
    ...     # about 10 feet apart
    ...     [(40.714732,-74.008091), (40.714753,-74.008074)],
    ...     # inches apart
    ...     [(40.754850,-73.975560), (40.754851,-73.975561)],
    ... ]

    >>> for pair in coord_pairs:
    ...     great_circle_distance(pair[0], pair[1]) # doctest: +ELLIPSIS
    83.325362855055...
    4133342.6554530...
    2.7426970360283...
    0.1396525521278...
    """
    lat1, lon1 = latlong_a
    lat2, lon2 = latlong_b

    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dLon / 2) * math.sin(dLon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = EARTH_CIRCUMFERENCE * c

    return d
#############################
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'upperperkins.csv')


array = np.genfromtxt(filename, delimiter=',')
transformer = array[1]
array = array[1:]
print(array)
print(array)

cdd = {'vertices': array}
t = tr.triangulate(cdd,'q30')

tr.plot(plt.axes(), **t)
plt.show()
print(t)

new_points = np.array([point for point in t['vertices'] if point not in array])
print(new_points)
pruned_added_points = []
for splitter in new_points:
    flag = False
    for point in array:
        if great_circle_distance(splitter,point)<18:
            flag = True
    if flag == False:
        pruned_added_points.append(splitter)

pruned_added_points.append(transformer)
pruned_added_points =  np.array(pruned_added_points)
connections = prims([tuple(i) for i in pruned_added_points])


def nearestpoints(a,b):

    '''
    connects each point in a to its nearest point in b and returns a list containting tuples of coordinates
    :param a:
    :param b:
    :return:
    '''
    result = []
    for i in a:
        min_dist = float('inf')
        closest_point = ()
        for j in b:

            if min_dist > great_circle_distance(i,j):
                closest_point = (i,j)
                min_dist = great_circle_distance(i,j)
        result.append(closest_point)
    return result

secondary_connections = nearestpoints([tuple(i) for i in array],[tuple(i) for i in pruned_added_points])

for pointPair in connections:

        point1 = pointPair[0]
        point2 = pointPair[1]

        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values,color = 'red')

for pointPair in secondary_connections:

        point1 = pointPair[0]
        point2 = pointPair[1]

        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values,color = 'red')
plt.scatter(array[:,0],array[:,1])
plt.scatter(pruned_added_points[:,0],pruned_added_points[:,1])

plt.show()