"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

Geocoding Addresses with Pandas and Geopy

Note:
    Geopy's geocode/Nominatim requires internet connection to determine 
    latitude/longhitude

Author: Jhesed Tacadena
Date: 2017-01-25

Section 9 Contents:
    53. What is Pandas?
    54. Getting Started with Pandas
    # run: Jupyter notebook, very nice on data analysis and web scraping
    55. Getting Started with Jupyter Notebooks 
    56. Loading Data in Python from CSV, Excel, TCT and JSOS files
    57. Indexing and Slicing Dataframes
    58. Dropping Dataframe Columns and rows
"""

import pandas
from geopy.geocoders import Nominatim

# The directory of the files to be read
RES_DIR = 'res'

if __name__ == '__main__':

    # -------------------------------------------------------------------------
    # ... JSON
    # -------------------------------------------------------------------------

    print('...LOADING FROM JSON')
    
    # Output:
    #           Address           City Country  Employees  ID         Name  \
    # 0     3666 21st St  San Francisco     USA          8   1      Madeira
    # 1   735 Dolores St  San Francisco     USA         15   2  Bready Shop
    # 2      332 Hill St  San Francisco     USA         25   3  Super River
    # 3     3995 23rd St  San Francisco     USA         10   4   Ben's Shop
    # 4  1056 Sanchez St  San Francisco     USA         12   5      Sanchez
    # 5  551 Alvarado St  San Francisco     USA         20   6   Richvalley

    #               State
    # 0          CA 94114
    # 1          CA 94119
    # 2  California 94114
    # 3          CA 94114
    # 4        California
    # 5          CA 94114
    df7 = pandas.read_json("{}/supermarkets.json".format(RES_DIR))  
    print(df7)

    # -------------------------------------------------------------------------
    # ... GEOPY
    # -------------------------------------------------------------------------

    # May raise Service timed out
    nom = Nominatim()
    res = nom.geocode('3995 23rd St, San Francisco, CA 94114')
    print(res.latitude)
    print(res.longitude)

    # We can then extract all address from Pandas then add pass it to geocode
    # .apply is a special method. i.e. mathematical method. Important! Don't
    # pass `()` in apply
    # We calculate in Pandas by batch without using `for` loop 
    df7['Coordinates'] = df7['Address'].apply(res.geocode)
    df7['Latitude'] = df7['Coordinates'].apply(lambda x: x.latitude if x else None)
    df7['Longitude'] = df7['Coordinates'].apply(lambda x: x.longitude if x else None)