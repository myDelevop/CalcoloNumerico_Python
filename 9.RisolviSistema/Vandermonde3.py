# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:26:07 2015

@author: rocco
"""

import numpy as np

print('\n')

# Dimensione del sistema
for n in range(1,20):

    # Costruzione della matrice di Vandermonde
    A = [[ i**j for j in range(n)] for i in range(n)]

    # Costruzione di un problema test
    xsol = [1 for i in range(n)]
    b = np.dot(A,xsol)

    # Risoluzione del sistema lineare
    x = np.linalg.solve(A,b)
    err = x - xsol
    err_norm = np.linalg.norm(err)

    # Visualizzazione dei risultati
    print('n = %2d  ||err||=%e' % (n,err_norm))
    
print('\n')