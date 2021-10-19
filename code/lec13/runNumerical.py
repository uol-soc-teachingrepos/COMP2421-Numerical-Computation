""" runNumerical.py

Script that compares euler and midpoint numerical methods

To run via commandline use one of the folllowing:

python runNumerical.py -m euler python runNumerical.py -m midpoint

"""

# Python modules
import getopt
import sys

import matplotlib.pyplot as plt

# Comp2941 modules
sys.path.append("..")
from timestepSolve import *


def main(argv):
    try:
        opts, _ = getopt.getopt(argv[1:], "m:", ["mode="])
    except getopt.GetoptError:
        print("Warning: Unknown flag!")
        sys.exit(2)

    mode = None

    for opt, arg in opts:
        if opt in ("-m", "--mode"):
            mode = arg

    if mode == "euler":
        runEuler()
    elif mode == "midpoint":
        runMidpoint()
    else:
        # no option passed do both
        runEuler()
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

    # set up figure
    plt.figure()
    # print table header
    print("n    dt      soln    error")
    print("---  ------  ------  ------")
    # ensure t is defined
    t = np.array([1.0, 2.0])

    # Set the number of time steps to be taken
    for n in [10, 20, 40, 80, 160, 320, 640]:
        # run euler scheme
        t, y = euler(rhs, 1.0, 1.0, 2.0, n)
        plt.plot(t, y, label=f"n = {n}")

        # compute error and time step
        dt = (2.0 - 1.0) / float(n)
        soln = y[n][0]
        error = abs(soln - 8.0)

        # print output
        print(f"{n:3d} {dt:7.4f} {soln:7.4f} {error:7.4f}")

    # plot results
    plt.legend(loc="upper left")
    plt.xlim([t.min(), t.max()])
    plt.ylim([0, 8])
    plt.savefig("euler.svg")


def runMidpoint():
    """
    Function that calls the midpoint function with smaller and smaller values of
    dt and plots the results.
    """
    # set up figure
    plt.figure()
    # print table header
    print("n    dt      soln    error")
    print("---  ------  ------  ------")
    # ensure t is defined
    t = np.array([1.0, 2.0])

    for n in [10, 20, 40, 80, 160, 320, 640]:
        # run midpoint scheme
        t, y = midpoint(rhs, 1.0, 1.0, 2.0, n)
        plt.plot(t, y, label=f"n = {n}")

        # compute error and timestep
        dt = (2.0 - 1.0) / float(n)
        soln = y[n][0]
        error = abs(soln - 8.0)

        # print output
        print(f"{n:3d} {dt:7.4f} {soln:7.4f} {error:7.4f}")

    # plot results
    plt.legend(loc="upper left")
    plt.xlim([t.min(), t.max()])
    plt.ylim([0, 8])
    plt.savefig("midpoint.svg")


if __name__ == "__main__":
    main(sys.argv)
