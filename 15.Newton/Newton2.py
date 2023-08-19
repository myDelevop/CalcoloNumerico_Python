# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:39:50 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

print('\n')

def Newton(f,df,x0,tol,itmax):

    # Inizializzazione del processo di calcolo
    fx0 = f(x0)
    dfx0 = df(x0) 
    it = 0 ; stop = False
    plt.plot(x0,0,'r+')
    
    # Ciclo di calcolo del metodo di newton
    while not(stop) and it < itmax:

        x1 = x0 - fx0/dfx0
        fx1 = f(x1)

        # Grafico della tangente in x0
        plt.plot(x0,fx0,'r.') 
        plt.plot(np.array([x0,x0]),np.array([0,fx0]), 'k:', linewidth=0.4 ) 
        plt.plot(np.array([x0,x1]),np.array([fx0,0]), 'k-', linewidth=0.4)
        plt.plot(x1,0,'r+')

        stop = (abs(x1-x0) < tol) and abs(fx1) < tol
        it = it + 1

        if not(stop):
            x0 = x1 ; fx0 = fx1 ; dfx0 = df(x0)

    # Verifica avvenuta convergenza
    if not(stop):
        print('Metodo di Newton non converge in %d iterazione alla precisione %e' % (it,tol))


    # Output del risultato
    return x1

# ====================================================
def f1(x):
    y = cos(x)+2*sin(x)
    return y

# ====================================================
def df1(x):
    y = -sin(x)+2*cos(x)    
    return y

# ====================================================
x_array = np.linspace(-0.5,4.5)
y_array = np.array([f1(x) for x in x_array])

# Grafico della funzione
fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([1.88,3,-3,3])
plt.plot(x_array, y_array, 'b-', linewidth=1 )

# Disegno assi cartesiani
left,right = ax.get_xlim()
low,high = ax.get_ylim()
plt.arrow( left, 0, right-left, 0,
           length_includes_head = True,
           head_width=(high-low)/60, head_length=(right-left)/40, fc='k' )
plt.arrow( 0, low, 0, high-low,
           length_includes_head = True,
           head_width=(right-left)/60, head_length=(high-low)/40, fc='k' ) 

# Calcolo della radice
z = Newton(f1,df1,2,1.0e-6,130)
print('Lo zero della funzione è : %f ' % z) 

plt.show()