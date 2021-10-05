---
title: Lecture 10
subtitle: Effects of finite precision arithmetic
---

# The need for row swapping in GE

Consider the following linear system of equations
$$
\begin{pmatrix}
0 & 2 & 1 \\
2 & 1 & 0 \\
1 & 2 & 0
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 4 \\ 5
\end{pmatrix}
$$

*Problem*. We cannot eliminate the first column by the diagonal by adding multiples of row 1 to rows 2 and 3 respectively.

## Row swapping

*Solution*. Swap the order of the equations!

- Swap rows 1 and 2:
  $$
  \begin{pmatrix}
  2 & 1 & 0 \\
  0 & 2 & 1 \\
  1 & 2 & 0
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  4 \\ 7 \\ 5
  \end{pmatrix}
  $$

- Now apply Gaussian elimination
  $$
  \begin{pmatrix}
  2 & 1 & 0 \\
  0 & 2 & 1 \\
  0 & 1.5 & 0
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  4 \\ 7 \\ 3
  \end{pmatrix}
  ;
  \begin{pmatrix}
  2 & 1 & 0 \\
  0 & 2 & 1 \\
  0 & 0 & -0.75
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  4 \\ 7 \\ -2.25
  \end{pmatrix}.
  $$

## Another example

Consider another system of equations
$$
\begin{pmatrix}
2 & 1 & 1 \\
4 & 2 & 1 \\
2 & 2 & 0
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
 3 \\ 5 \\ 2
\end{pmatrix}
$$

- Apply Gaussian elimination as usual:
  $$
  \begin{pmatrix}
  2 & 1 & 1 \\
  0 & 0 & -1 \\
  2 & 2 & 0
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  3 \\ -1 \\ 2
  \end{pmatrix}
  ;
  \begin{pmatrix}
  2 & 1 & 1 \\
  0 & 0 & -1 \\
  0 & 1 & -1
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  3 \\ -1 \\ -1
  \end{pmatrix}
  $$

- *Problem*. We cannot eliminate the second column below the diagonal by adding a multiple of row 2 to row3.

## Another example (cont.)

- Again this problem may be overcome simply by swapping the order of the equations - this time swapping rows 2 and 3:
  $$
  \begin{pmatrix}
  2 & 1 & 1 \\
  0 & 1 & -1 \\
  0 & 0 & -1
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2 \\ x_3
  \end{pmatrix}
  =
  \begin{pmatrix}
  3 \\ -1 \\ -1
  \end{pmatrix}
  $$

- We can now continue the Gaussian elimination process as usual.

*In general*. Gaussian elimination requires row swaps to avoid breaking down when there is a zero in the "pivot" position.

# Problems with finite precision

::: {.container}
:::: {.col}
Consider using Gaussian elimination to solve the linear system of equations given by
$$
\begin{pmatrix}
\varepsilon & 1 \\
1 & 1
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}
 =
\begin{pmatrix}
2 + \varepsilon \\ 3
\end{pmatrix}
$$
where $\varepsilon \neq 1$ (as illustrated in the file [`gaussElimTest1.py`](../code/lec10/gaussElimTest1.py))
::::
:::: {.col .fragment}
- The true, unique solution is $(x_1, x_2)^T = (1, 2)^T$.

- If $\varepsilon \neq 0$, Gaussian elimination gives
  $$
  \begin{pmatrix}
  \varepsilon & 1 \\
  0 & 1 - \frac{1}{\varepsilon}
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2
  \end{pmatrix}
   =
  \begin{pmatrix}
  2 + \varepsilon \\ 3 - \frac{2 + \varepsilon}{\varepsilon}
  \end{pmatrix}
  $$

- Problems occur not only when $\varepsilon = 0$ but also when it is very small, i.e. when $\frac{1}{\varepsilon}$ is very large, this will introduce very significant rounding errors into the computation.
::::
:::

## Removing the problem

::: {.container}
:::: {.col}
Use Gaussian elimination to solve the linear system of equations given by
$$
\begin{pmatrix}
1 & 1 \\
\varepsilon & 1
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}
 =
\begin{pmatrix}
3 \\ 2 + \varepsilon
\end{pmatrix}
$$
where $\varepsilon \neq 1$ is very small (as illustrated in the file [`gaussElimTest2.py`](../code/lec10/gaussElimTest2.py)).
::::
:::: {.col .fragment}
- The true solution is still $(x_1, x_2)^T = (1, 2)^T$.

- Gaussian elimination now gives
  $$
  \begin{pmatrix}
  1 & 1 \\
  0 & 1 - \varepsilon
  \end{pmatrix}
  \begin{pmatrix}
  x_1 \\ x_2
  \end{pmatrix}
  =
  \begin{pmatrix}
  3 \\ 2 - 2\varepsilon
  \end{pmatrix}
  $$

- The problems due to small values of $\varepsilon$ have disappeared.
::::
:::
## Notes

