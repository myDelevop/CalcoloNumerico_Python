# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:52:54 2015

@author: rocco
"""

#Prodotto fra 2 matrici quadrate

A = [[3,3,-3],[-2,-2,3],[-4,-6,7]]
B = [[2/3,-1/2,1/2],[1/3,3/2,-1/2],[2/3,1,0]]

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