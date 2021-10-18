"""
TODO doc me
"""
# Python modules
import sys

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *
from nonlinear_functions import *


if __name__ == "__main__":
    print("\n\n--- sqrt2, 1, 1.5, 1.0e-4")
    secant(sqrt2, 1, 1.5, 1.0e-4)
    print("\n\n--- compund, 100, 120, 0.1")
    secant(compound, 100, 120, 0.1)
    print("\n\n--- naca0012, 1, 0.9, 1.0e-4")
    secant(naca0012, 1, 0.9, 1.0e-4)
    print("\n\n--- naca0012, 0, 0.1, 1.0e-4")
    secant(naca0012, 0.0, 0.1, 1.0e-4)
    print("\n\n-- lin, 2, 3, 1.0e-4")
    secant(lin, 2, 3, 1.0e-4)
