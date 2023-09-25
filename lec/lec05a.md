# Lecture 05: Solving triangular systems

A general *lower triangular* system of equations has $a_{ij} = 0$ for $j > i$ and takes the form:

$$
 \begin{pmatrix}
 a_{11} & 0 & 0 & \cdots & 0 \\
 a_{21} & a_{22} & 0 & \cdots & 0 \\
 a_{31} & a_{32} & a_{33} & \cdots & 0 \\
 \vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \cdots & a_{nn}
 \end{pmatrix}
 \begin{pmatrix}
 x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_n
 \end{pmatrix} =
 \begin{pmatrix}
 b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_n
 \end{pmatrix}.
$$

Note the first equation is

$$
a_{11} x_1 = b_1.
$$

The $x_i$ can be found by calculating

$$
x_i = \frac{1}{a_{ii}} \left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j \right)
$$

for each row $i = 1, 2, \ldots, n$ in turn.

-   Each calculation requires only previously computed values $x_j$ (and the sum gives a loop for $j < i$.
-   The matrix $A$ **must** have nonzero diagonal entries\
    i.e. $a_{ii} \neq 0$ for $i = 1, 2, \ldots, n$.
-   **Upper triangular** systems of equations can be solved in a similar manner.

## Example 1

Solve the lower triangular system of equations given by

$$
\begin{aligned}
 2 x_1 && && &= 2 \\
 x_1 &+& 2 x_2 && &= 7 \\
 2 x_1 &+& 4 x_2 &+& 6 x_3 &= 26
\end{aligned}
$$

or, equivalently,

$$
\begin{pmatrix}
2 & 0 & 0 \\
1 & 2 & 0 \\
2 & 4 & 6
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix} =
\begin{pmatrix}
2 \\ 7 \\ 26
\end{pmatrix}.
$$

## Example 1: solution

The solution can be calculated systematically from

$$
\begin{aligned}
x_1 &= \frac{b_1}{a_{11}} = \frac{2}{2} = 1 \\
x_2 &= \frac{b_2 - a_{21} x_1}{a_{22}}
= \frac{7 - 1 \times 1}{2} = \frac{6}{2} = 3 \\
x_3 &= \frac{b_3 - a_{31} x_1 - a_{32} x_2}{a_33}
= \frac{26 - 2 \times 1 - 4 \times 3}{6}  = \frac{12}{6}
= 2
\end{aligned}
$$

which gives the solution $\vec{x} = (1, 3, 2)^T$.

## Example 2 (homework)

Solve the upper triangular linear system given by

$$
\begin{aligned}
2 x_1 &+& x_2 &+& 4 x_3 &=& 12 \\
&& 1.5 x_2 && &=& 3 \\
&& && 2 x_3 &=& 4
\end{aligned}.
$$

## Notes

-   It is simple to solve a lower (upper) triangular system of equations (provided the diagonal is nonzero).

-   This process is often referred to as **forward** (**backward**) **substitution**.

-   A general system of equations (i.e. a full matrix $A$) can be solved rapidly once it has been reduced to upper triangular form.

-   This will be the topic of the next section...


## Further reading

- Wikipedia: [Triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix)
