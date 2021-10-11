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

# Assign values to the parameters g and k
g = 9.81
k = 0.2

# Initialise the arrays t and s - to be used for plotting the solution
t = np.zeros([n + 1, 1])
U = np.zeros([n + 1, 1])
V = np.zeros([n + 1, 1])
X = np.zeros([n + 1, 1])
Y = np.zeros([n + 1, 1])

for speed in [5, 10, 15, 20, 25, 30]:
    # Initialise the arrays t and s - to be used for plotting the solution
    t = np.zeros([n + 1, 1])
    U = np.zeros([n + 1, 1])
    V = np.zeros([n + 1, 1])
    X = np.zeros([n + 1, 1])
    Y = np.zeros([n + 1, 1])
    t[0] = 0.0
    U[0] = speed
    V[0] = 0.0
    X[0] = 0.0
    Y[0] = 100.0

    # Calculate the size of each interval
    dt = (tfinal - t[0]) / n

    # Take n steps of Euler integration in which it is assumed that the
    # acceleration is approximately constant in each small time interval
    for i in range(n - 1):
        U[i + 1] = U[i] + dt * (-k * U[i])
        V[i + 1] = V[i] + dt * (-g - k * V[i])
        X[i + 1] = X[i] + dt * U[i]
        Y[i + 1] = Y[i] + dt * V[i]
        t[i + 1] = t[i] + dt

    # Plot calculated trajectory
    plt.plot(X, Y, label="Initial speed = %d m/s" % speed)

plt.legend()
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.xlabel("x : in metres")
plt.ylabel("y : in metres")
plt.show()
