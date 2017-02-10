"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 10: Numpy

Images to Numpy and Vice Versa
Loading images with Numpy and OpenCV

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

    # Loads image
    # 2nd parameter means grayscale (if 0), colored if 1
    # Output: (Array representation of the image)
    # [[187 158 104 121 143]
    #  [198 125 255 255 147]
    #  [209 134 255  97 182]]
    im_g = cv2.imread('res/smallgray.png', 0)
    print(im_g)

    # Output: non-gray scale

    # Raises illegal instruction on current python (2.7) on 
    # this VM. Perhaps the libraries should be updated.
    # im_g = cv2.imread('res/smallgray.png', 1)
    # print(im_g)

    # Writes array of pixels as images
    cv2.imwrite('res/newsmallgray.png', im_g)
