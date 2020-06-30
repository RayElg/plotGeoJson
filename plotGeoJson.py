import json
import numpy as np
from matplotlib import pyplot as plt
    
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
    elif type == "MultiLineString":
        return x["geometry"]["coordinates"][0][0]
    else:
        print("unexpected geometry type:")
        print(type)



def justDots(x,y,figsize):
    plt.figure(figsize=figsize) #Size of final image. figsize * 160 = resolution
    plt.scatter(x,y,s=0.5,marker=",",antialiased=False) 
    plt.gca().set_aspect('equal', adjustable='box') #Prevents the figure from having latitude&longitude skewed
    plt.axis("off")
    plt.savefig("justDots.png",facecolor="black",dpi=160)

def heatMap(x,y,gridsize):
    plt.gca().set_aspect('equal', adjustable='box')
    plt.hexbin(x,y,gridsize=gridsize,bins="log",cmap='inferno',linewidths=0.2)
    plt.axis("off")
    plt.savefig("heatMap.png",dpi=6*gridsize,bbox_inches='tight',facecolor="black")

#mainline
    
print("Enter the name of the geojson file")
fileName = input()

try:
    with open(fileName, encoding='utf-8') as f: #Load the features dictionary from the featurecollection
        data = (json.load(f))["features"]
except:
    print("File error: " + fileName)
else:
    #Get a uniform list of coordinates for each feature
    coordList = [firstCoord(x) for x in data]
    #Display on graph
    npArr = np.array(coordList)
    x, y = npArr.T

    #Get plot type & params from user, execute function
    try:
        print("'dots' or 'heat'?")
        entry = input()
        if(entry == 'dots'):
            print("Figsize in inches? dpi=160 Example: '16,9'")
            justDots(x,y,tuple(map(float,input().split(','))))
        elif(entry == 'heat'):
            print("Number of bins?")
            heatMap(x,y,int(input()))
    except:
        print("Input error")






