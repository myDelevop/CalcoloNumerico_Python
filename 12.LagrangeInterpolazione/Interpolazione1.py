# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:25:54 2015

@author: rocco
"""

import numpy as np
import matplotlib.pyplot as plt

# Calcolo coefficienti formula di Lagrange Baricentrica
def Z_Coeff(x,y):
    
    n = len(x)
    #Calcolo differenze xj-xk
    X = np.zeros((n,n))
    for j in range(n):
        for k in range(0,j):
            X[j][k] = -X[k][j]
        for k in range(j+1,n):
            X[j][k] = x[j] - x[k]
    
    #Calcolo coeffecienti zj    
    z = np.zeros(n)
    for j in range(n):
        p = 1
        for k in range(n):
            if (k != j):
                p = p*X[j][k]        
        z[j] = y[j] / p    
    #Output
    return z

# Calcolo polinomio di interpolazione in un punto
def Calc_Lagrange(x,z,xp):
   
    n = len(x)
    #Calcolo valori xp-xj
    xxj = np.zeros(n)
    for j in range(n):
        xxj[j] = xp - x[j]
    #Calcolo Pin
    pin = 1
    for j in range(n):
        pin = pin * xxj[j]
    
    #Calcolo polinomio interpolazione
    p = 0
    for j in range(n):
        p = p+z[j]/xxj[j]  
    p = p*pin
    
    #Output
    return p
    
n = 2 # Grado del pol. di interpolazione

x_nodi = np.linspace(-np.pi,np.pi,n+1) # n+1 nodi
y_vass = np.cos(x_nodi)           # n+1 valori associati

z = Z_Coeff(x_nodi,y_vass) 
xp = np.linspace(-np.pi,np.pi,851) #Punti in cui calcolare il polinomio

# Calcolo del polinomio di interpolazione nei punti di xp
p = np.zeros(len(xp))
for i in range(len(xp)):
    check_nodi = abs(xp[i] - x_nodi) < 1.0e-14
    if True in check_nodi:
        temp = np.where(check_nodi == True)
        i_nodo = temp[0][0]
        p[i] = y_vass[i_nodo]
    else:
        p[i] = Calc_Lagrange(x_nodi,z,xp[i])

f = np.cos(xp) # Valori della funzione

#GRAFICI

plt.figure(0) #Grafico polinomio interpolazione
plt.axis([-4, 4, -1.2, 1.2])
plt.plot(xp, p, label='p_n(x)') ;
plt.plot(xp, f, label='cos(x)') ;
plt.plot(x_nodi,y_vass, 'ro')
plt.xlabel('x', fontsize=14)
plt.legend()
plt.show()

plt.figure(1) #Grafico resto del pol. di interpolazione
plt.semilogy(xp,abs(p-f), label='Resto')
plt.xlabel('x', fontsize=14)
plt.legend()
plt.show()