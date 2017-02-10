"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

Updating and Adding Columns 

Author: Jhesed Tacadena
Date: 2017-01-24

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

    # Adding column:
    # note that df7.shape[0] is used to fill all rows with Asia
    # df7.shape[0] # no of rows
    # df7.shape[1] # no of columns    
    # Output:
    #            Address           City Country  Employees  ID         Name  \
    # 0     3666 21st St  San Francisco     USA          8   1      Madeira
    # 1   735 Dolores St  San Francisco     USA         15   2  Bready Shop
    # 2      332 Hill St  San Francisco     USA         25   3  Super River
    # 3     3995 23rd St  San Francisco     USA         10   4   Ben's Shop
    # 4  1056 Sanchez St  San Francisco     USA         12   5      Sanchez
    # 5  551 Alvarado St  San Francisco     USA         20   6   Richvalley

    #               State continent
    # 0          CA 94114      Asia
    # 1          CA 94119      Asia
    # 2  California 94114      Asia
    # 3          CA 94114      Asia
    # 4        California      Asia
    # 5          CA 94114      Asia
    df7['continent'] = df7.shape[0]*['Asia']
    print(df7)

    # Updating row:
    # Output
    #        Address           City Country  Employees  ID         Name  \
    # 0     3666 21st St  San Francisco     USA          8   1      Madeira
    # 1   735 Dolores St  San Francisco     USA         15   2  Bready Shop
    # 2      332 Hill St  San Francisco     USA         25   3  Super River
    # 3     3995 23rd St  San Francisco     USA         10   4   Ben's Shop
    # 4  1056 Sanchez St  San Francisco     USA         12   5      Sanchez
    # 5  551 Alvarado St  San Francisco     USA         20   6   Richvalley

    #               State continent
    # 0          CA 94114   America
    # 1          CA 94119      Asia
    # 2  California 94114      Asia
    # 3          CA 94114      Asia
    # 4        California      Asia
    # 5          CA 94114      Asia
    df7['continent'][0] = 'America'
    print(df7)

    # Updating column (i.e. title) is quite tricky.
    # We need to transpose rows as columns, then edit the row
    # df7_t = df7.T  # Transpose
    # df7_t['My Address'] = ['My City', 'My Country', 10, 7, 'My Shop', 'My Name',
    #                        'My State', 'My Continent']
    # df7_t = df7_t.T
    # print(df7_t)