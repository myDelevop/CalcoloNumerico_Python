# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:20:33 2015

@author: rocco
"""

#Eliminazione di Gauss con Pivoting

A = [[1,1,-2,3],[3,2,1,0],[2,-2,1,0],[2,1,-2,3]]
b = [3,2,1,1]

n = len(A)

for j in range(n):
    
    #Individuazione riga Pivot
    Amax = abs(A[j][j])
    imax = j
    for i in range(j+1,n):
        if abs(A[i][j]) > Amax:
            Amax = abs(A[i][j])
            imax = i
            
    #Eventuale Scambio di Riga
    if imax > j:
        for k in range(j,n):
            A[j][k], A[imax][k] = A[imax][k], A[j][k]
        b[j], b[imax] = b[imax], b[j]
            
    #Eliminazione di Gauss
    for i in range(j+1,n):
        m = -A[i][j] / A[j][j]
        A[i][j] = 0
        for k in range(j+1,n):
            A[i][k] = A[i][k] + m*A[j][k]
        b[i] =  b[i] + m*b[j]
        
#Stampa dei Risultati:
print('\nMatrice T.Superiore:\n')
for i in range(n):
    print('  %5.2f  '*n %tuple(A[i]))
print('\n\nVettore dei termini noti:\n',b)