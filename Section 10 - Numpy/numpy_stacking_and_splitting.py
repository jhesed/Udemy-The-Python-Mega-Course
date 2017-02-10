"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 10: Numpy

Stacking and Splitting

Author: Jhesed Tacadena
Date: 2017-01-26

Section 10 Contents:
    61. What is Numpy?
    62. Installing OpenCV (cv2)
    63. Images to Numpy and Vice-versa
    64. Indexing, Slicing and Iterating
    65. Stacking and Splitting

"""

import numpy
import cv2

if __name__ == '__main__':
    

    # ... STACKING

    im_g = cv2.imread('res/smallgray.png', 0)

    # Output:
    # [[187 158 104 121 143]
    #  [198 125 255 255 147]
    #  [209 134 255  97 182]]
    print(im_g)

    # Output:
    # [[187 158 104 121 143 187 158 104 121 143]
    #  [198 125 255 255 147 198 125 255 255 147]
    #  [209 134 255  97 182 209 134 255  97 182]]
    ims = numpy.hstack((im_g, im_g))
    print(ims)

    # Output:
    # [[187 158 104 121 143]
    #  [198 125 255 255 147]
    #  [209 134 255  97 182]
    #  [187 158 104 121 143]
    #  [198 125 255 255 147]
    #  [209 134 255  97 182]]
    # NOTE: Dimensions should match
    ims = numpy.vstack((im_g, im_g))
    print(ims)


    # ... SPLITTING

    # OUtput:
    # [array([[187],
    #        [198],
    #        [209],
    #        [187],
    #        [198],
    #        [209]], dtype=uint8), array([[158],
    #        [125],
    #        [134],
    #        [158],
    #        [125],
    #        [134]], dtype=uint8), array([[104],
    #        [255],
    #        [255],
    #        [104],
    #        [255],
    #        [255]], dtype=uint8), array([[121],
    #        [255],
    #        [ 97],
    #        [121],
    #        [255],
    #        [ 97]], dtype=uint8), array([[143],
    #        [147],
    #        [182],
    #        [143],
    #        [147],
    #        [182]], dtype=uint8)]
    lst = numpy.hsplit(ims, 5)
    print(lst)

    # Output:
    # [array([[187, 158, 104, 121, 143]], dtype=uint8), 
    # array([[198, 125, 255, 255, 147]], dtype=uint8), 
    # array([[209, 134, 255,  97, 182]], dtype=uint8), 
    # array([[187, 158, 104, 121, 143]], dtype=uint8), 
    # array([[198, 125, 255, 255, 147]], dtype=uint8), 
    # array([[209, 134, 255,  97, 182]], dtype=uint8)]
    lst = numpy.vsplit(ims, 6)
    print(lst)
