# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:17:53 2015
@author: rocco
"""
#Metodo di Sostituzione in Avanti (Triangolare Inferiore)

L = [[2,0,0],[1,2,0],[1,-2,3]]
b = [1,2,-1]

n = len(L)
x = [0]*n
 
for i in range(n):
    S = 0
    for j in range(i):
        S = S + L[i][j]*x[j]
    
    x[i] = (b[i]-S) / L[i][i]

#Stampa delle Incognite:

print('\nVettore delle Soluzioni:\n')
print(x)