import triangle as tr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/user/Documents/SummerProject/ExtractedCairns/poles.csv')
print(data.head())

coords = data[['lon','lat']].to_numpy()
print(coords)
cdd = {'vertices': coords}
print(cdd)
t = tr.triangulate(cdd)
print(t)
tr.plot(plt.axes(),**t)
plt.show()