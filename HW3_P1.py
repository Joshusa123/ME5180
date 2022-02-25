#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

g = 9.81
L = 1
a = 0.9
rho = 5
F = lambda c: L-(2*c)/rho/g*np.sinh(rho*g*a/(2*c))
c = np.linspace(10,50)
plt.plot(c,F(c), label='f(c)')
plt.plot(c,np.zeros(c.shape), label='f(c)=0')
plt.legend()
plt.xlabel('c')
plt.ylabel('f(c)')


# In[77]:


f = lambda c: L-(2*c)/rho/g*np.sinh(rho*g*a/(2*c))
from scipy.optimize import fsolve
c0 = 30
c_sol = fsolve(f, c0)

print('c_sol = {} and f(c_sol) = {}'.format(c_sol[0], f(c_sol)))


# In[78]:


x = np.linspace(-a/2,a/2)
lam = c_sol[0]*np.cosh((g*rho*a)/(2*c_sol[0]))

y = (c_sol[0]/(rho*g))*(np.cosh(rho*g*x/c_sol[0])-lam/c_sol[0])

plt.plot(x,y,label=r'a = 0.9')
plt.xlabel('x-axis (m)')
plt.ylabel('y(x) - chain location (m)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# In[ ]:





# In[ ]:




