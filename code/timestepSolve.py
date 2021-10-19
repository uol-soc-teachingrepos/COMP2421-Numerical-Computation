import numpy as np


def euler(rhs, t0, y0, tfinal, n):
    """
    Use Euler's method to solve the differential equation y'(t)=f(t,y) subject
    to the initial condition y(t0) = y0.

    ARGUMENTS:  t0  initial value of t
                y0  initial value of y(t) when t=t0
                tfinal final value of t for which the solution is required
                n   the number of sub-intervals to use for the approximation
                rhs function of right-hand side of differential equation


    RESULTS:    t   (n+1)-vector storing the values of t at which the solution
                    is estimated
                y   (n+1)-vector storing the estimated solution.
    """

    # Initialise the arrays ta and y
    t = np.zeros([n + 1, 1])
    y = np.zeros([n + 1, 1])
    t[0] = t0
    y[0] = y0

    # Calculate the size of each interval
    dt = (tfinal - t0) / float(n)
    # Take n steps of Euler's method
    for i in range(n):
        y[i + 1] = y[i] + dt * rhs(t[i], y[i])
        t[i + 1] = t[i] + dt

    return t, y


def midpoint(rhs, t0, y0, tfinal, n):
    """
    Use midpoint method to solve the differential equation y'(t)=f(t,y) subject
    to the initial condition y(t0) = y0.

    ARGUMENTS:  t0  initial value of t
                y0  initial value of y(t) when t=t0
                tfinal final value of t for which the solution is required
                n   the number of sub-intervals to use for the approximation
                rhs function of right-hand side of differential equation


    RESULTS:    t   (n+1)-vector storing the values of t at which the solution
                    is estimated
                y   (n+1)-vector storing the estimated solution.
    """

    # Initialise arrays t and y
    t = np.zeros([n + 1, 1])
    y = np.zeros([n + 1, 1])
    t[0] = t0
    y[0] = y0

    # Calculate the size of each interval
    dt = (tfinal - t0) / float(n)

    # Take n steps of the midpoint method...
    for i in range(n):
        yhalf = y[i] + 0.5 * dt * rhs(t[i], y[i])
        thalf = t[i] + 0.5 * dt
        y[i + 1] = y[i] + dt * rhs(thalf, yhalf)
        t[i + 1] = t[i] + dt

    return t, y


def eulerN(rhs, t0, y0, tfinal, n):
    """
    Use Euler's method to solve N number of differential equation y'(t)=f(t,y) subject
    to the initial condition y(t0) = y0.

    ARGUMENTS:  t0  initial value of t
                y0  N-dimensional array of initial value of y(t) when t=t0
                tfinal final value of t for which the solution is required
                n   the number of sub-intervals to use for the approximation
                rhs function of right-hand side of differential equation


    RESULTS:    t   (n+1)-vector storing the values of t at which the solution
                    is estimated
                y   N x (n+1)-matrix array storing the estimated solution.
    """

    # Get dimensions
    N = len(y0)

    # Initialise the arrays ta and y
    t = np.zeros([n + 1, 1])
    y = np.zeros([n + 1, N])  # N x (n+1) matrix
    t[0] = t0
    y[0, :] = y0

    # Calculate the size of each interval
    dt = (tfinal - t0) / float(n)
    # Take n steps of Euler's method
    for i in range(n):
        y[i + 1, :] = y[i, :] + dt * rhs(t[i], y[i, :])
        t[i + 1] = t[i] + dt

    return t, y


def midpointN(rhs, t0, y0, tfinal, n):
    """
    Use midpoint method to solve N number of differential equation y'(t)=f(t,y) subject
    to the initial condition y(t0) = y0.

    ARGUMENTS:  t0  initial value of t
                y0  N-dimensional initial value of y(t) when t=t0
                tfinal final value of t for which the solution is required
                n   the number of sub-intervals to use for the approximation
                rhs function of right-hand side of differential equation


    RESULTS:    t   (n+1)-vector storing the values of t at which the solution
                    is estimated
                y   N x (n+1)-vector storing the estimated solution.
    """

    # Get dimensions
    N = len(y0)

    # Initialise arrays t and y
    t = np.zeros([n + 1, 1])
    y = np.zeros([n + 1, N])
    t[0] = t0
    y[0, :] = y0

    # Calculate the size of each interval
    dt = (tfinal - t0) / float(n)

    # Take n steps of the midpoint method...
    for i in range(n):
        yhalf = y[i, :] + 0.5 * dt * rhs(t[i], y[i, :])
        thalf = t[i] + 0.5 * dt
        y[i + 1, :] = y[i, :] + dt * rhs(thalf, yhalf)
        t[i + 1] = t[i] + dt

    return t, y
