# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:43:55 2015

@author: rocco
"""

#Somma fra Matrici quadrate

A = [[1,-2,3],[3,2,0],[0,2,-1]]
B = [[0,0,2],[1,1,-2],[2,2,-3]]

n = len(A)
C = [[0 for i in range(n)]for j in range(n)]

print('Somma fra matrici:\n')

for i in range(n):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]
        

print('\n')
for i in range(n):
    print('  %5.2f  '*n %tuple(C[i]))