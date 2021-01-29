import triangle as tr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Data/poles.csv')

data = pd.read_csv(filename)

coords = data[['lon','lat']].to_numpy()

cdd = {'vertices': coords}

t = tr.triangulate(cdd)


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

def createLinestring(lines,df):
    
print(getEdges(t,data))
print(t['triangles'])
tr.plot(plt.axes(),**t)
plt.show()