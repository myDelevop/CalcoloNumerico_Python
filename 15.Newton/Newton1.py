# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:39:04 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

def Newton(f,df,x0,tol,itmax):

    # Inizializzazione del processo di calcolo
    fx0 = f(x0)
    dfx0 = df(x0) 
    it = 0 ; stop = False

    print(' n         xn            f(xn)           f\'(xn)           xn1') 
    
    # Ciclo di calcolo del metodo di newton
    while not(stop) and it < itmax:

        x1 = x0 - fx0/dfx0
        fx1 = f(x1)

        stop = abs(x1-x0) < tol and abs(fx1) < tol
        it = it + 1

        print('%2d : %12.9f  %15.7e  %15.7e  %12.9f' % (it,x0,fx0,dfx0,x1)) 
        if not(stop):
            x0 = x1 ; fx0 = fx1 ; dfx0 = df(x0)

    # Verifica avvenuta convergenza
    if not(stop):
        print('Metodo di Newton non converge in %d iterazione alla precisione %e' % (it,tol))


    # Output del risultato
    return x1

# ====================================================
def f(x):
    y = x**7 - 3*x**6 + 5*x -3
    return y

# ====================================================
def df(x):
    y = 7*x**6 - 18*x**5 + 5
    return y


# Calcolo della radice
z = Newton(f,df,0,1.0e-8,30)
print('Lo zero della funzione è : %18.16f ' % z) 