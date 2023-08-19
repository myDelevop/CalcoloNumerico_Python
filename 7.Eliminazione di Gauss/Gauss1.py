# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:09:21 2015

@author: rocco
"""

#Eliminazione di Gauss

A = [[2,-1,2,3],[4,2,-3,1],[3,4,1,0],[-1,0,1,1]]
b = [1,-2,3,1]

n = len(A)

for j in range(n):
    for i in range(j+1,n):
        m = -A[i][j]/A[j][j]
        A[i][j] = 0 #Viene azzerato direttamente
        for k in range (j+1,n):
            A[i][k] = A[i][k] + m*A[j][k]
        b[i] = b[i] + m*b[j]

#Stampa dei Risultati:
print('\nMatrice T.Superiore:\n')
for i in range(n):
    print('  %5.2f  '*n %tuple(A[i]))
print('\n\nVettore dei termini noti:\n',b)