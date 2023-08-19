# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:08:30 2015

@author: rocco
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:06:05 2015

@author: rocco
"""
  
#Prodotto fra 2 matrici quadrate

A = [[1,2,-3],[-2,0,3],[-4,2,3]]
B = [[1,1,0],[3,3,4],[8,2,1]]

n = len(A)
C= [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        S = 0
        for k in range(n):
            S = S + A[i][k]*B[k][j]
            
        C[i][j] = S

#Stampa
print('\nProdotto fra matrici:\n')

for i in range(n):
    print('  %7.2f  '*n %tuple(C[i]))        