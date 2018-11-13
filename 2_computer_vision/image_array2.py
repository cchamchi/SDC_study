#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:41:38 2018

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

array_2d_R=np.array([[0,0],[0,0],[0,0]],dtype=np.uint8)
array_2d_G=np.array([[0,0],[0,0],[0,0]],dtype=np.uint8)
array_2d_B=np.array([[0,0],[0,0],[0,0]],dtype=np.uint8)

array_2d_R255=np.array([[255,255],[255,255],[255,255]],dtype=np.uint8)
array_2d_G255=np.array([[255,255],[255,255],[255,255]],dtype=np.uint8)
array_2d_B255=np.array([[255,255],[255,255],[255,255]],dtype=np.uint8)

array_2d_R1=np.array([[0,255],[255,255],[255,255]],dtype=np.uint8)
array_2d_G1=np.array([[0,255],[255,255],[255,255]],dtype=np.uint8)
array_2d_B1=np.array([[0,255],[255,255],[255,255]],dtype=np.uint8)

array_2d_R6=np.array([[255,255],[255,255],[255,10]],dtype=np.uint8)
array_2d_G6=np.array([[255,255],[255,255],[255,100]],dtype=np.uint8)
array_2d_B6=np.array([[255,255],[255,255],[255,10]],dtype=np.uint8)

# axis = 2  로 하고 볼것
array_3d323 = np.zeros((3,2,3), 'uint8')
array_3d323[:,:,0]=array_2d_R6
array_3d323[:,:,1]=array_2d_G
array_3d323[:,:,2]=array_2d_B

plt.imshow(array_3d323)
plt.show()

# test.jpg 의 R,G,B 값만 그리는 필터를 만들어 보자
# 힌트 test.jpg의 R 값을 제외한 다른 slice는 0으로..