- Writing the equations in a different order has removed the previous problem.

- The diagonal entries are now always *relatively* larger.

- The interchange of the order of equations is a simple example of **row pivoting**. This strategy avoids excessive rounding errors in the computations.

# Gaussian elimination with pivoting

- Before eliminating entries in column $j$:

  - find the entry in column $j$, below the diagonal, of maximum magnitude;
  - if that entry is larger in magnitude than the diagonal entry then swap its row with row $j$.

- Then eliminate column $j$ as before.

The pivoting algorithm ([`gauss_elimination_pivot`](../code/matrixSolve.html#gauss_elimination_pivot)) is defined in [`matrixSolve.py`](../code/matrixSolve.html) and applied in the file [`gaussElimTest1Pivot.py`](../code/lec10/gaussElimTest1Pivot.html).

## Notes

- This algorithm will always work when the matrix $A$ is invertible/non-singular.

- Conversely, if all of the possible pivot values are zero this implies that the matrix is singular and a unique solution does not exist.

- At each elimination step the row multiplies used are guaranteed to be at most one in magnitude...

- ... so any errors in the representation of the system cannot be amplified by the elimination process.

- As always, solving $A \vec{x} = \vec{b}$ requires that the entries in $\vec{b}$ are also swapped in the appropriate way.

## Notes (cont.)

- Pivoting can be applied in an equivalent way to LU factorisation.

- The sequence of pivots is independent of the vector $\vec{b}$ and can be recorded and reused.

- The constraint imposed on the row multipliers means that for LU factorisation every entry in $L$ satisfies $| l_{ij} | \le 1$.

- In python, the function call
  ```python
  P, L, U = scipy.linalg.lu(A, permute_l=0)
  ```
  factorises $A$ and returns $L$, $U$ and the **pivot matrix** $P$.

## Example

Consider the linear system of equations given by
$$
\begin{pmatrix}
10 & -7 & 0 \\
-3 & 2.1 - \varepsilon & 6 \\
5 & -1 & 5
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 9.9 + \varepsilon \\ 11
\end{pmatrix}
$$
where $0 \le \varepsilon \ll 1$, and solve it using

1. Gaussian elimination without pivoting

2. Gaussian elimination with pivoting.

The exact solution is $\vec{x} = (0, -1, 2)^T$ for any $\varepsilon$ in the given range.

## Example (cont.)

1. Solve the system using Gaussian elimination with no pivoting.

Eliminating the first column gives
$$
\begin{pmatrix}
10 & -7 & 0 \\
0 & -\varepsilon & 6 \\
0 & 2.5 & 5
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 12 + \varepsilon \\ 7.5
\end{pmatrix}
$$
and then the second column gives
$$
\begin{pmatrix}
10 & -7 & 0 \\
0 & -\varepsilon & 6 \\
0 & 0 & 5 + 15/\varepsilon
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 12 + \varepsilon \\ 7.5 + 2.5(12 + \varepsilon)/\varepsilon
\end{pmatrix}
$$

## Example (cont.)

which leads to
$$
x_3 = \frac{3 + \frac{12 + \varepsilon}{\varepsilon}}{2 + \frac{6}{\varepsilon}} \qquad
x_2 = \frac{(12 + \varepsilon) - 6x_3}{-\varepsilon} \qquad
x_1 = \frac{7+ 7x_2}{10}.
$$
There are many divisions by $\varepsilon$, so we will have problems if $\varepsilon$ is small.

## Example (cont.)

2. Solve the system using Gaussian elimination with pivoting.

The first stage is identical (because $a_{11} = 10$ is largest).
$$
\begin{pmatrix}
10 & -7 & 0 \\
0 & -\varepsilon & 6 \\
0 & 2.5 & 5
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 12 + \varepsilon \\ 7.5
\end{pmatrix}
$$
but now $|a_{22}| = \varepsilon$ and $|a_{32}| = 2.5$ so we swap rows 2 and 3 to give
$$
\begin{pmatrix}
10 & -7 & 0 \\
0 & 2.5 & 5 \\
0 & -\varepsilon & 6
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 7.5 \\ 12 + \varepsilon
\end{pmatrix}
$$

## Example (cont.)

Now we may eliminate column 2:
$$
\begin{pmatrix}
10 & -7 & 0 \\
0 & 2.5 & 5 \\
0 & 0 & 6 + 2 \varepsilon
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
 =
\begin{pmatrix}
7 \\ 7.5 \\ 12 + 4 \varepsilon
\end{pmatrix}
$$
which leads to the exact answer:
$$
x_3 = \frac{12 + 4\varepsilon}{6 + 2 \varepsilon} = 2 \qquad
x_2 = \frac{7.5 - 5x_3}{2.5} = -1 \qquad
x_1 = \frac{7 + 7 x_2}{10} = 0.
$$
