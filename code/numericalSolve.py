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
    print(" it       x            f(x)\n")

    # Set the initial estimate for the root and evaluate the function there.
    x = x0
    f = fnon(x)
    it = 0

    # Print the estimate and function value
    print(f"{it:4d} {x:12.6f} {f:12.6f}")

    # Repeat the Newton iteration until the magnitude of the function value is
    # less than tol.
    while abs(f) > tol:
        # Apply one iteration of Newton's method and evaluate the function at the
        # new estimate.
        x = x - f / dfnon(x)
        f = fnon(x)
        it = it + 1

        # Print the new estimate and function value.
        print(f"{it:4d} {x:12.6f} {f:12.6f}")


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

    # format for printing
    prec = int(-np.log10(tol)) + 1
    format = f" {{x:{prec+4}.{prec}f}} {{f:{prec+4}.{prec}f}}"

    # Print column headings for output.
    print(" x" + " " * (prec + 4) + " f" + " " * (prec + 4))
    print(" " + "-" * (prec + 5) + " " + "-" * (prec + 5))

    # Set the initial estimate for the root and evaluate the function there.
    x = x0
    f = fnon(x)

    # Print the estimate and function value.
    print(format.format(x=x, f=f))

    # Repeat the Newton iteration until the magnitude of the function value is
    # less than tol.
    while abs(f) > tol:
        # Apply one iteration of Newton's method and evaluate the function at the
        # new estimate.
        x = x - (dx * f) / (fnon(x + dx) - f)
        f = fnon(x)

        # Print the new estimate and function value.
        print(format.format(x=x, f=f))

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


def secant(fnon, x0, x1, tol):
    """
    Use the secant method to find the root of the nonlinear equation fnon(x)=0
    starting from the estimates x0 and x1.

    ARGUMENTS:  fnon  handle for the nonlinear function
                x0    the initial estimate
                x1    the second estimate
                tol   convergence tolerance

    RETURNS:    x     the computed root
                f     the function value at that root
    """
    # Print column headings for output
    print("      x            f(x)\n")

    # Set the initial estimate for the root and evaluate the function there.
    f0 = fnon(x0)
    f1 = fnon(x1)

    # Print the estimate and function value.
    print(" %20.14f %20.14f" % (x0, f0))
    print(" %20.14f %20.14f" % (x1, f1))

    # Repeat the secant iteration until the magnitude of the function value is
    # less than tol.

    while abs(f1) > tol:
        # Apply one iteration of the secant method and evaluate the function at the
        # new estimate.
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = fnon(x2)
        # Print the new estimate and function value.
        print(" %20.14f %20.14f" % (x2, f2))

        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f2

    x = x1
    f = f1

    return x, f


def fzero(fnon, x0, x1=None, tolx=1e-4, tolfun=1e-4, maxiter=100):
    """
    TODO doc me
    """
    print("running fzero with arguments")
    print(
        f"fnon = {fnon.__name__}, x0 = {x0}, x1 = {x1}, tolx = {tolx}, tolfunc = {tolfun}, maxiter = {maxiter}"
    )

    # find initial function value
    f0 = fnon(x0)

    if x1 is None:
        # find x1 > x0 st f0 * f1 < 0
        it = 0
        d = tolx
        x1 = x0 + d
        f1 = fnon(x1)
        while f0 * f1 > 0:
            it += 1
            d *= 2
            x1 += d
            f1 = fnon(x1)
        print(f"found opposite sign at {x1} -> f({x1}) = {f1} after {it} iterations")
    else:
        f1 = fnon(x1)
        if f0 * f1 > 0:
            print("WARNING initial bracket does not bracket solution")
            exit(1)

    # go into iteration
    it = 0
    x2, f2 = x1, f1
    print(" it   solution    f value      ")
    print(" ---- ----------- -------------")

    # while not converged
    while abs(x1 - x0) > tolx and abs(f2) > tolfun and it < maxiter:
        # update it
        it += 1

        # take one step of secant method
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        # if x2 outside interval
        if x2 < min(x0, x1) and x2 > max(x0, x1):
            # replace x2 with one step of bisection
            x2 = (x0 + x1) / 2.0
            print("bisection")

        # evaluate f at x2
        f2 = fnon(x2)

        # choose updated interval
        if f0 * f2 <= 0:
            # root is between [x0, x2]
            x1, f1 = x2, f2
        else:
            # root is between [x2, x1]
            x0, f0 = x2, f2

        # print guess
        print(f"{it:4d} {x2:12.6f} {f2:12.6e}")

    if it == maxiter:
        print("WARNING: method has not converged")
        print(f"|x1 - x0| = {abs(x1 - x0)}")
        print(f"|f(x2)| = {abs(f2)}")
