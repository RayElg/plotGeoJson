import json
import numpy as np
from matplotlib import pyplot as plt

print("Enter the name of the geojson file")
fileName = input()

with open(fileName, encoding='utf-8') as f: #Load the features dictionary from the featurecollection
  data = (json.load(f))["features"]

#Will return the first coordinate for each feature. Since some features will contain many points, and only one is necessary.
#Note that this optimization reduces number of points to plot, however will not show the full size of features
def firstCoord(x):
    type = x["geometry"]["type"]
    if type == "Point":
        return x["geometry"]["coordinates"]
    elif type == "LineString":
        return x["geometry"]["coordinates"][0]
    elif type == "Polygon":
        return x["geometry"]["coordinates"][0][0]
    elif type == "MultiPolygon":
        return x["geometry"]["coordinates"][0][0][0]
    else:
        print("unexpected geometry type:")
        print(type)

#Get a uniform list of coordinates for each feature
coordList = [firstCoord(x) for x in data]


#Display on graph
data = np.array(coordList)
x, y = data.T
plt.scatter(x,y,s=0.8,marker=",")
plt.show()
