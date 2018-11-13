#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:05:48 2018

@author: user
"""


import matplotlib.pyplot as plt
import numpy as np
xsize=960
ysize=540

left_bottom = [100, 450]
right_bottom = [840, 450]
apex = [470, 310]


x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]

plt.plot(x, y, 'b--', lw=4)
plt.show()


fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

print fit_left
print fit_right
print fit_bottom



XX, YY = np.meshgrid(np.arange(1, xsize), np.arange(1, ysize))
'''
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
'''

region_thresholds = (YY > (XX*fit_left[0] + fit_left[1]))

#plt.imshow(canvas)
# 조건을 만족하는 부분은 true >> 흰색으로 보임

plt.imshow(region_thresholds, cmap='gray')
plt.plot(x, y, 'b--', lw=4)
plt.show()




region_thresholds = (YY > (XX*fit_right[0] + fit_right[1]))
                    
plt.imshow(region_thresholds, cmap='gray')
plt.plot(x, y, 'b--', lw=4)
plt.show()  

           

region_thresholds = (YY < (XX*fit_bottom[0] + fit_bottom[1]))
                    
plt.imshow(region_thresholds, cmap='gray')
plt.plot(x, y, 'b--', lw=4)
plt.show()  



region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))   
                    
plt.imshow(region_thresholds, cmap='gray')
plt.plot(x, y, 'b--', lw=4)
plt.show()                      