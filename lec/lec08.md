# Lecture 8: Iterative solutions of linear equations

## Direct methods

-   Gaussian elimination and LU factorisation are characterised as **direct** methods.

-   They are guaranteed to produce a solution with a fixed amount of work (in exact arithmetic).

-   This fixed amount of work may be **very** large.

For a general $n \times n$ matrix system $A \vec{x} = \vec{b}$:

-   the computational expense of all the direct methods is $O(n^3)$, i.e. increasing $n$ by a factor of 10 increases the computational work by a factor of 1000;

-   the amount of storage required for these approaches is $O(n^2)$, and is dominated by the matrix $A$;

-   as $n$ becomes large the storage and computational work required limit the practicality of the method.

## Iterative methods

It is possible to construct an **iteration** which will improve an approximation $\vec{x}^{(k)}$ to the solution of (linear) equations $A \vec{x} = \vec{b}$.

-   The iteration takes the form

    $$
    \vec{x}^{(k+1)} = \vec{F}(\vec{x}^{(k)})
    $$

	where $\vec{x}^{(k)}$ is now a vector of values and $\vec{F}$ is some vector function, yet to be defined.

-   Often a reasonable approximation to $\vec{x}$ is available which can be used to initiate the iterative method.

-   Sometimes there is no obvious initial approximation available. The method may still converge but take more iterations.

-   When should we stop?

### Some very bad examples

**Example 1**

Consider

$$
\vec{F}(\vec{x}^{(k)}) = \vec{x}^{(k)}.
$$

Each iteration is very cheap to compute but very inaccurate - it never converges!

**Example 2**

Consider 

$$
\vec{F}(\vec{x}^{(k)}) = \vec{x}^{(k)} + A^{-1} (\vec{b} - A \vec{x}^{(k)}).
$$

Each iteration is very expensive to compute - you have to invert $A$! - but it converges in just one step since

$$
\begin{aligned}
A \vec{x}^{(k+1)} & = A \vec{x}^{(k)} + A A^{-1} (\vec{b} - A \vec{x}^{(k)}) \\
& = A \vec{x}^{(k)} + \vec{b} - A \vec{x}^{(k)} \\
& = \vec{b}.
\end{aligned}
$$

**Key idea**

Construct iteration given by

$$
\vec{F}(\vec{x}^{(k)}) = \vec{x}^{(k)} + P (\vec{b} - A \vec{x}^{(k)}).
$$

for some matrix $P$ such that

-  $P$ is easy to compute, or the matrix vector product $P \vec{r}$ is easy to compute,
-  $P$ approximates $A^{-1}$ well enough that the algorithm converges in few iterations.

## Jacobi iteration

Consider the system $A \vec{x} = \vec{b}$ but rewrite the matrix $A$ as

$$
A = D + (A - D),
$$

where $D$ is the diagonal of $A$, i.e.

$$
D_{ii} = A_{ii} \quad \text{ and } \quad D_{ij} = 0 \text{ for } i \neq j.
$$

Manipulations give

$$
\begin{aligned}
A \vec{x} = (D + (A-D)) \vec{x} & = \vec{b} \\
D \vec{x} & = \vec{b} - (A-D) \vec{x} \\
D \vec{x} & = D \vec{x} + (\vec{b} - A \vec{x}) \\
\vec{x} = \vec{x} + D^{-1} (\vec{b} - A \vec{x}).
\end{aligned}
$$

That is take $P = D^{-1}$!

The **Jacobi iteration** is given by

$$
\vec{x}^{(k+1)} = \vec{x}^{(k)} + D^{-1}(\vec{b} - A \vec{x}^{(k)})
$$

-   $D$ is a *diagonal matrix*, so $D^{-1}$ is trivial to form (as long as the diagonal entries are all nonzero).

-   $\vec{b} - A \vec{x}^{(k)} = \vec{r}$ is call the **residual**.

### Notes

-   The cost of one iteration is $O(n^2)$ for a full matrix, and this is dominated by the matrix-vector product $A \vec{x}^{(k)}$.

-   This cost can be reduced to $O(n)$ if the matrix $A$ is sparse - this is when iterative methods are especially attractive (see next lecture).

-   The amount of work also depends on the number of iterations required to get a "satisfactory" solution.

    -   The number of iterations depends on the matrix;
	-   Fewer iterations are needed for a less accurate solution;
    -   A good initial estimate $\vec{x}^{(0)}$ reduces the required number of iterations.

-   Unfortunately, the iteration might not converge!

### Component by component

The Jacobi iteration updates all elements of $\vec{x}^{(k)}$ *simultaneously* to get $\vec{x}^{(k+1)}$.

Writing the method out component by component gives

