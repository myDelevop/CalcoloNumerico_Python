# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:00:32 2015

@author: rocco
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:43:55 2015

@author: rocco
"""

#Somma fra Matrici quadrate

A = [[1,-2,0,-1],[3,7,-2,1],[0,-1,2,-2],[-2,-3,3,7]]
B = [[-1,2,0,1],[-3,-7,2,-1],[0,1,-2,2],[2,3,-3,-7]]

n = len(A)
C = [[0 for i in range(n)]for j in range(n)]

print('\nSomma fra matrici:\n')

for i in range(n):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]
        
#Stampa della matrice
for i in range(n):
    print('  %5.2f  '*n %tuple(C[i]))