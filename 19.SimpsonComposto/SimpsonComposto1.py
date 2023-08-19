# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:13:02 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

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

# Definizione funzione da integrare
def f(x):
    y = x**3 + 3
    return y

# Definizione della primitiva
def F(x):
    y = x**4/4
    return y

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
    s=fz[0]+fz[n]
    for k in range (0,n):
        s=s+4*fzm[k]
    for k in range (1,n):
        s=s+2*fz[k]
# Visualizzazione grafica di simpson
    for i in range (0,len(z)-1):
        tempNodi=np.linspace(z[i],z[i+1],4)
        tempAsso=[f(tempNodi[m]) for m in range(0,4)]
        d=diffDiv(tempNodi,tempAsso)
        grafico=np.linspace(tempNodi[0],tempNodi[3],40)
        p = np.zeros(len(grafico))
        for k in range(len(grafico)):
            check_nodi = abs(grafico[k] - tempNodi) < 1.0e-14
            if True in check_nodi:
                temp = np.where(check_nodi == True)
                i_nodo = temp[0][0]
                p[k] = tempAsso[i_nodo]
            else:
                p[k] = calcNewton(grafico[k],tempNodi,d)
        #GRAFICO SIMPSON
        plt.plot([grafico[0],grafico[0]],[0,p[0]],'b-', linewidth=1.0)
        for q in range (0,len(grafico)-1):
            plt.plot([grafico[q],grafico[q+1]],[p[q],p[q+1]],'b-', linewidth=1.0)
        plt.plot([grafico[len(grafico)-1],grafico[len(grafico)-1]],[p[len(p)-1],0],'b-', linewidth=1.0)
        #RIEMPIMENTO GRAFICO SIMPSON
        for q in range (0,len(grafico)-1):
            plt.fill([grafico[q],grafico[q],grafico[q+1],grafico[q+1],grafico[q]],[0,p[q],p[q+1],0,0],color='y')
    s=s*h
    return s


# Integrazione mediante la formula composta del trapezio

# Definizione dell'intervallo di integrazione e numero sotto intervalli
a = -3.0 ; b = 6.0; N = 23



# Calcolo formula del trapezio
S = SimpsonComposti(f,a,b,N)

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
x = np.linspace(a-0.1,b+0.1,200)
y = [f(xx) for xx in x]
fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.plot(x,y,'k-',linewidth=1.2,label='f(x)')
stringa = 'Integrale esatto : %f ' % I
plt.text(0.1,0.3,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Integrale approx : %f ' % S
plt.text(0.1,0.2,stringa,fontsize=15,transform=ax.transAxes)
stringa = 'Errore commesso  : %e ' % Errore
plt.text(0.1,0.1,stringa,fontsize=15,transform=ax.transAxes)
plt.legend()
plt.show()