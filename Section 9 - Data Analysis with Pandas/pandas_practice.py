"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 9: Data Analysis with Pandas

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


if __name__ == '__main__':

    # -------------------------------------------------------------------------
    print("..... PANDAS: Using lists")
    
    # Output:
    # 
    #       0   1   2
    #    0  1   2   3
    #    1  5  10  15
    print(pandas.DataFrame([[1, 2, 3], [5, 10, 15]]))

    # Output:
    #    Price  Age  Value
    # 0      1    2      3
    # 1      5   10     15
    print(pandas.DataFrame([[1, 2, 3], [5, 10, 15]], 
                          columns=['Price', 'Age', 'Value']))

    # Output:
    #         Price  Age  Value
    # First       1    2      3
    # Second      5   10     15
    data_frame_obj = pandas.DataFrame([[1, 2, 3], [5, 10, 15]], 
                                      columns=['Price', 'Age', 'Value'],
                                      index=['First', 'Second'])
    print(data_frame_obj)

    # Output:
    # Price    3.0
    # Age      6.0
    # Value    9.0
    # dtype: float64
    print(data_frame_obj.mean())

    # Output:
    # First     1
    # Second    5
    # Name: Price, dtype: int64
    print(data_frame_obj.Price)

    # Output:
    # 5
    print(data_frame_obj.Price.max())

    # -------------------------------------------------------------------------
    print("..... PANDAS: Using dicionaries")
    
    # Output:
    #    Name   Surname
    # 0  Jhesed  Tacadena
    # 1  Hannah       NaN
    data_frame_obj = pandas.DataFrame([
        {'Name': 'Jhesed', "Surname": "Tacadena"}, 
        {'Name': 'Hannah'}])
    print(data_frame_obj)