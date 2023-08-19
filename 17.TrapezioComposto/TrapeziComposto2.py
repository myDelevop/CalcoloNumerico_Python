# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:44:10 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Definizione funzione da integrare
def f(x):
    y = 1/x
    return y

# Definizione della primitiva
def F(x):
    y = log(abs(x))
    return y

# Calcolo formula trapezi composti
def TrapeziComposti(f,a,b,N):

    # Calcolo estremi sotto intervalli
    z = np.linspace(a,b,N+1)
    fz = [f(zz) for zz in z]

    # Calcolo della formula di quadratura
    S = 0
    for i in range(1,N):
        S = S + fz[i] ;
    T = (fz[0] + 2*S + fz[N])*(b-a)/2/N

    # Visualizzazione grafica dei trapezi
    for i in range(0,N):
        plt.plot([z[i],z[i],z[i+1],z[i+1],z[i]],
                 [0,fz[i],fz[i+1],0,0], 'b-', linewidth=1.2)
        plt.fill([z[i],z[i],z[i+1],z[i+1],z[i]],
                 [0,fz[i],fz[i+1],0,0], color = 'y')

    # Output del risultato
    return T



# Integrazione mediante la formula composta del trapezio

# Definizione dell'intervallo di integrazione e numero sotto intervalli
a = 1 ; b = 3
N = 18 

# Calcolo formula del trapezio
T = TrapeziComposti(f,a,b,N)

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
stringa = 'Integrale esatto : %f ' % I
plt.text(0.1,0.3,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Integrale approx : %f ' % T
plt.text(0.1,0.2,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Errore commesso  : %e ' % Errore
plt.text(0.1,0.1,stringa,fontsize=15,transform=ax.transAxes)
plt.legend()
plt.show()
