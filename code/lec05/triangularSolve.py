"""
triangularSolve.py

Script that illustrates use of lower_triangular_solve and
upper_triangular_solve.  

"""

# Python modules
import sys

import numpy as np

# comp2421 modules
sys.path.append("..")
from matrixSolve import *

# Lower triangular solve
L = np.array([[2, 0, 0, 0], [1, 1, 0, 0], [4, 5, 2, 0], [3, -2, 1, 1]])
b = np.array([[2, 1, 6, 4]])
b = np.transpose(b)

# Function from our matrixSolve module
x = lower_triangular_solve(L, b)

print("Lower triangular matrix: ")
print(L)
print("b vector: ")
print(b)
print("Solution: ")
print(x)

# Upper triangular solve
U = np.transpose(L)

# Function from our matrixSolve module
x = upper_triangular_solve(U, b)

print("Upper triangular matrix: ")
print(U)
print("b vector: ")
print(b)
print("Solution: ")
print(x)
