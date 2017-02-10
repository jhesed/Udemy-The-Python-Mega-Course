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
from bs4 import BeautifulSoup

if __name__ == '__main__':


    # ... SECTIONS :: 
    # 142: Demonstration of Webscraping Application
    # 143: Understanding the Problem and Loading the Webpage in Python
    # 144: Extracting Divisions of All Properties

    # Load the first page
    req = requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # Get all real estate proerty rows
    all_properties = soup.find_all('div', {'class': 'propertyRow'})

    # Get the property price and remove the spaces
    # Output:
    # $725,000
    price1 = all_properties[0].find('h4', {'class': 'propPrice'}).text.strip()
    print(price1)

    # ... SECTIONS ::
    # 145: Extracting Addresses and Property Details
    
    # Using a loop
    for item in all_properties:
        
        # Retrieve the prices
        price = item.find('h4', {'class', 'propPrice'}).text.strip()
        print(price)

        # Retrieve the address
        address1 = item.find_all('span', 'propAddressCollapse')[0].text
        address2 = item.find_all('span', 'propAddressCollapse')[1].text
        print(address1)
        print(address2)

        # Retrieve bed info (which is not present all the time)
        try:
            # bed_info = item.find('span', {'class': 'infoBed'}).text
            
            # Retrieve only the number of beds
            bed_count = item.find('span', {'class': 'infoBed'}).find('b').text
            print(bed_count)

        except:
            # Nothing to do for now
            print(None)

        try:
            # Retrieve square feet
            sqft = item.find('span', {'class': 'infoSqFt'}).find('b').text
            print(sqft)

        except:
            print(None)

        # Retrieve full bath info (which is not present all the time)
        try:
            # Retrieve only the number of full bath
            full_bath_count = item.find(
                'span', {'class': 'infoValueFullBath'}).find('b').text
            print(full_bath_count)

        except:
            print(None)

        try:
            # Retrieve only the number of half bath
            half_bath_count = item.find(
                'span', {'class': 'infoValueHalfBath'}).find('b').text
            print(half_bath_count)

        except:
            print(None)


        # New line for viewing purpose
        print('')

        # ... SECTIONS ::
        # 146: Extracting Elements with no Unique Identifiers

        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            # print(column_group)

            for feature_group, feature_name in zip(
                column_group.find_all('span', {'class': 'featureGroup'}),
                column_group.find_all('span', {'class': 'featureName'})):

                if 'lot size' in feature_group.text.lower():
                    lot_size = feature_name.text
                else:
                    lot_size = None
                print(lot_size)



