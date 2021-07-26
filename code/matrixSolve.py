import numpy as np


def lower_triangular_solve(A, b0):
    """
    Solve the system  A x = b  where A is assumed to be lower triangular,
    i.e. A(i,j) = 0 for j > i, and the diagonal is assumed to be nonzero,
    i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   lower triangular n x n array
                b0   right hand side column n-vector
                
    RETURNS:    x   column n-vector solution    
    """

    # Check that A is lower triangular
    if not np.allclose(A, np.tril(A)):
        print("Error: The input array is not lower triangular!")
        return None

    # Get n-dimension
    n = len(b0)

    # Copy vector b0 and convert to float
    b = np.copy(b0).astype(float)

    # Initialise x
    x = np.zeros([n, 1])

    # Loop through the remaining rows, calculating the solution components
    # in turn by backward substitution

    for i in range(n):
        for j in range(i):
            b[i] = b[i] - A[i, j] * x[j]
        x[i] = b[i] / A[i, i]

    return x


def upper_triangular_solve(A, b0):
    """
    Solve the system  A x = b  where A is assumed to be upper triangular,
    i.e. A(i,j) = 0 for j < i, and the diagonal is assumed to be nonzero,
    i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   upper triangular n x n array
                b0   right hand side column n-vector
                
    RETURNS:    x   column n-vector solution    
    """

    # Check that A is upper triangular
    if not np.allclose(A, np.triu(A)):
        print("Error: The input array is not upper triangular!")
        return None

    # Get n-dimension
    n = len(b0)

    # Copy vector b0 and covert to float
    b = np.copy(b0).astype(float)

    # Initialise x
    x = np.zeros([n, 1])

    # Loop through the remaining rows, calculating the solution components
    # in turn by backward substitution

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i] = b[i] - A[i, j] * x[j]
        x[i] = b[i] / A[i, i]

    return x


def gauss_elimination(A, b, *args):
    """
    Reduce the system  A x = b  to upper triangular form, assuming that
    the diagonal is nonzero, i.e. A(i,i) \= 0.
    
    ARGUMENTS:  A   n x n matrix
                b   right hand side column n-vector
                
                print  (optional) prints elimination steps
    
    RETURNS:    A   upper triangular n x n matrix
                b   modified column n-vector    
    """
    # Get dimensions
    n = len(b)

    # Make sure entries are set to float
    A = A.astype(float)
    b = b.astype(float)

    # Loop through the rows (i) of the system
    for i in range(n - 1):
        # Print solution information
        if 'print' in args:
            print('Eliminate column %d\n' % i)
            input('Press key to continue')

        # Pick out the diagonal entry (and assume that it isn't zero
        r = 1. / A[i, i]

        # Loop through the rows (j) of the system below row i
        for j in range(i + 1, n):
            # Calculate the multiplier for that row for elimination
            d = r * A[j, i]

            # Loop through the elements of row j which have yet to be set to zero
            for k in range(i, n):
                # For column k, subtract the scaled element in row i from row j.
                A[j, k] = A[j, k] - d * A[i, k]

            # Subtract scalded right hand side of row i from row j
            b[j] = b[j] - d * b[i]

        if 'print' in args:
            print(A)
            print(b)

    return A, b


def gauss_elimination_pivot(A, b):
    """
    Reduce the system  A x = b  to upper triangular form, making use of
    row pivoting.
    
    ARGUMENTS:  A   n x n matrix
                b   right hand side column n-vector
    
    RETURNS:    A   upper triangular n x n matrix
                b   modified column n-vector    
    """
    # Get dimensions
    n = len(b)

    # Make sure entries are set to float
    A = A.astype(float)
    b = b.astype(float)

    # Loop through the rows (i) of the system.
    for i in range(n - 1):
        # Find the value and position of the largest entry in
        # column i on or below the diagonal
        amax = abs(A[i, i])
        kmax = -1
        for k in range(i + 1, n):
            bmax = abs(A[k, i])
            if bmax > amax:
                amax = bmax
                kmax = k

        # If an entry below the diagonal is larger than the one on the
        # diagonal then swap the rows
        if kmax > i:
            temp = np.copy(A[i, :])
            A[i, :] = A[kmax, :]
            A[kmax, :] = temp[:]

            tempb = np.copy(b[i])
            b[i] = b[kmax]
            b[kmax] = tempb

        # Now we carry out the usual elimination process, eliminating column i
        # Note - this is just the inner loop from gauss_elimination

        # Pick out the diagonal entry (and assume that it isn't zero
        r = 1. / A[i, i]

        # Loop through the rows (j) of the system below row i
        for j in range(i + 1, n):
            # Calculate the multiplier for that row for elimination
            d = r * A[j, i]

            # Loop through the elements of row j which have yet to be set to zero
            for k in range(i, n):
                # For column k, subtract the scaled element in row i from row j.
                A[j, k] = A[j, k] - d * A[i, k]

            # Subtract scalded right hand side of row i from row j
            b[j] = b[j] - d * b[i]

    return A, b


