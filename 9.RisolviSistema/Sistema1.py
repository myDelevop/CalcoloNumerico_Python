# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:39:25 2015

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
    
    
#Programma Principale:

A = [[2, 1, 0], [2, 3, -1], [3, 3, -2]]
b = [-3, 4, -6]

U, c = eliminazioneGaussPivot(A,b)
x = SostituzioneIndietro(U,c)

#Stampa dei risultati
print('\nVettore delle incognite:\n')
print(x) 