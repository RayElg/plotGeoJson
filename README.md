# plotGeoJson
Creates a plot of GeoJson features

Turns a dataset containing GeoJson features (such as one from [http://overpass-turbo.eu/]) into a map drawn only with these features

#### Example, using dataset of all pubs on openstreetmaps in the U.K.

![justDots.png](https://github.com/RayElg/plotGeoJson/blob/master/justDots.png?raw=true)

#### Or this example, using hexbin rather than scatterplot on a dataset of places of worship in Portugal

![heatMap.png](https://github.com/RayElg/plotGeoJson/blob/master/heatMap.png?raw=true)

Not suitable for drawing maps of roads, large lakes, or rivers, as only the first coordinate of a feature is drawn.
