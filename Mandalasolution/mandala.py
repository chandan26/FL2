#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def mandalapolygon(num, radi, angleinit=0, **kwargs):   #function to plot polygon as required to generate any plot
    ax.plot(np.linspace(angleinit, angleinit + 3 * np.pi, (num + 2)), np.full(num + 2, radi), **kwargs)
    

fig = plt.figure()
ax = fig.add_subplot(111, polar=True) # Affirming polar plot for the outer circle


#ploting circles  of diffrernt radius
ax.plot(np.linspace(0, 5 * np.pi, 400), np.ones(400) * 5, color='r', linestyle='-')
ax.plot(np.linspace(0, 4 * np.pi, 300), np.ones(300) * 6, color='b', linestyle='-.')
ax.plot(np.linspace(0, 3 * np.pi, 200), np.ones(200) * 4, color='g', linestyle='-')
ax.plot(np.linspace(0, 2* np.pi, 100), np.ones(100) * 3, color='y', linestyle='-')

mandalapolygon(num=8, radi=5, color='g', linestyle='-')
ax.set_yticklabels([])
ax.set_xticklabels([])
mandalapolygon(num=5, radi=3, color='g', linestyle='-') #plotting polygons
mandalapolygon(num=4, radi=4, angleinit=np.pi, color='g', linestyle='-')
mandalapolygon(num=5, radi=5, angleinit=np.pi*2, color='r', linestyle='-.')
mandalapolygon(num=6,radi=6, angleinit=np.pi*4, color='b', linestyle='-')
mandalapolygon(num=7, radi=7, angleinit=np.pi*6, color='g', linestyle='-.')
mandalapolygon(num=8, radi=8, angleinit=np.pi*6, color='r', linestyle='-')
mandalapolygon(num=9,radi=8, angleinit=np.pi*6, color='b', linestyle='-.')
mandalapolygon(num=10,radi=9,angleinit=np.pi*6, color='r', linestyle='--')
plt.savefig('mandala.png')
plt.show()


# In[ ]:




