# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 20:20:14 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt


def diffDiv(x,y):
#grado Polinomio
    n=len(x)-1
#differenze divise
    d= np.copy(y)
    for j in range (1,n+1):
        for i in range (n,j-1,-1):
            d[i]=(d[i]-d[i-1])/(x[i]-x[i-j])
    return d


def calcNewton(x,xn,d):
#grado del polinomio
    n=len(xn)-1
#Polinomio di Newton
    p=d[n]
    for i in range (n-1,-1,-1):
        p=d[i]+(x-xn[i])*p
    return p


# Definizione funzione da integrare
def f(x):
    y = 7*x + 2
    return y

# Definizione della primitiva
def F(x):
    y = 7/2*x**2 + 2*x
    return y


# Integrazione di una funzione mediante la formula di Simpson
# Definizione dell'intervallo di integrazione
a = -2.0 ; b = 3.0;

# Calcolo formula di Simpson
c=(b+a)/2
fa = f(a) ; fb = f(b);fc=f(c)
S = (fa + fb + (4*fc))*((b-a)/6)


#CALCOLO FUNZIONE DI SIMPSON TRAMITE NEWTON
simpsonx = np.linspace(a,b,4)
simpsony = [f(simpsonx[i]) for i in range (0,4)]
differenze = diffDiv(simpsonx,simpsony)
r = np.linspace(a,b,100)
g = np.zeros(len(r))
for i in range(len(r)):
    check_nodi = abs(r[i] - simpsonx) < 1.0e-14
    if True in check_nodi:
        temp = np.where(check_nodi == True)
        i_nodo = temp[0][0]
        g[i] = simpsony[i_nodo]
    else:
        g[i] = calcNewton(r[i],simpsonx,differenze)




# Calcolo integrale mediante primitiva
Fa = F(a) ; Fb = F(b)
I = Fb - Fa

# Calcolo dell'errore
Errore = abs(I-S)

# Visualizzazione dei risultati
print('\n\nIntervallo [%f %f] ' % (a,b))
print('Integrale esatto : %f ' % I)
print('Integrale approx : %f ' % S)
print('Errore commesso  : %e\n ' % Errore)

# Visualizzazione grafica dei risultati
x = np.linspace(a-0.1,b+0.1,100)
y = [f(xx) for xx in x]
fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.plot(x,y,'k-',linewidth=1.2,label='f(x)')
#GRAFICO SIMPSON
plt.plot([r[0],r[0]],[0,g[0]],'b-', linewidth=1.0)
for i in range (0,len(r)-1):
    plt.plot([r[i],r[i+1]],[g[i],g[i+1]],'b-', linewidth=1.0)
plt.plot([r[len(r)-1],r[len(r)-1]],[g[len(g)-1],0],'b-', linewidth=1.0)
#RIEMPIMENTO GRAFICO SIMPSON
for i in range (0,len(r)-1):
    plt.fill([r[i],r[i],r[i+1],r[i+1],r[i]],[0,g[i],g[i+1],0,0],color='y')
#plt.fill([a,a,b,b,a],[0,fa,fb,0,0],color='y')
stringa = 'Integrale esatto : %f ' % I
plt.text(0.1,0.3,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Integrale approx : %f ' % S
plt.text(0.1,0.2,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Errore commesso  : %e ' % Errore
plt.text(0.1,0.1,stringa,fontsize=15,transform=ax.transAxes)
plt.legend(loc=2)
plt.show()