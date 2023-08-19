# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:20:05 2015

@author: rocco
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt

def diff_divise(x,y):
#grado Polinomio
    n=len(x)-1
#differenze divise
    d= np.copy(y)
    for j in range (1,n+1):
        for i in range (n,j-1,-1):
            d[i]=(d[i]-d[i-1])/(x[i]-x[i-j])
    return d

def calc_Newton(x,xn,d):
#grado del polinomio
    n=len(xn)-1
#Polinomio di Newton
    p=d[n]
    for i in range (n-1,-1,-1):
        p=d[i]+(x-xn[i])*p
    return p

def funz(x):
    y = x**5 + 5*x
    return y
    
n = 3 # Grado del pol. di interpolazione

x_nodi = np.linspace(-3,10,n+1) # n+1 nodi
y_vass = np.array([funz(xx) for xx in x_nodi])

z = diff_divise(x_nodi,y_vass) 
xp = np.linspace(-3,10,851) #Punti in cui calcolare il polinomio

# Calcolo del polinomio di interpolazione nei punti di xp
p = np.zeros(len(xp))
for i in range(len(xp)):
    check_nodi = abs(xp[i] - x_nodi) < 1.0e-14
    if True in check_nodi:
        temp = np.where(check_nodi == True)
        i_nodo = temp[0][0]
        p[i] = y_vass[i_nodo]
    else:
        p[i] = calc_Newton(xp[i],x_nodi,z)

f = funz(xp)

#GRAFICI
plt.figure(0) #Grafico polinomio interpolazione
plt.axis([-5, 12,-9000, 106990])
plt.plot(xp, p, label='p_n(x)') ;
plt.plot(xp, f, label='cos(x)') ;
plt.plot(x_nodi,y_vass, 'ro')
plt.xlabel('x', fontsize=14)
plt.legend(loc = 2)
plt.show()

plt.figure(1) #Grafico resto del pol. di interpolazione
plt.semilogy(xp,abs(p-f), label='Resto')
plt.xlabel('x', fontsize=14)
plt.legend()
#plt.show()