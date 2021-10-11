"""
Projectile.py

Script that approximates the solution to a system of differential 
equations that gives a simple model for the motion of a projectile

"""

# Python modules
import sys

import matplotlib.pyplot as plt
import numpy as np

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *


def rhs(t, y):
    """
    Define the right-hand side of a system of 4 differential equations.

    ARGUMENTS:  t   value of t
                y   4-dimensional array

    RESULTS:    f 1x4-dimensional array of the right-hand of differential equation
    """

    f = np.zeros([4, 1])

    g = 9.81
    k = 0.2

    f[0] = -k * y[0]
    f[1] = -g - k * y[1]
    f[2] = y[0]
    f[3] = y[1]

    return f.T


# Set the initial speed of the projectile in the x direction:

# Select initial and final time
t0 = 0.0
tfinal = 6.0

# Select the number of time steps to be taken
n = 1200

# Setup plot
plt.figure()

for speed in [5, 10, 15, 20, 25, 30]:
    # initialise y defined as
    # [X-velocity,Y-velocity,X-position,Y-position]
    y0 = np.array([speed, 0, 0, 100.0])

    # Apply Euler for n steps, assuming that acceleration is approximately
    # constant in each small time interval
    t, y = eulerN(rhs, t0, y0, tfinal, n)

    # Plot calculated trajectory
    plt.plot(y[:, 2], y[:, 3], label="Initial speed = %d m/s" % speed)

plt.legend()
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.xlabel("x : in metres")
plt.ylabel("y : in metres")
plt.show()
