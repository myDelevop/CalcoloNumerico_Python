# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 17:48:10 2015

@author: rocco
"""

#Metodo eliminazione Gauss e Pivot
def eliminazioneGaussPivot(A,b):
    
    n = len(A)
    for j in range(n):
        
        #Individuazione riga Pivot
        Amax = abs(A[j][j])
        imax = j
        for i in range(j+1,n):
            if abs(A[i][j] > Amax):
                Amax = abs(A[i][j])
                imax = i
                
        #Eventuale Scambio riga
        if imax > j:
            for k in range(j,n):
                A[j][k], A[imax][k] = A[imax][k], A[j][k]
            b[j], b[imax] = b[imax], b[j]
            
        #Eliminazione di Gauss
        for i in range(j+1,n):
            m = -A[i][j] / A[j][j]
            A[i][j] = 0
            for k in range (j+1,n):
                A[i][k] = A[i][k] + m*A[j][k]
            b[i] = b[i] + m*b[j]
    
    #Output (T.Superiore + vett)
    return A,b
    
    
#Algoritmo Sostituzione Indietro
def SostituzioneIndietro(U,b):
    
    n = len(U)
    x = [0]*n
    
    for i in range(n-1,-1,-1):
        S = 0
        for j in range(i+1,n):
            S = S + U[i][j]*x[j]            
        x[i] = (b[i] - S) / U[i][i]
    
    #Output Soluzioni
    return x


# Risoluzione di un sistema
A = [[-3, 2, 1], [1, 0, -1], [4, -2, 2]]

# Costruzione del problema test
n = len(A)
xsol = [1]*n
b = [0]*n
for i in range(n):
    for j in range(n):
        b[i] = b[i] + A[i][j]*xsol[j]

# Stampa della matrice dei coefficienti
print('\n\nMatrice dei coefficienti')
str_fmt = '| '+('%6.3f '*n) +' |'
for i in range(n):
    print(str_fmt % tuple(A[i]))

# Stampa vettore dei termini noti
print('\nVettore dei termini noti')
for i in range(n):
    print('| %6.3f |' % b[i])

U, c = eliminazioneGaussPivot(A,b)
x = SostituzioneIndietro(U,c)

# Stampa soluzione attesa
print('\nSoluzione attesa, calcolata e differenza')
str_fmt = '| %6.3f |  | %6.3f |   | %e | '
for i in range(n):
    print(str_fmt % (xsol[i],x[i],abs(xsol[i]-x[i])))
print('\n')