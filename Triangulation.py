import triangle as tr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Data/poles.csv')


def prims(vertices):

    unconnected = copy.copy(vertices)
    connected = [unconnected.pop()]
    print(connected)
    print(unconnected)
    connections = []

    while unconnected:
        print(connected)
        smallest = float('inf')
        candidate = ()
        for index1,node1 in enumerate(connected):
            for index2,node2 in enumerate(unconnected):

                #find the smallest distance connection
                print("node1",node1)
                print("node2",node2)
                if distance(node1,node2)<smallest:
                    smallest = distance(node1,node2)
                    candidate = (node1,node2)
                    print("replaced")

        #add the smallest distance to the graph
        print("candidate is ")
        print(candidate)
        connections.append(candidate)
        #remove node2 from unconnected
        unconnected.remove(candidate[1])
        connected.append(candidate[1])
    print("connections ",connections)

    return connections


def distance(node1,node2):

    return sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)


def getEdges(triangulation,df):
    '''
    Takes in a triangulation and returns only the vetices that ahve an edge and a
    :param triangulation:
    :return:
    '''

    nodes  = []
    for t in triangulation['triangles']:

        lines = []
        lines.append((t[0],t[1]))
        lines.append((t[1],t[2]))
        lines.append((t[2], t[0]))

        for l in lines:
            if df['type'][l[0]] == 'house' and df['type'][l[1]] == 'house':
                continue
            elif df['type'][l[0]] == 'pole' and df['type'][l[1]] == 'house':
                nodes.append(l)
            elif df['type'][l[0]] == 'hose' and df['type'][l[1]] == 'pole':
                nodes.append(l)
            else:
                nodes.append(l)

    return nodes

data = pd.read_csv(filename)


def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return (sorted(tup, key=lambda x: x[1]))
print(data.shape)
coords = data[['lon','lat']].to_numpy()

cdd = {'vertices': coords}

t = tr.triangulate(cdd)


print(getEdges(t,data))
print(t['triangles'])
#tr.plot(plt.axes(),**t)
#plt.show()




