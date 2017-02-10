"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

Reading csv, json, xlsx, txt files with Pandas.

Note:
    * Pandas can also accept a url i.e. http://localhost/supermarket.csv
      as a parameter.  This is very useful in web automation

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
    # ... CSV
    # -------------------------------------------------------------------------

    print('...LOADING FROM CSV')
    
    # Output:
    # ID          Address           City             State Country         Name  \
    # 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira
    # 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop
    # 2   3      332 Hill St  San Francisco  California 94114     USA  Super River
    # 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop
    # 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez
    # 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley

    #    Employees
    # 0          8
    # 1         15
    # 2         25
    # 3         10
    # 4         12
    # 5         20
    df1 = pandas.read_csv("{}/supermarkets.csv".format(RES_DIR))  
    print(df1)

    # Use a column as the Python index
    df1.set_index('ID')

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
    df2 = pandas.read_json("{}/supermarkets.json".format(RES_DIR))  
    print(df2)


    # -------------------------------------------------------------------------
    # ... EXCEL
    # -------------------------------------------------------------------------

    print('...LOADING FROM EXCEL')
    
    # Output:
    #    ID          Address           City             State Country  \
    # 0   1     3666 21st St  San Francisco          CA 94114     USA
    # 1   2   735 Dolores St  San Francisco          CA 94119     USA
    # 2   3      332 Hill St  San Francisco  California 94114     USA
    # 3   4     3995 23rd St  San Francisco          CA 94114     USA
    # 4   5  1056 Sanchez St  San Francisco        California     USA
    # 5   6  551 Alvarado St  San Francisco          CA 94114     USA

    #   Supermarket Name  Number of Employees
    # 0          Madeira                    8
    # 1      Bready Shop                   15
    # 2      Super River                   25
    # 3       Ben's Shop                   10
    # 4          Sanchez                   12
    # 5       Richvalley                   20
    df3 = pandas.read_excel(
        "{}/supermarkets.xlsx".format(RES_DIR), sheetname=0)  
    print(df3)


    # -------------------------------------------------------------------------
    # ... TXT, comma separated
    # -------------------------------------------------------------------------

    print('...LOADING FROM TXT, comma separated')
    
    # # Output:
    #    ID          Address           City             State Country         Name  \
    # 0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira
    # 1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop
    # 2   3      332 Hill St  San Francisco  California 94114     USA  Super River
    # 3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop
    # 4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez
    # 5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley

    #    Employees
    # 0          8
    # 1         15
    # 2         25
    # 3         10
    # 4         12
    # 5         20
    df4 = pandas.read_csv("{}/supermarkets-commas.txt".format(RES_DIR))  
    print(df4)    

    # -------------------------------------------------------------------------
    # ... TXT, colon
    # -------------------------------------------------------------------------

    print('...LOADING FROM TXT, semi-colon separated')
    
    # Output:
    #    ID          Address           City             State Country          Name  \
    # 0   1     3666 21st St  San Francisco          CA 94114     USA       Madeira
    # 1   2   735 Dolores St  San Francisco          CA 94119     USA   Bready Shop
    # 2   3      332 Hill St  San Francisco  California 94114     USA   Super River
    # 3   4     3995 23rd St  San Francisco          CA 94114     USA    Ben's Shop
    # 4   5  1056 Sanchez St  San Francisco        California     USA       Sanchez
    # 5   6  551 Alvarado St  San Francisco          CA 94114     USA    Richvalley

    #    Employees
    # 0          8
    # 1         15
    # 2         25
    # 3         10
    # 4         12
    # 5         20
    df5 = pandas.read_csv("{}/supermarkets-semi-colons.txt".format(RES_DIR), 
                          sep=';')  
    print(df5)
