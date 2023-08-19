# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:42:37 2015

@author: rocco
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Definizione funzione da integrare
def f(x):
    y = x**3 + 2*x**2 + 4*x + 5
    return y

# Definizione della primitiva
def F(x):
    y = 1/4*x**4 + 2/3*x**3 + 2*x**2 + 5*x
    return y


# Integrazione di una funzione mediante la formula del trapezio

# Definizione dell'intervallo di integrazione
a = 1;
b = 2;

# Calcolo formula del trapezio
fa = f(a); 
fb = f(b)

T = (fa + fb)*(b-a)/2

# Calcolo integrale mediante primitiva
Fa = F(a) ; Fb = F(b)
I = Fb - Fa

# Calcolo dell'errore
Errore = abs(I-T)

# Visualizzazione dei risultati
print('\n\nIntervallo [%f %f] ' % (a,b))
print('Integrale esatto : %f ' % I)
print('Integrale approx : %f ' % T)
print('Errore commesso  : %e\n ' % Errore)

# Visualizzazione grafica dei risultati
x = np.linspace(a-0.1,b+0.1,100)
y = [f(xx) for xx in x]
fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.plot(x,y,'k-',linewidth=1.2,label='f(x)')
plt.plot([a,a,b,b,a],[0,fa,fb,0,0],'b-', linewidth=1.0)
plt.fill([a,a,b,b,a],[0,fa,fb,0,0],color='y')
stringa = 'Integrale esatto : %f ' % I
plt.text(0.1,0.3,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Integrale approx : %f ' % T
plt.text(0.1,0.2,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Errore commesso  : %e ' % Errore
plt.text(0.1,0.1,stringa,fontsize=15,transform=ax.transAxes)
plt.legend(loc=2)
plt.show()