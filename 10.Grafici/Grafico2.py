
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:02:49 2015

@author: rocco
"""
#Grafico funzione coseno 

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #Inserire La funzione cui si vuole visualizzare il grafico
  # y = ...?
    y = x*x
    return y
    
#Intervallo ascisse
x = np.linspace(-20,20)
y = f(x)

plt.plot(x,y,'r--')  # Rosso tratteggiato
#plt.plot(x,y,'ro')  # Puntini rossi ad ogni punto

plt.show()

