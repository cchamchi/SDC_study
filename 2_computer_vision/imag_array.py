#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:14:39 2018

@author: user
"""

import numpy as np

# array

# 1d array

array_1d=np.array([1,2,3,4,5])
array_1d_uint8=np.array([1,2,3,4,5],dtype=np.uint8)
print array_1d.shape

array_1d_uint8_ov=np.array([1,2,3,256,257],dtype=np.uint8)
array_1d_uint8_un=np.array([-2,-1,0,4,5],dtype=np.uint8)


# 2d array(row,col)

array_2d32=np.array([[1,2],[3,4],[5,6]],dtype=np.uint8)
print array_2d32.shape

array_2d23=np.array([[1,2,3],[4,5,6]],dtype=np.uint8)
print array_2d23.shape

# 3d array (row,col,slice)

# 3 slice of 2d array

array_2d_R=np.array([[1,2],[3,4],[5,6]],dtype=np.uint8)
array_2d_G=np.array([[7,8],[9,10],[11,12]],dtype=np.uint8)
array_2d_B=np.array([[13,14],[15,16],[17,18]],dtype=np.uint8)

array_3d332=np.array([array_2d_R,array_2d_G,array_2d_B],dtype=np.uint8)
print array_3d332.shape


# axis = 2  로 하고 볼것
array_3d323 = np.zeros((3,2,3), 'uint8')
array_3d323[:,:,0]=array_2d_R
array_3d323[:,:,1]=array_2d_G
array_3d323[:,:,2]=array_2d_B


##################### slicing ##########################

s_1d_2=array_1d[1]
s_2d_row2=array_2d32[1,:]
s_2d_col2=array_2d32[:,1]
s_3d_slice2=array_3d332[1,:,:]

s_3d_add=array_3d332[0,:,:] + array_3d332[1,:,:]+ array_3d332[2,:,:]
