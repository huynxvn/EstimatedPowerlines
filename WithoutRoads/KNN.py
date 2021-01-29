##implementation of k nearest neighbours with great circle implemented

from GreatCircle import *
from math import sqrt
import random
def knn_greatcircle(df,npoints = None,distfunc = None):
    nentries = len(df)
    converged = False


    if not distfunc:
        distfunc = lambda x: sqrt(x[0] ** 2 + x[1] ** 2)
    if not npoints:
        npoints = nentries//3


    df['cluster'] = 1
    bbox =  [max(df['lat']),max(df['lon']),min(df['lon']),min(df['lon'])]

    #randomly select a centroid
    centroids = [(random.random(bbox[0],bbox[2]),random.random(bbox[1],bbox[3])) for i in range(npoints)]
    print(centroids)
    print(df.head())
    return(0)
    '''
    while not converged:
        ## calculate nearest distance
        for i in
    '''