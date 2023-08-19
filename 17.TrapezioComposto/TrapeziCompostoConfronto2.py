# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 09:11:05 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Formula dei trapezi composti
def TrapeziComposti(f,a,b,N):

    # Calcolo estremi sotto intervallo e valori della funzione
    z = np.linspace(a,b,N+1) 
    fz = [f(zz) for zz in z]

    # Calcolo formula di quadratura composta
    T = fz[0] + fz[N] 
    for k in range(1,N):
        T = T + 2*fz[k] 
    T = T * (b-a)/N/2 ;

    # Output del risultato
    return T

# Definizione funzione da integrare
def f(x):
    y = 1/x
    return y

# Definizione primitiva della funzione da integrare
def F(x):
    y = log(abs(x))
    return y


# ========================================================
# Confronto formula dei trapezi al variare di N

# Definizione intervallo di integrazione 
a = 2 ; b = 5 ;

# Numero massimo di sotto intervalli
Nmax = 45 

# Calcolo del valore teorico dell'integrale
Fa = F(a) ;
Fb = F(b) ;
I = Fb - Fa ;
print('\n\nValore esatto dell\'integrale : %f\n' % I)

# Calcolo del valore numerico ed errore al variare di N
Errore = np.zeros(Nmax+1)
for N in range(1,Nmax+1):
    T = TrapeziComposti(f,a,b,N)
    Errore[N] = abs(I-T)
    print('N=%2d  T=%f  Errore=%e' % (N,T,Errore[N]))

# Visualizzazione grafica dei risultati
plt.plot(np.array(range(1,N+1)),Errore[1:], 'r+', linewidth=1.2, label='Errore')
plt.yscale('log')
plt.xlabel('N', fontsize=14)
plt.legend()
plt.show()