$$
\begin{aligned}
x_1^{(k+1)} &= x_1^{(k)} + \frac{1}{A_{11}} \left( b_1 - \sum_{j=1}^n A_{1j} x_j^{(k)} \right) \\
x_2^{(k+1)} &= x_2^{(k)} + \frac{1}{A_{22}} \left( b_2 - \sum_{j=1}^n A_{2j} x_j^{(k)} \right) \\
\vdots \quad & \hphantom{=} \quad \vdots \\
x_n^{(k+1)} &= x_n^{(k)} + \frac{1}{A_{nn}} \left( b_n - \sum_{j=1}^n A_{nj} x_j^{(k)} \right).
\end{aligned}
$$

Note that once the first step has been taken, $x_1^{(k+1)}$ is already known, but the Jacobi iteration does not make use of this information!

## Gauss-Seidel iteration

Alternatively, the iteration might use $x_i^{(k+1)}$ as soon as it is calculated, giving

$$
\begin{aligned}
x_1^{(k+1)}
& = x_1^{(k)} + \frac{1}{A_{11}} \left(
b_1 - \sum_{j=1}^n A_{1j} x_j^{(k)}
\right) \\
x_2^{(k+1)}
& = x_2^{(k)} + \frac{1}{A_{22}} \left(
b_2 - A_{21} x_1^{(k+1)} - \sum_{j=2}^n A_{2j} x_j^{(k)}
\right) \\
x_3^{(k+1)}
& = x_3^{(k)} + \frac{1}{A_{33}} \left(
b_1 - \sum_{j=1}^2 A_{3j} x_j^{(k+1)} - \sum_{j=2}^n A_{3j} x_j^{(k)}
\right) \\
\vdots \quad & \hphantom{=} \quad \vdots \\
x_i^{(k+1)}
& = x_i^{(k)} + \frac{1}{A_{ii}} \left(
b_i - \sum_{j=1}^{i-1} A_{ij} x_j^{(k+1)} - \sum_{j=i}^n A_{ij} x_j^{(k)}
\right) \\
\vdots \quad & \hphantom{=} \quad \vdots \\
x_n^{(k+1)}
& = x_n^{(k)} + \frac{1}{A_{nn}} \left(
b_n - \sum_{j=1}^{n-1} A_{nj} x_j^{(k+1)} - A_{nn} x_n^{(k)}
\right).
\end{aligned}
$$

Consider the system $A \vec{x}= b$ but rewrite the matrix $A$ as

$$
A = D + L + U,
$$

where $D$ is the diagonal of $A$, $L$ contains the elements below the diagonal and $U$ contains the elements above the diagonal.

The system can be manipulated to give

$$
\begin{aligned}
A \vec{x} = (D + L + U) \vec{x} & = \vec{b} \\
(D + L) \vec{x} & = \vec{b} - U \vec{x} \\
(D + L) \vec{x} & = (D + L) \vec{x} + (\vec{b} - A \vec{x}) \\
\vec{x} & = \vec{x} + (D + L)^{-1} (\vec{b} - A \vec{x}),
\end{aligned}
$$

...and hence the **Gauss-Seidel** iteration

$$
\vec{x}^{(k+1)} = \vec{x}^{(k)} + (D + L)^{-1} (\vec{b} - A \vec{x}^{(k)}).
$$

That is $P = (D+L)^{-1}$.

### Example 1

Take two iterations of (i) Jacobi iteration; (ii) Gauss-Seidel iteration to approximate the solution of the following system using the initial guess $\vec{x}^{(0)} = (1, 1)^T$:

$$
\begin{pmatrix}
2 & 1 \\ -1 & 4
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}
 =
\begin{pmatrix}
3.5 \\ 0.5
\end{pmatrix}
$$

-   What happens if the initial estimate is altered to $\vec{x}^{(0)} = (2, 1)^T$ (homework).

-   Note that the exact solution to this system is $x_1 = 1.5$ and $x_2 = 0.5$.

#### (i) Jacobi iteration

Starting from $\vec{x}^{(0)} = (2, 1)^T$ we have

Iteration 1:

$$
\begin{aligned}
x^{(1)}_1 & = x^{(0)}_1 + \frac{1}{A_{11}} (b_1 - A_{11} x^{(0)}_1 - A_{12} x^{(0)}_2) \\
          & = 2 + \frac{1}{2} (3.5 - 2 \times 2 - 1 \times 1) = 1.25 \\
x^{(1)}_2 & = x^{(0)}_2 + \frac{1}{A_{22}} (b_2 - A_{21} x^{(0)}_1 - A_{22} x^{(0)}_2) \\
          & = 1 + \frac{1}{4} (0.5 - (-1) \times 2 - 4 \times 1) = 0.625.
\end{aligned}
$$

Iteration 2:

$$
\begin{aligned}
x^{(2)}_1 & = x^{(1)}_1 + \frac{1}{A_{11}} (b_1 - A_{11} x^{(1)}_1 - A_{12} x^{(1)}_2) \\
          & = 1.25 + \frac{1}{2} (3.5 - 2 \times 1.25 - 1 \times 0.625) = 1.4375 \\
