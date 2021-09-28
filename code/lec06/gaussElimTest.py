"""
gaussElimTest.py

Script to illustrate use of gauss_elimination

Solves a 4x4 example system A x = b first using Gaussian Elimination
and solving the resulting upper triangular system.

"""
# Python modules
import sys

import numpy as np

# comp2421 modules
sys.path.append("..")
from matrixSolve import *

# Example 4x4 matrix to invert
A = np.array([[4, 3, 2, 1], [1, 2, 2, 2], [1, 1, 3, 0], [2, 1, 2, 3]])

# Example column 4-vector for the right hand side.
b = np.array([[10, 7, 5, 8]])
b = np.transpose(b)

# Print arrays
print(A)
print(b)

# Reduce A x = b to upper triangular form and print result
A, b = gauss_elimination(A, b)
print(A)
print(b)

# Solve the resulting upper triangular system A x = b and print result
x = upper_triangular_solve(A, b)
print(x)