def lu_factorise(A):
    """
    LU factorise the matrix A into a lower triangular matrix L and an
    upper triangular matrix U.

    ARGUMENTS:  A   n x n matrix

    RETURNS:    L   lower triangular matrix
                U   upper triangular matrix
    """

    # Get matrix dimension
    n = len(A)

    # Make sure A entries are float
    A = A.astype(float)

    # Initialise L to be the n x n identity matrix I and U to be the
    # n x n zero matrix
    L = np.eye(n, dtype=float)
    U = np.zeros([n, n], dtype=float)

    # Loop through the column of the matrix
    for j in range(n - 1):
        # Compute the elements of U on and above the diagonal in column j
        # using previously computed elements of L and U.
        U[0, j] = A[0, j]
        for i in range(1, j + 1):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # Compute the elements of L below the diagonal in column j using
        # previously computed elements of L and U
        r = 1. / U[j, j]

        for i in range(j + 1, n):
            L[i, j] = r * (A[i, j] - np.dot(L[i, :j], U[:j, j]))

    # For column n there are no entries of L to be computed so only compute
    # the % elemens of U on and above the diagonal in column n, again using
    # previously computed elements of L and U
    U[0, -1] = A[0, -1]
    for i in range(1, n):
        U[i, -1] = A[i, -1] - np.dot(L[i, :i], U[:i, -1])

    return L, U


def gauss_seidel(A, u, b, n_iterations):
    """
    Solve the system A u = b using a Gauss-Seidel iteration

    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                n_iterations
                    integer number of iterations to carry out
   
    RESULTS:    u   k-vector storing solution    
    """

    # Get dimension
    k = len(A)

    # Make sure matrix A is float
    A = A.astype(float)

    for i in range(n_iterations):
        for j in range(k):
            u[j] = u[j] + (b[j] - np.dot(A[j, :], u)) / A[j, j]
        print(u)

    return u


def jacobi(A, u, b, n_iterations):
    """
    Solve the system A u = b using a Jacobi iteration
    
    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                n_iterations
                    integer number of iterations to carry out
    
    RESULTS:    u   k-vector storing solution
    """

    # Get dimension
    k = len(A)

    # Make sure matrix A is float
    A = A.astype(float)

    for i in range(n_iterations):
        r = (b - np.dot(A, u))
        for j in range(k):
            r[j] = r[j] / A[j, j]

        u = u + r

    return u


def jacobi2(A, u, b, n_iterations):
    """
    Solve the system A u = b using a Jacobi iteration
    
    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                n_iterations
                    integer number of iterations to carry out
    
    RESULTS:    u   k-vector storing solution
    """

    # Get dimension
    k = len(A)

    # Make sure matrix A is float
    A = A.astype(float)

    unew = np.zeros([k, 1])
    for i in range(n_iterations):
        for j in range(k):
            unew[j] = u[j] + (b[j] - np.dot(A[j, :], u)) / A[j, j]

        u = np.copy(unew)

    return u


def gauss_seidel_new(A, u, b, tol):
    """
    Solve the system A u = b using a Gauss-Seidel iteration
    
    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                tol real number providing the required convergence tolerance
    
    RESULTS:    u   k-vector storing solution
    """

    # Get dimension
    k = len(A)

    # Make sure matrix A is float
    A = A.astype(float)

    # Set the maximum number of iterations
    maxit = 1000

    # Initialise the iteration counter
    it = 0

    # Initialise diffRMS to exceed tol for the first iteration
    diffRMS = 2 * tol

    while (diffRMS > tol) and (it < maxit):
        uold = np.copy(u)
        for j in range(k):
            u[j] = u[j] + (b[j] - np.dot(A[j, :], u)) / A[j, j]

        diffRMS = 0
        for j in range(k):
            diffRMS = diffRMS + (u[j] - uold[j])**2

        it += 1
        diffRMS = np.sqrt(diffRMS)

    if diffRMS > tol:
        print('Warning! Iteration has not converged')

    return u


def jacobi_new(A, u, b, tol):
    """
    Solve the system A u = b using a Jacobi iteration
    
    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                tol real number providing the required convergence tolerance
    
    RESULTS:    u   k-vector storing solution
    """
    # Get dimension
    k = len(A)

    # Make sure matrix A is float
    A = A.astype(float)

    # Set the maximum number of iterations
    maxit = 1000

    # Initialise the iteration counter
    it = 0

    # Initialise diffRMS to exceed tol for the first iteration
    diffRMS = 2 * tol

    unew = np.zeros([k, 1])
    while (diffRMS > tol) and (it < maxit):
        for j in range(k):
            unew[j] = u[j] + (b[j] - np.dot(A[j, :], u)) / A[j, j]

        diffRMS = 0
        for j in range(k):
            diffRMS = diffRMS + (unew[j] - u[j])**2

        it += 1
        diffRMS = np.sqrt(diffRMS)
        print(it, diffRMS)
        u = np.copy(unew)

    if diffRMS > tol:
        print('Warning! Iteration has not converged')

    return u
