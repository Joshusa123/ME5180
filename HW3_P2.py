#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
from scipy.optimize import fsolve
from numpy import sin,cos,pi
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Target angle - Theta 1
a1 = 180*(pi/180)

#Length Constants
l1 = 0.5
l2 = 1
l3 = 1

#Fixed-Pin Location
dy = -0.5
dx = 1

#Use Fsolve to determine theta2 and theta3
Fbar = lambda a: np.array([l1*sin(a1)+l2*sin(a[0])-l3*sin(a[1])-dy,
                           l1*cos(a1)+l2*cos(a[0])-l3*cos(a[1])-dx])

a0 = [0,pi/2]
a_sol = fsolve(Fbar, a0)

a2 = a_sol[0];
a3 = a_sol[1];

print("\nTheta1 = "+str(a1*180/pi)+"\nTheta2 = "+str(a2*180/pi)+"\nTheta3 = "+str(a3*180/pi)+"\n")

rx = np.array([0, l1*cos(a1), l1*cos(a1)+l2*cos(a2), l1*cos(a1)+l2*cos(a2)-l3*cos(a3)])
ry = np.array([0, l1*sin(a1), l1*sin(a1)+l2*sin(a2), l1*sin(a1)+l2*sin(a2)-l3*sin(a3)])

plt.plot(rx,ry,'o-')
plt.axis([-0.75, 1.5, -0.6, 0.6])


# In[ ]:




