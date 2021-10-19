""" runEuler.py

Script that calls the Euler function (defined in numericalSolve.py)
with smaller and smaller values of dt and plots the results

"""

# Python modules
import sys

import matplotlib.pyplot as plt

# Comp2941 modules
sys.path.append("..")
from timestepSolve import *


def rhs(t, y):
    """
    Return a value for the right-hand side of the differential equation
    y'(t) = f(t,y)

    ARGUMENTS:  t   the current value of t
                y   the current value of y

    RETURNS:    f   the value of f(t,y)
    """

    return -(y ** 2) + 1.0 / t


# Set the number of time steps to be taken
plt.figure()
for n in [3, 6, 12, 24, 48, 96, 192]:
    t, y = euler(rhs, 1, 2, 2, n)
    plt.plot(t, y, label="n = %d" % n)

plt.legend()
plt.xlim([1, 2])
plt.ylim([0.8, 2])

plt.tight_layout()
plt.savefig("euler.svg")
