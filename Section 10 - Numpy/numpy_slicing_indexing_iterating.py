"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 10: Numpy

Indexing, slicing and iterating

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
import cv2

if __name__ == '__main__':
    

    # ... SLICING

    im_g = cv2.imread('res/smallgray.png', 0)

    # Output:
    # [[187 158 104 121 143]
    #  [198 125 255 255 147]
    #  [209 134 255  97 182]]
    print(im_g)

    # Output:
    # [[187 158 104 121 143]
    #  [198 125 255 255 147]]
    print(im_g[0:2])

    # Output:
    # [[104 121]
    #  [255 255]]
    print(im_g[0:2, 2:4])

    # Output:
    # 158
    print(im_g[0, 1])


    # ... ITERATING

    # Output:
    # [187 158 104 121 143]
    # [198 125 255 255 147]
    # [209 134 255  97 182]
    for i in im_g:
        print(i)
    
    # Output:
    # [187 198 209]
    # [158 125 134]
    # [104 255 255]
    # [121 255  97]
    # [143 147 182]
    for i in im_g.T:
        print(i)
    
    # Output:
    # 187
    # 158
    # 104
    # 121
    # 143
    # 198
    # 125
    # 255
    # 255
    # 147
    # 209
    # 134
    # 255
    # 97
    # 182
    for i in im_g.flat:
        print(i)
    
    