# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 20:06:25 2015

@author: rocco
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 19:52:16 2015

@author: rocco
"""

def fattLUpivot(A):
    n = len(A)
    indice = [i for i in range(n)]
    
    for j in range(n-1):
        #Individuazione riga Pivot
        Amax = abs(A[j][j])
        imax = j
        for i in range(j+1,n):
            if (abs(A[i][j]) > Amax):
                Amax = abs(A[i][j])
                imax = i
        
        #eventuale scambio di riga
        if imax > j:
            for k in range(n):
                A[j][k],A[imax][k] = A[imax][k],A[j][k]
            
            indice[j],indice[imax] = indice[imax],indice[j]
        
        #Eliminazione di Gauss
        for i in range(j+1,n):
            m = A[i][j]/A[j][j]
            A[i][j] = m
            for k in range(j+1,n):
                A[i][k] = A[i][k] - m*A[j][k]
    
    return A,indice
    
    
    
A = [[1,2,-3],[3,4,1],[2,2,1]]

LU, indice = fattLUpivot(A)

#Stampa dei risultati:
print('\n')
n = len(LU)
for i in range(n):
    print('  %7.2f  '*n %tuple(LU[i]))        
 