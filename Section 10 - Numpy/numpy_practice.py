"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 10: Numpy

Author: Jhesed Tacadena
Date: 2017-01-25

Section 9 Contents:
    61. What is Numpy?
    62. Installing OpenCV (cv2)
    63. Images to Numpy and Vice-versa
    64. Indexing, Slicing and Iterating
    65. Stacking and Splitting

"""

import numpy

if __name__ == '__main__':
    
    # Example usage: Image representation
    # Output:
    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    #  25 26]
    # 1 dimensional array
    n = numpy.arange(27)
    print(n)

    # 2-d array
    # Output:
    # [[ 0  1  2  3  4  5  6  7  8]
    #  [ 9 10 11 12 13 14 15 16 17]
    #  [18 19 20 21 22 23 24 25 26]]
    n = n.reshape(3, 9)
    print(n)

    # 3-d array
    # Output:
    # [[[ 0  1  2]
    #   [ 3  4  5]
    #   [ 6  7  8]]

    #  [[ 9 10 11]
    #   [12 13 14]
    #   [15 16 17]]

    #  [[18 19 20]
    #   [21 22 23]
    #   [24 25 26]]]
    n = n.reshape(3, 3, 3)
    print(n)

    # Create numpy from Python list
    # Output:
    # [[123, 12, 123, 12, 33] [] []]
    m = numpy.asarray([[123, 12, 123, 12, 33],[],[]])
    print(m)