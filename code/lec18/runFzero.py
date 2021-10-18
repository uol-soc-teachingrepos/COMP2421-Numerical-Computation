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
    fzero(sqrt2, 1.0, tolx=1.0e-12, tolfun=1.0e-12)
    fzero(naca0012, 0.5, tolx=1.0e-12, tolfun=1.0e-12)
