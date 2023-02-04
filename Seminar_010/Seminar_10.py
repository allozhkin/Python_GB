#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


def func(a,b,c,x):
    return a*x**2+b*x+c


# In[3]:


a,b,c = 5, 10, -30


# In[4]:


x = np.arange(-10, 10, 0.01)


# In[5]:


def find_sqrt(a, b, c):
    d = b**2-4*a*c
    if d < 0:
       return ('Корней нет',)
    elif d == 0:
        x = -b / (2 * a)
        return (round(x,2),)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (round(x1,2), round(x2,2))


# In[6]:


sqrts = find_sqrt(a,b,c)


# In[7]:


min_y = min(func(a,b,c,x))


# In[8]:


c2 = c - min_y
min_x = find_sqrt(a,b,c2)
min_x = min_x[0]


# In[9]:


pos_down = np.arange(-10, sqrts[1], 0.01)
neg_down = np.arange(sqrts[1],min_x , 0.01)
neg_up = np.arange(min_x, sqrts[0], 0.01)
pos_up = np.arange(sqrts[0],10 , 0.01)


# In[10]:


# plt.plot(x, func(5, 10, -30, x), 'r-')
# корни
plt.plot(sqrts[0],0,'go', label = f'Корни: ({sqrts[0]},{sqrts[1]})')
plt.plot(sqrts[1],0,'go')
# вершина
plt.plot(min_x, min_y, 'rx', label = f'Вершина ({min_x}, {min_y})')
# pos_down
plt.rcParams['lines.linestyle'] = '-'
plt.plot(pos_down, func(a,b,c,pos_down), 'b', label = 'убывает > 0')
# neg_down
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(neg_down, func(a,b,c,neg_down), 'b', label = 'убывает < 0')
# neg_up
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(neg_up, func(a,b,c,neg_up), 'y', label = 'Возрастает < 0')
# pos_up
plt.rcParams['lines.linestyle'] = '-'
plt.plot(pos_up, func(a,b,c,pos_up), 'y', label = 'Возрастает > 0')
plt.legend()
plt.grid()

