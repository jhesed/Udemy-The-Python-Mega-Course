"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 11: Creating Leaflet Webmaps with Python and Folium

Adding Markers to the map from CSV Data

Author: Jhesed Tacadena
Date: 2017-01-26

Section 11 Contents:
    66. Demonstration of Web Mapping Application
    67. Creating an Open Street Map with Python
    68. Adding Markers to the Map
    69. Adding Markers to the Map from CSV Data
    70. Rule-based COloring of Markers
    71. More on Rule-based Styling
    72. Calculating the Map Center from Input Data
    73. Adjusting the Code for the Latest Version of Folium
    74. Adding a Choropleth Map from GeoJson
    75. Adding a Layer Control Panel
    
"""

import pandas
import folium


# -----------------------------------------------------------------------------
def determine_color(elev):
    """
    Determines color based on elevation
    """

    # Decide the marker color
    if elev in range(1, 1000):
        marker_color = 'green'
    elif elev in range(1000, 3000):
        marker_color = 'orange'
    else:
        marker_color = 'red'                

    return marker_color


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    # Read the reference file for fetching coordinates
    df = pandas.read_csv('res/Volcanoes-USA.txt')

    # Create the folium map object
    # location = <latitude, longitude>
    # zoom_start = lower means zoom out
    # tiles = to override default tile view 
    # Use mean() to find the center of the map
    map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], 
                     zoom_start=4,
                     tiles='Stamen Terrain')

    # Adding map markers from csv

    for lat, lon, name, elev in zip(df['LAT'], df['LON'], 
                                    df['NAME'], df['ELEV']): 

        map.simple_marker(location=[lat, lon], popup=name,
                          marker_color=determine_color(elev))
    
    # Create the html file with the actual map
    map.create_map(path='folium_test.html')
