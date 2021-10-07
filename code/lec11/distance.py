"""
distance

Estimate the distance covered by an object moving with
speed s(t)

To run via commandline use one of the following:

python distance.py -m 1
python distance.py -m 2


"""
# Python modules
import getopt
import sys

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.size"] = "16"

# Comp2941 modules
sys.path.append("..")
from matrixSolve import *


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

    if mode == "1":
        distance()
    elif mode == "2":
        distance2()


def distance():
    """
    Estimate distance by considering smaller and smaller intervals
    """

    # print output
    print("# intervals \tincrement size \ttotal distance")

    # Consider breaking the problem into different numbers of intervals
    for n in [1e1, 1e2, 1e3, 1e4, 1e5]:
        # The time increment for each interval is dt
        dt = 1.0 / n
        # The initial distance covered and initial time and are both zero
        d = 0.0
        t = 0.0
        for i in range(int(n)):
            # Increment the distance covered and the time
            d = d + dt * s(t)
            t = t + dt

        print("%d \t%6.3e \t%7.5f" % (n, dt, d))


def distance2():
    """
    Estimate distance and then plot this as a function of time
    """

    # Consider breaking the problem into n intervals
    n = 1000

    # The time increment for each interval is dt
    dt = 1.0 / n

    # Save the distance and time at each step
    d = np.zeros([n + 1, 1])
    t = np.zeros([n + 1, 1])

    # The initial distance covered and initial time are both zero
    d[0] = 0.0
    t[0] = 0.0

    for i in range(n):
        # Increment the distance covered and the time
        d[i + 1] = d[i] + dt * s(t[i])
        t[i + 1] = t[i] + dt

    # Output a plot of both d and s as functions of t
    speed = s(t)

    plt.figure()
    plt.plot(t, d, "r", label="Distance")
    plt.plot(t, speed, "b", label="Speed")
    plt.xlim([0, t.max()])
    plt.xlabel("t: time in seconds")
    plt.legend()
    plt.title("Distance and speed as functions of time")
    plt.savefig("graphics.svg")


def s(t):
    """
    Return a value for the speed, s, as a function of time, t.
    ARGUMENTS:  t   the time
    RETURNS:    s   the speed
    """
    return 1 + 5 * t - 6 * t ** 2


if __name__ == "__main__":
    main(sys.argv)
