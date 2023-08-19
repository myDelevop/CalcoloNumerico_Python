# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:20:46 2015

@author: rocco
"""

a = 0.2 #Non appartiene a F
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
print('L\'Errore non esce nullo come ci si aspettava,poichè',a,'non e')
print('un numero macchina.')