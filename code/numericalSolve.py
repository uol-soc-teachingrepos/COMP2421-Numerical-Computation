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

    return t, y, thalf, yhalf


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


def bisection(fnon, xL, xR, tol):
    """
    Use the basic bisection method to find the root of the nonlinear equation
    fnon(x)=0 within the bracket [xL,xR].

    ARGUMENTS:  fnon  handle for the nonlinear function
                xL,xR the initial bracket [xL,xR], for which f(xL)*f(xR)<0
                tol   convergence tolerance

    RETURNS:    x     the computed root
                f     the function value at that root
    """

    # Find the function values on the initial bracket
    fL = fnon(xL)
    fR = fnon(xR)

    if fL * fR > 0:
        print("Warning! The input values do not provide a bracket")
        return None, None

    else:
        # Print column heading for output
        print(" it  (    xL,          f(xL)    ) (    xR,          f(xR)    )\n")

        # iteration counter for output
        it = 0

        # Repeat the bisection iteration until the bracket width is less than tol
        while abs(xR - xL) > tol:
            # Print the current bracket and the function values at each end.
            print(f"{it:3d}  ({xL:12.8f}, {fL:12.8f}) ({xR:12.8f}, {fR:12.8f})")

            # Find the midpoint of the bracket and evaluate the function there.
            xC = 0.5 * (xL + xR)
            fC = fnon(xC)

            # Choose the new bracket to contain the root.
            if fL * fC <= 0:
                # The root is to the left of C, so set R=C
                xR = xC
                fR = fC
            else:
                # The root is to the right of C, so set L=C
                xL = xC
                fL = fC

            # update counter
            it = it + 1

    # Set final estimate to be the midpoint value
    x = 0.5 * (xL + xR)
    f = 0.5 * (fL + fR)

    return x, f


def newton(fnon, dfnon, x0, tol):
    """
    Use Newton's method to find the root of the nonlinear equation fnon(x)=0,
    with derivative dfnon(x) and starting from the estimate x0.

    ARGUMENTS:  fnon  handle for the nonlinear function
                dfnon handle for the derivative of the nonlinear function
                x0    the initial estimate
                tol   convergence tolerance

    RETURNS:    x     the computed root
                f     the function value at that root
    """
    # Print column headings for output
    print("      x            f(x)\n")

    # Set the initial estimate for the root and evaluate the function there.
    x = x0
    f = fnon(x)

    # Print the estimate and function value
    print(" %12.6f %12.6f" % (x, f))

    # Repeat the Newton iteration until the magnitude of the function value is
    # less than tol.
    while abs(f) > tol:
        # Apply one iteration of Newton's method and evaluate the function at the
        # new estimate.
        x = x - f / dfnon(x)
        f = fnon(x)

        # Print the new estimate and function value.
        print(" %12.6f %12.6f" % (x, f))


def modified_newton(fnon, x0, tol):
    """
    Use a modified Newton method to solve the nonlinear equation fnon(x)=0,
    starting from the estimate x0.

    ARGUMENTS:  fnon  handle for the nonlinear function
                x0    the initial estimate
                tol   convergence tolerance

    RETURNS:    x     the computed root
                f     the function value at that root
    """

    # Select a suitable value for dx
    eps = np.finfo(float).eps
    dx = np.sqrt(eps)

    # Print column headings for output.
    print("      x            f(x)")

    # Set the initial estimate for the root and evaluate the function there.
    x = x0
    f = fnon(x)

    # Print the estimate and function value.
    print(" %12.6f %12.6f" % (x, f))

    # Repeat the Newton iteration until the magnitude of the function value is
    # less than tol.
    while abs(f) > tol:
        # Apply one iteration of Newton's method and evaluate the function at the
        # new estimate.
        x = x - (dx * f) / (fnon(x + dx) - f)
        f = fnon(x)

        # Print the new estimate and function value.
        print(" %12.6f %12.6f" % (x, f))

    return x, f


def difference(fnon, dfnon, x0, dx):
    """
    Approximation of the derivative of the function fnon(x) at the point x0.

    ARGUMENTS:  fnon  handle for the nonlinear function
                dfnon handle for the true derivative (for error checking)
                x0    the point at which the derivative is required
                dx    the size of the step for the derivative approximation

    RETURNS:    d     the estimate of the derivative
                error   the error in the approximation to the derivative
    """

    d = (fnon(x0 + dx) - fnon(x0)) / dx
    error = abs(d - dfnon(x0))
    return d, error


def rk4(rhs, t0, y0, tfinal, n):
    """
    Use the fourth order Runge-Kutta method to solve the differential
    equation y'(t)=f(t,y), subject to the initial condition y(t0) = y0.

    ARGUMENTS:  t0  initial value of t
                y0  initial value of y(t) when t=t0
                tfinal final value of t for which the solution is required
                n   the number of sub-intervals to use for the approximation
                rhs function of right-hand side of differential equation

    RESULTS:    t   (n+1)-vector storing the values of t at which the solution
                    is estimated
                y   (n+1)-vector storing the estimated solution.
    """

    # Initialise the arrays t and y
    t = np.zeros([n + 1, 1])
    y = np.zeros([n + 1, 1])
    t[0] = t0
    y[0] = y0

    # Calculate the size of each interval
    dt = (tfinal - t0) / float(n)

    # Take n steps of the RK4 method...
    for i in range(n):
        k1 = dt * rhs(t[i], y[i])
        k2 = dt * rhs(t[i] + 0.5 * dt, y[i] + 0.5 * k1)
        k3 = dt * rhs(t[i] + 0.5 * dt, y[i] + 0.5 * k2)
        k4 = dt * rhs(t[i] + dt, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t[i + 1] = t[i] + dt

    return t, y
