# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 18:31:20 2015

@author: rocco
"""

import numpy as np
import matplotlib.pyplot as plt

# Dimensione del sistema
err_norm = [0]*40
err_stim = [0]*40
for n in range(1,40):

    # Costruzione della matrice di Vandermonde
    A = [[ i**j for j in range(n)] for i in range(n)]

    # Costruzione di un problema test
    xsol = [1 for i in range(n)]
    b = np.dot(A,xsol)

    # Risoluzione del sistema lineare
    x = np.linalg.solve(A,b)
    err = x - xsol
    err_norm[n] = np.linalg.norm(err)
    err_stim[n] = np.linalg.cond(A)*np.finfo(float).eps

# Visualizzazione dei risultati
print('\n\n')
plt.semilogy(range(40),err_norm, label='Errore')
plt.semilogy(range(40),err_stim, label='Stima')
plt.xlabel('n', fontsize=14)
plt.title('Malcondizionamento matrice di Vandermonde')
plt.legend(loc=4)
plt.show()