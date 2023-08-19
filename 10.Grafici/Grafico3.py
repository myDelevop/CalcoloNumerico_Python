# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:04:24 2015

@author: rocco
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi)

#imposta intervallo ascissa e ordinata grafico:
plt.axis([-3, 3, -2, 2]) 

y1 = np.cos(x)
y2 = np.sin(x) 

# Visualizzazione di 2 funzioni sovrapposte.
plt.plot(x,y1,  'k:', label = 'cos(x')
plt.plot(x,y2, 'r--', label = 'sin(x)') 

plt.xlabel('x', fontsize=18) 
plt.ylabel('f(x)', fontsize=18) 

plt.legend(loc=4)
plt.grid(True) #Griglia tratteggiata

plt.title('Grafico di funzione') 
plt.suptitle('Programma di prova') 

plt.show()