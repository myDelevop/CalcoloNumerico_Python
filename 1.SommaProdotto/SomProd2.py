# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:56:19 2015

@author: rocco
"""
a = 0.09375 #Numero Macchina (b=2)
b = 100000

#Calcolo Mediante Prodotto
P = a*b

#Calcolo Mediante Somme
S = 0
for i in range(b):
    S = S + a

#Calcolo Errore Relativo
Err = abs(P-S) / abs(P) 

#Visualizzazione di Risultati:
print('\nMOLTIPLICAZIONE TRA ',a,'e',b)
print('\nValore calcolato mediante Prodotto:  %.13f' % P)
print('Valore calcolate mediante Somme:     %.13f' % S)
print('Errore Relativo:                     %e \n\n' % Err)
print('\nIn questo caso l\'errore e\'nullo poichè',a,'e un numero macchina\n')