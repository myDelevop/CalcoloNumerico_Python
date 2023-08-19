# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:42:17 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Formula dei trapezi composti
def calcNewton(x,xn,d):
#grado del polinomio
    n=len(xn)-1
#Polinomio di Newton
    p=d[n]
    for i in range (n-1,-1,-1):
        p=d[i]+(x-xn[i])*p
    return p

def diffDiv(x,y):
#grado Polinomio
    n=len(x)-1
#differenze divise
    d= np.copy(y)
    for j in range (1,n+1):
        for i in range (n,j-1,-1):
            d[i]=(d[i]-d[i-1])/(x[i]-x[i-j])
    return d

# Calcolo formula trapezi composti
def SimpsonComposti(f,a,b,n):
    h=(b-a)/(6*n)
    # Calcolo estremi sotto intervalli
    z = np.linspace(a,b,n+1)
    fz = [f(zz) for zz in z]

    x=z[0:-1]
    y=z[1:]
    zm=(x+y)/2
    fzm=[f(zz) for zz in zm]
    S=fz[0]+fz[n]
    for k in range (0,n):
        S=S+4*fzm[k]
    for k in range (1,n):
        S=S+2*fz[k]
    S=S*h
    return S


# ========================================================
# Confronto formula dei trapezi al variare di N


def f(x):
    y = 1/x
    return y

def F(x):
    y = log(abs(x))
    return y
# Definizione intervallo di integrazione 
a = 1.001 ; b = 4.7 ;

# Numero massimo di sotto intervalli
Nmax = 30 

# Calcolo del valore teorico dell'integrale
Fa = F(a) ;
Fb = F(b) ;
I = Fb - Fa ;
print('\n\nValore esatto dell\'integrale : %f\n' % I)

# Calcolo del valore numerico ed errore al variare di N
Errore = np.zeros(Nmax+1)
for N in range(1,Nmax+1):
    S = SimpsonComposti(f,a,b,N)
    Errore[N] = abs(I-S)
    print('N=%2d  T=%f  Errore=%e' % (N,S,Errore[N]))

# Visualizzazione grafica dei risultati
plt.plot(np.array(range(1,N+1)),Errore[1:], 'r+', linewidth=1.2, label='Errore')
plt.yscale('log')
plt.xlabel('N', fontsize=14)
plt.legend()
plt.show()