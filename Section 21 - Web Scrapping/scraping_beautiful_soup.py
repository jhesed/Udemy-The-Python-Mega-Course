"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 21: Web Scraping

Author: Jhesed Tacadena
Date: 2017-01-27

Section 21 Contents:
    139 - Section Introduction
    140 - The Concept Behind Webscraping
    141 - Scraping a webpage with Requests and Beautiful Soup

Notes:
    * Request library is used to load the page
    * Beautiful Soup to process information

"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # Load the page
    req = requests.get('http://pythonhow.com/example.html')
    content = req.content

    # print(content)

    # Parse using beautiful soup
    # 2nd parameter is what to use as parser
    soup = BeautifulSoup(content, 'html.parser')

    # print test content
    print(soup.prettify())

    all_div_cities = soup.find_all('div', {'class': 'cities'})
    print('... All Cities')
    # Output:
    # [<div class="cities">\n<h2>London</h2>\n<p>London is the capital of 
    # England and it's been a British settlement since 2000 years ago. 
    # </p>\n</div>, <div class="cities">\n<h2>Paris</h2>\n<p>Paris is the 
    # capital city of France. It was declared capital since 508.</p>\n</div>, 
    # <div class="cities">\n<h2>Tokyo</h2>\n<p>Tokyo is the capital of Japan 
    # and one of the most populated cities in the world.</p>\n</div>]
    print(all_div_cities)

    print('... The first City')
    # We may also use soup.find() instead of find all to get the first
    # City. However, find_all returns a list so we can access it using slicing
    # Output:
    # <div class="cities">
    # <h2>London</h2>
    # <p>London is the capital of England and it's been a British settlement 
    # since 2000 years ago. </p>
    # </div>
    print(all_div_cities[0])

    print('... Retrieving the h2 element of the first city')
    # Output:
    # [<h2>London</h2>]
    print(all_div_cities[0].find_all('h2'))

    print('... Extracting only the text part')
    # Output:
    # London
    print(all_div_cities[0].find_all('h2')[0].text)


    print('... Extracting only the cities using loop')    
    # Output:
    # London
    # Paris
    # Tokyo
    for city in all_div_cities:
        print(city.find_all('h2')[0].text)

