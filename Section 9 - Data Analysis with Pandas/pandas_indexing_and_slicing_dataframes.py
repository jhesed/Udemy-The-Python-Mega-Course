"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

Indexing and Slicing Dataframes

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

    # Use as index
    # this is non-destructive. Meaning, printing df7 will not change output
    df7.set_index('Address')

    # so, to actually change df7, re-assign it:
    # Output:
    #                           City Country  Employees  ID         Name  \
    # Address
    # 3666 21st St     San Francisco     USA          8   1      Madeira
    # 735 Dolores St   San Francisco     USA         15   2  Bready Shop
    # 332 Hill St      San Francisco     USA         25   3  Super River
    # 3995 23rd St     San Francisco     USA         10   4   Ben's Shop
    # 1056 Sanchez St  San Francisco     USA         12   5      Sanchez
    # 551 Alvarado St  San Francisco     USA         20   6   Richvalley

    #                             State
    # Address
    # 3666 21st St             CA 94114
    # 735 Dolores St           CA 94119
    # 332 Hill St      California 94114
    # 3995 23rd St             CA 94114
    # 1056 Sanchez St        California
    # 551 Alvarado St          CA 94114
    df7 = df7.set_index('Address')
    print(df7)

    print('...USING LOC')
    # Output: 
    #                Country  Employees  ID
    # Address
    # 735 Dolores St     USA         15   2
    # 332 Hill St        USA         25   3
    # [COLUMN SLICE, ROW SLICE]
    print(df7.loc['735 Dolores St':'332 Hill St', 'Country': 'ID'])


    print('...USING ILOC')
    # ..Note: loc is not very common way to access Pandas elements
    # Using iloc
    # Output:
    #                Country  Employees  ID
    # Address
    # 735 Dolores St     USA         15   2
    # 332 Hill St        USA         25   3
    # Country      USA
    # Employees     10
    # Name: 3995 23rd St, dtype: object
    # [COLUMN SLICE, ROW SLICE]
    print(df7.iloc[3, 1:3])


    print('...USING IX')
    # ix = combination of labels and indexes
    # Output:
    # Ben's Shop
    print(df7.ix[3, 4])