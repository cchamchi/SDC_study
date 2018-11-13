#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:42:58 2018

@author: user
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
image = mpimg.imread('test.jpg')
ysize = image.shape[0]
xsize = image.shape[1]

image_R_filter=np.zeros((ysize,xsize,3),dtype=np.uint8)
image_R_filter[:,:,0]=image[:,:,0]

plt.imshow(image_R_filter)
plt.show()

image_G_filter=np.zeros((ysize,xsize,3),dtype=np.uint8)
image_G_filter[:,:,1]=image[:,:,1]

plt.imshow(image_G_filter)
plt.show()

image_B_filter=np.zeros((ysize,xsize,3),dtype=np.uint8)
image_B_filter[:,:,2]=image[:,:,2]

plt.imshow(image_B_filter)
plt.show()