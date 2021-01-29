

import csv
import numpy as np
import os
from Poles import *

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Data/poles.csv')
roads = []
with open('C:/Users/user/Documents/SummerProject/ExtractedCairns/roads.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

with open('C:/Users/user/Documents/SummerProject/ExtractedCairns/points.csv') as f:
    reader= csv.reader(f)
    build_centroids = list(reader)

print(build_centroids)

for line in data:
    line.pop()
    c = []
    for coord in line:
        cd = coord.split(' ')
        convert = tuple(map(float, cd))
        c.append(convert)


    roads.append(c)


print(build_centroids)

pole_output = candidates(roads)
pole_output = cull(pole_output)
print(pole_output.keys())
with open('C:/Users/user/Documents/SummerProject/ExtractedCairns/poles.csv','w',newline = '')  as out:
    csv_out = csv.writer(out)
    csv_out.writerow(["lon","lat","score",'type'])
    for row in pole_output.keys():
        to_write = [row[0],row[1],pole_output[row],"pole"]
        csv_out.writerow(to_write)
    for row in build_centroids:
        to_write = [row[0],row[1],10,"house"]
        csv_out.writerow(to_write)



