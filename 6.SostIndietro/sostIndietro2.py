# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:14:55 2015

@author: rocco
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:47:14 2015

@author: rocco
"""

#Metodo di Sostituzione Indietro (Triangolare Superiore)

U = [[1,2,2,1],[0,1,2,3],[0,0,3,-2],[0,0,0,1]]
b = [2,1,2,-1]

n = len(U)
x = [0]*n

for i in range(n-1,-1,-1):
    S = 0
    for j in range(i+1,n):
        S = S + U[i][j]*x[j]
    x[i] = (b[i] - S) /U[i][i]
    
#Stampa delle incognite:
print('\nVettore delle Soluzioni:\n')
print(x)