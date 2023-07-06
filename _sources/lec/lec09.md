# Lecture 08: Sparse matrices and stopping criteria

##  Sparse Matrices

There are two main ways in which sparse matrices can be exploited in order to obtain benefits within iterative methods.

-   The storage must be reduced for $O(n^2)$.

-   The cost per iteration must be reduced from $O(n^2)$.

Recall that a sparse matrix is defined to be such that it has at most $\alpha n$ non-zero entries (where $\alpha$ is independent of $n$).

-   Typically this happens when we know there are at most $\alpha$ non-zero entries in any row.

### Sparse matrix storage

The simplest way in which a sparse matrix is stored is using three arrays:

-   an array of floating point numbers (`A_real` say) that stores the non-zero entries;

-   an array of integers (`I_row` say) that stores the row number of the corresponding entry in the real array;

-   an array of integers (`I_col` say) that stores the column numbers of the corresponding entry in the real array.

This requires just $3 \alpha n$ units of storage - i.e. $O(n)$.

### Sparse matrix multiplication

Given the above storage pattern, the following algorithm will execute a sparse matrix-vector multiplication ($\vec{z} = A \vec{y}$) in $O(n)$ operations:

``` python
z = np.zeros((n, 1))
for k in range(nonzero):
    z[I_row[k]] = z[I_row[k]] + A_real[k] * y[I_col[k]]
```

-   Here `nonzero` is the number of non-zero entries in the matrix.

-   Note that the cost of this operation is $O(n)$ as required.

## Convergence of an iterative method

We have discussed the construction of **iterations** which aim to find the solution of the equations $A \vec{x} = \vec{b}$ through a sequence of better and better approximations $\vec{x}^{(k)}$.

-   In general the iteration takes the form

    $$
    \vec{x}^{(k+1)} = \vec{F}(\vec{x}^{(k)})
    $$

	where $\vec{x}^{(k)}$ is a vector of values and $\vec{F}$ is some vector-valued function which we have defined.

-   How can we decide if this iteration has converged?

    -   We need $\vec{x} - \vec{x}^{(k)}$ to be small.

### Magnitude of a vector

How do we decide that a vector/array is small?

-   We need a way of defining the size/magnitude of an array.

-   The most common measure is to use the "Euclidean norm" of an array.

-   This is defined to be the square root of the sum of squares of the entries of the array:

    $$
    \| \vec{r} \| = \sqrt{ \sum_{i=1}^n r_i^2 }
    $$

	where $\vec{r}$ is a vector with $n$ entries.

### Examples

Consider the following sequence $\vec{x}^{(k)}$:

$$
\begin{pmatrix}
1 \\ -1
\end{pmatrix},
\begin{pmatrix}
1.5 \\ 0.5
\end{pmatrix},
\begin{pmatrix}
1.75 \\ 0.25
\end{pmatrix},
\begin{pmatrix}
1.875 \\ 0.125
\end{pmatrix},
\begin{pmatrix}
1.9375 \\ -0.0625
\end{pmatrix},
\begin{pmatrix}
1.96875 \\ -0.03125
\end{pmatrix},
\ldots
$$

-   What is $\|\vec{x}^{(1)} - \vec{x}^{(0)}\|$?
-   What is $\|\vec{x}^{(5)} - \vec{x}^{(4)}\|$?

Let $\vec{x} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$.

-   What is $\|\vec{x} - \vec{x}^{(3)}\|$?
-   What is $\|\vec{x} - \vec{x}^{(4)}\|$?
-   What is $\|\vec{x} - \vec{x}^{(5)}\|$?

### Convergence detection

Rather than decide in advance how many iterations (of the Jacobi or Gauss-Seidel methods) to use stopping criteria:

-   This could be a maximum number of iterations.

-   This could be the *change* in values is small enough:

    $$
    \|x^{(k+1)} - \vec{x}^{(k)}\| < tol,
    $$


-   This could be the *norm of the residual* is small enough:

	$$
	\| \vec{r} \| = \| \vec{b} - A \vec{x}^{(k)} \| < tol
	$$

-   In both cases, we call $tol$ the **convergence tolerance**.

-   The choice of $tol$ will control the accuracy of the solution.

### Discussion

> What is a good convergence tolerance?

## Failure to converge

In general there are two possible reasons that an iteration may fail to converge.

-   It may **diverge** - this means that $\|\vec{x}^{(k)}\| \to \infty$ as $k$ (the number of iterations) increases, e.g.:

    $$
    \begin{pmatrix}
    1 \\ 1
    \end{pmatrix},
    \begin{pmatrix}
    4 \\ 2
    \end{pmatrix},
    \begin{pmatrix}
    16 \\ 4
    \end{pmatrix},
    \begin{pmatrix}
    64 \\ 8
    \end{pmatrix},
    \begin{pmatrix}
    256 \\ 16
    \end{pmatrix},
    \begin{pmatrix}
    1024 \\ 32
    \end{pmatrix},
    \ldots
    $$

-   It may *neither* converge nor diverge, e.g.:

    $$
    \begin{pmatrix}
    1 \\ 1
    \end{pmatrix},
    \begin{pmatrix}
    2 \\ 0
    \end{pmatrix},
    \begin{pmatrix}
    3 \\ 1
    \end{pmatrix},
    \begin{pmatrix}
    1 \\ 0
    \end{pmatrix},
    \begin{pmatrix}
    2 \\ 1
    \end{pmatrix},
    \begin{pmatrix}
    3 \\ 0
    \end{pmatrix},
    \ldots
    $$

### Implementation

In addition to testing for convergence it is also necessary to include tests for failure to converge.

-   Divergence may be detected by monitoring $\|\vec{x}^{(k)}\|$.

-   Impose a maximum number of iterations to ensure that the loop is not repeated forever!


## Further reading

- Wikipedia [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix) - including a long detailed list of software libraries support sparse matrices.

- [`scipy.sparse`](https://docs.scipy.org/doc/scipy/reference/sparse.html) custom routines specialised to sparse matrices
- [SuiteSparse](http://faculty.cse.tamu.edu/davis/suitesparse.html), a suite of sparse matrix algorithms, geared toward the direct solution of sparse linear systems

- Stackoverflow: [Using a sparse matrix vs numpy array](https://stackoverflow.com/questions/36969886/using-a-sparse-matrix-versus-numpy-array)
- Jason Brownlee: [A gentle introduction to sparse matrices for machine learning](https://machinelearningmastery.com/sparse-matrices-for-machine-learning/), Machine learning mastery


- Jack Dongarra [Templates for the solution of linear systems: Stopping criteria](http://www.netlib.org/linalg/html_templates/node83.html)
