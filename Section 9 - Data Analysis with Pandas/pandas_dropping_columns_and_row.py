"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

Dropping DataFrame columns and rows

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
    #       Address           City Country  Employees  ID         Name  \
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


    # DROP does not delete in place, should be reassigned afterwards 
    # to take effect.  But we'll not do it here

    print('...DROPPING COLUMN')
    # OUtput:
    #                Address Country  Employees  ID         Name             State
    # 0     3666 21st St     USA          8   1      Madeira          CA 94114
    # 1   735 Dolores St     USA         15   2  Bready Shop          CA 94119
    # 2      332 Hill St     USA         25   3  Super River  California 94114
    # 3     3995 23rd St     USA         10   4   Ben's Shop          CA 94114
    # 4  1056 Sanchez St     USA         12   5      Sanchez        California
    # 5  551 Alvarado St     USA         20   6   Richvalley          CA 94114
    print(df7.drop('City', 1))

    print('...DROPPING COLUMN')
    # OUtput:
    #    Employees  ID         Name             State
    # 0          8   1      Madeira          CA 94114
    # 1         15   2  Bready Shop          CA 94119
    # 2         25   3  Super River  California 94114
    # 3         10   4   Ben's Shop          CA 94114
    # 4         12   5      Sanchez        California
    # 5         20   6   Richvalley          CA 94114
    print(df7.drop(df7.columns[0:3], 1))

    # OUtput:
    # RangeIndex(start=0, stop=6, step=1))
    print(df7.index)

    # Output:
    # Index([u'Address', u'City', u'Country', u'Employees', u'ID', u'Name',
    #  u'State'],
    #  dtype='object')
    print(df7.columns)


    print(df7.rows)
