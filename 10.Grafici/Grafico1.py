# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:02:49 2015

@author: rocco
"""
#Grafico funzione coseno 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi)
y = np.cos(x)

plt.plot(x,y)
plt.show()

