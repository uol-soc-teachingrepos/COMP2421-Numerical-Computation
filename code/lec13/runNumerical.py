"""
runNumerical.py

Script that compares euler and midpoint numerical methods

To run via commandline use one of the folllowing:

python runNumerical.py -m euler
python runNumerical.py -m midpoint

"""

# Python modules
import getopt
import sys

import matplotlib.pyplot as plt

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "m:", ["mode="])
    except getopt.GetoptError:
        print("Warning: Unknown flag!")
        sys.exit(2)
        return 0

    mode = None

    for opt, arg in opts:
        if opt in ("-m", "--mode"):
            mode = arg

    if mode == "euler":
        runEuler()
    elif mode == "midpoint":
        runMidpoint()


def rhs(t, y):
    """
    Return a value for the right-hand side of the differential equation
    y'(t) = f(t,y)

    ARGUMENTS:  t   the current value of t
                y   the current value of y

    RETURNS:    f   the value of f(t,y)
    """

    return 3.0 * y / t


def runEuler():
    """
    Function that calls the Euler function with smaller and smaller values of
    dt and plots the results.
    """
    # Set the number of time steps to be taken
    print("n \tdt \tsoln \terror \tratio")
    plt.figure()
    errorold = 0.0
    ratio = 0.0
    for n in [10, 20, 40, 80, 160, 320, 640]:
        t, y = euler(rhs, 1.0, 1.0, 2.0, n)
        plt.plot(t, y, label=f"n = {n}")

        dt = (2.0 - 1.0) / float(n)
        soln = y[n][0]
        error = abs(soln - 8.0)

        if errorold > 0.0:
            ratio = error / errorold

        errorold = error
        print(f"{n} \t{dt:2.4f} \t{soln:2.4f} \t{error:2.4f} \t{ratio:2.4f}")

    plt.legend(loc="upper left")
    plt.xlim([t.min(), t.max()])
    plt.ylim([0, 8])
    # plt.show()


def runMidpoint():
    """
    Function that calls the midpoint function with smaller and smaller values of
    dt and plots the results.
    """
    # Set the number of time steps to be taken
    print("n \tdt \tsoln \terror \tratio")
    plt.figure()
    errorold = 0.0
    ratio = 0.0
    for n in [10, 20, 40, 80, 160, 320, 640]:
        t, y, thalf, yhalf = midpoint(rhs, 1.0, 1.0, 2.0, n)
        plt.plot(t, y, label=f"n = {n}")

        dt = (2.0 - 1.0) / float(n)
        soln = y[n][0]
        error = abs(soln - 8.0)

        if errorold > 0.0:
            ratio = error / errorold

        errorold = error
        print(f"{n} \t{dt:2.4f} \t{soln:2.4f} \t{error:2.4f} \t{ratio:2.4f}")

    plt.legend(loc="upper left")
    plt.xlim([t.min(), t.max()])
    plt.ylim([0, 8])
    # plt.show()


if __name__ == "__main__":
    main(sys.argv)
