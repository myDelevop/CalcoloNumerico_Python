# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:38:05 2015

@author: rocco
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi)

plt.figure(1)
plt.subplot(121)

plt.plot(x,np.sin(x))
plt.subplot(122)

plt.plot(x,np.cos(x))
plt.show()

plt.figure(2)
plt.subplot(221)

plt.plot(x,np.sin(x)-np.cos(x))
plt.subplot(222)

plt.plot(x,np.cos(x)+3*np.cos(x))
plt.subplot(223)

plt.plot(x,2*np.sin(x)+np.cos(x))
plt.subplot(224)

plt.plot(x,np.cos(x)-3*np.cos(x))

plt.show()