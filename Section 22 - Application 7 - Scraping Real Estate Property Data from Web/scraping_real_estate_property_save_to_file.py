"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 22: Scraping Real Estate Property Data from the Web

Original website is: `http://century21.com`

But it was updates a cached version will be used isntead for practice purpose:
    `http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/`

Author: Jhesed Tacadena
Date: 2017-01-27

Section 22 Contents:
   142: Demonstration of Webscraping Application
   143: Understanding the Problem and Loading the Webpage in Python
   144: Extracting Divisions of All Properties
   145: Extracting Addresses and Property Details
   146: Extracting Elements with no Unique Identifiers
   147: Saving the Extracted Data in CSV
   148: Crawling Through Webpages

Notes:
    * Request library is used to load the page
    * Beautiful Soup to process information
    * Read data policy of webpage before scraping

"""

import requests
import pandas
from bs4 import BeautifulSoup

if __name__ == '__main__':
    BASE_URL = 'http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='

    # ... SECTIONS :: 
    # 142: Demonstration of Webscraping Application
    # 143: Understanding the Problem and Loading the Webpage in Python
    # 144: Extracting Divisions of All Properties

    # Get page count

    req = requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    page_count = int(soup.find_all('a', {'class': 'Page'})[-1].text)

    # List to hold the dictionary of results
    l = []

    # Crawls in pages, step is 10 as observed in the url
        
    for page in range(0, page_count*10, 10):

        # Load the page dynamically
        req = requests.get(BASE_URL + str(page) + '.html')
        content = req.content

        soup = BeautifulSoup(content, 'html.parser')

        # Get all real estate proerty rows
        all_properties = soup.find_all('div', {'class': 'propertyRow'})

        # ... SECTIONS ::
        # 145: Extracting Addresses and Property Details
     
        for item in all_properties:
            
            # Dict to hold the item values
            d = {}

            # Retrieve the address
            d['address'] = item.find_all('span', 'propAddressCollapse')[0].text
            d['locality'] = item.find_all('span', 'propAddressCollapse')[1].text

            # Retrieve the prices
            d['price'] = item.find('h4', {'class', 'propPrice'}).text.strip()
                    
            try:
                # Retrieve only the number of beds
                d['bed_count'] = item.find('span', {'class': 'infoBed'}).find('b').text
               
            except:
                d['bed_count'] = None

            try:
                # Retrieve square feet
                d['sqft'] = item.find('span', {'class': 'infoSqFt'}).find('b').text
            except:
                d['sqft'] = None
            
            try:
                # Retrieve only the number of full bath
                d['full_bath_count'] = item.find(
                    'span', {'class': 'infoValueFullBath'}).find('b').text
            except:
                d['full_bath_count'] = None

            try:
                d['half_bath_count'] = item.find(
                    'span', {'class': 'infoValueHalfBath'}).find('b').text
                
            except:
                d['half_bath_count'] = None

            # ... SECTIONS ::
            # 146: Extracting Elements with no Unique Identifiers

            for column_group in item.find_all('div', {'class': 'columnGroup'}):
                # print(column_group)

                for feature_group, feature_name in zip(
                    column_group.find_all('span', {'class': 'featureGroup'}),
                    column_group.find_all('span', {'class': 'featureName'})):

                    if 'lot size' in feature_group.text.lower():
                        d['lot_size'] = feature_name.text
                    else:
                        d['lot_size'] = None
                    
            # Append to list
            l.append(d)

    # Create a Pandas Data Frame using the list
    df = pandas.DataFrame(l)

    # Save results to csv file
    df.to_csv('web-scraping-results.csv')
