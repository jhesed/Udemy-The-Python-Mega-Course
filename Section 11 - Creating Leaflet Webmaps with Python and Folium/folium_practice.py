"""
Udemy: The Python Mega Course:  Building 10 Real World Applications

Section 11: Creating Leaflet Webmaps with Python and Folium

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

import folium

if __name__ == '__main__':
    
    # Create the folium map object
    # location = <latitude, longitude>
    # zoom_start = lower means zoom out
    # tiles = to override default tile view 
    map = folium.Map(location=[45.372, -121.697], zoom_start=10,
                     tiles='Stamen Terrain')

    # Adding map markers
    map.simple_marker(location=[45.3288, -121.6625], popup='Mt. Hood Meadows',
                      marker_color='red')

    map.simple_marker(location=[45.3311, -121.7311], popup='Timberlake Lodge',
                      marker_color='green')
    
    # Create the html file with the actual map
    map.create_map(path='folium_test.html')
