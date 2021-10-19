"""
gaussElimTestPivot

Solve example 2x2 system of the form A x = b to illustrate
that pivoting can reduce the effects of rounding error

"""

# Python modules
import sys

import numpy as np

# comp2421 modules
sys.path.append("..")
from matrixSolve import *

# Print headers for the table output
print("epsilon    x[0]       x[1]")
print("--------   --------   --------")

# Loop through values of epsilon to give different matrices
for epsilon in [1e-5, 1e-10, 1e-14, 1e-16, 1e-18]:
    # Initialise the example 2x2 matrix
    A = np.array([[epsilon, 1], [1, 1]])

    # Initialise the example right hand side column 2-vector
    b = np.array([[2 + epsilon, 3]])
    b = np.transpose(b)

    # Reduce the system A x = b to upper triangular form
    A, b = gauss_elimination_pivot(A, b)

    # Solve upper triangular system A x = b
    x = upper_triangular_solve(A, b)

    # Print solution to the screen
    print(f"{epsilon:6.2e} {x[0][0]:10.6f} {x[1][0]:10.6f}")