x^{(2)}_2 & = x^{(1)}_2 + \frac{1}{A_{22}} (b_2 - A_{21} x^{(1)}_1 - A_{22} x^{(1)}_2) \\
          & = 0.625 + \frac{1}{4} (0.5 - (-1) \times 1.25 - 4 \times 0.625) = 0.4375.
\end{aligned}
$$

Note the only difference between the formulae for Iteration 1 and 2 is the iteration number, the superscript in brackets.

#### (ii) Gauss-Seidel iteration

Starting from $\vec{x}^{(0)} = (2, 1)^T$ we have

Iteration 1:

$$
\begin{aligned}
x^{(1)}_1 & = x^{(0)}_1 + \frac{1}{A_{11}} (b_1 - A_{11} x^{(0)}_1 - A_{12} x^{(0)}_2) \\
          & = 2 + \frac{1}{2} (3.5 - 2 \times 2 - 1 \times 1) = 1.25 \\
x^{(1)}_2 & = x^{(0)}_2 + \frac{1}{A_{22}} (b_2 - A_{21} x^{(1)}_1 - A_{22} x^{(0)}_2) \\
          & = 1 + \frac{1}{4} (0.5 - (-1) \times 1.25 - 4 \times 1) = 0.4375.
\end{aligned}
$$

Iteration 2:

$$
\begin{aligned}
x^{(2)}_1 & = x^{(1)}_1 + \frac{1}{A_{11}} (b_1 - A_{11} x^{(1)}_1 - A_{12} x^{(1)}_2) \\
          & = 1.25 + \frac{1}{2} (3.5 - 2 \times 1.25 - 1 \times 0.4375) = 1.53125 \\
x^{(2)}_2 & = x^{(1)}_2 + \frac{1}{A_{22}} (b_2 - A_{21} x^{(2)}_1 - A_{22} x^{(1)}_2) \\
          & = 0.4375 + \frac{1}{4} (0.5 - (-1) \times 1.53125 - 4 \times 0.4375) = 0.5078125.
\end{aligned}
$$

Again, note the changes in the iteration number on the right hand side of these equations, especially the differences against the Jacobi method.

### Example 2 (homework)

Take one iteration of (i) Jacobi iteration; (ii) Gauss-Seidel iteration to approximate the solution of the following system using the initial guess $\vec{x}^{(0)} = (1, 2, 3)^T$:

$$
\begin{pmatrix}
2 & 1 & 0 \\
1 & 3 & 1 \\
0 & 1 & 2
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
6 \\ 10 \\ 6
\end{pmatrix}.
$$

Note that the exact solution to this system is $x_1 = 2, x_2 = 2, x_3 = 2$.

### Notes

-   Here both methods converge, but fairly slowly. They might not converge at all!

-   We will discuss convergence and stopping criteria in the next lecture.

-   The Gauss-Seidel iteration generally out-performs the Jacobi iteration.

-   Performance can depend on the order in which the equations are written.

-   Both iterative algorithms can be made faster and more efficient for sparse systems of equations (far more than direct methods).

## Summary

-   Many complex computational problems simply cannot be solved with today's computers using direct methods.

-   Iterative methods are used instead since they can massively reduce the computational cost and storage required to get a "good enough" solution.

-   These basic iterative methods are simple to describe and program but generally slow to converge to an accurate answer - typically $O(n)$ iterations are required.

-   Their usefulness for general matrix systems is very limited therefore - next lecture we will show their value in the solution of sparse systems however.

-   More advanced iterative methods do exist but are beyond the scope of this module - see Final year projects, MSc projects, PhD, and beyond!

## Further reading

- Wikipedia: [Jacobi method](https://en.wikipedia.org/wiki/Jacobi_method)
- Wikipedia: [Gauss-Seidel method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
- Wikipedia: [Iterative methods](https://en.wikipedia.org/wiki/Iterative_method)
  - see also Richardson method, Damped Jacobi method, Successive over-relaxation method (SOR), Symmetric successive over-relaxation method (SSOR) and [Krylov subspace methods](https://en.wikipedia.org/wiki/Iterative_method#Krylov_subspace_methods)

- Jack Dongarra [Templates for the solution of linear systems: Stationary iterative methods](http://www.netlib.org/linalg/html_templates/node11.html#SECTION00720000000000000000)
- Golub, Gene H.; Van Loan, Charles F. (1996), Matrix Computations (3rd ed.), Baltimore: Johns Hopkins, ISBN 978-0-8018-5414-9.
- Saad, Yousef (2003). Iterative Methods for Sparse Linear Systems (2nd ed.). SIAM. p. 414. ISBN 0898715342.

- `scipy.sparse` iterative solvers: [Solving linear problems](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#solving-linear-problems)
- PETSc: [Linear system solvers](https://petsc.org/main/docs/manual/ksp/) - a high performance linear algebra toolkit
