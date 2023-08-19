# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:40:10 2015

@author: rocco
"""

# Calcolo della precisione di macchina
A = 1
while A + 1 > 1:
    A = A / 2 # Base=2 ===> Binario
A = A*2

#Stampa in formato esponenziale
print('\nLa precisione di macchina = %e ' % A)