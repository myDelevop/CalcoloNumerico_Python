# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:34:49 2015

@author: rocco
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

print('\n\n')
def Bisezioni(f,a,b,tol):

    # Verifica ordine degli estremi
    if a > b:
        a, b = b, a

    # Grafico della funzione
    x_array = np.linspace(a,b)
    y_array = np.array([f(x) for x in x_array])
    plt.plot(x_array,y_array,'b-') 
    plt.axis([2.46,3.92,-0.26,0.18])

    
    # Verifica sul cambio di segno di f(x) in [a,b]
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print("Errore: la funzione non cambia segno nell'intervallo!")
        return
    
    # Calcolo del numero di iterazioni necessarie
    n = ceil((log(b-a) - log(tol))/log(2))

    for i in range(n+1):
        c = (a+b)/2
        fc = f(c)
        print('%2d [%f,%f] -> c=%f f(c)=%e' % (i,a,b,c,fc))
        if fa*fc < 0:
            b = c ; fb = fc ;
        else:
            a = c ; fa = fc ;
        plt.plot(c,0,'r+')
        stringa = '$c_{%d}$' % i 
        plt.text(c,-0.2,stringa,fontsize=15)

    plt.show()
    
    # Output del risultato
    return c

def Funzione(x):
    y = tan(x) * 3*x*x
    return y 

z = Bisezioni(Funzione,0,5,1.0e-18)

print("La radice trovata e': %15.12f" % z)