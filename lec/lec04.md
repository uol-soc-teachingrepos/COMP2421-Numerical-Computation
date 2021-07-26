---
author:
- name: Tom Ranner
  email: T.Ranner@leeds.ac.uk
title: COMP2421 Lecture 4
subtitle: Matrices and vectors I
# pandoc options
transition: none
backgroundTransition: none
autoPlayMedia: true
center: false
# mathjax
mathjaxurl: ../js/mathjax/es5/tex-chtml-full.js
include-before: |
  <div style="display:none">
  $$
    \renewcommand{\vec}[1]{\boldsymbol{#1}}
  $$
  </div>
# citeproc
link-citations: true
---
<!-- TODO: table of contents -->

# Introduction to matrices

**What is a matrix?**

A matrix is a two-dimensional array of objects (usually number)...

- e.g. 4 rows and 5 columns
  $$
  \begin{pmatrix}
  1.1 & -1.2 & 0.0 & 21.3 & -2.9 \\
  11.2 & 0.0 & 0.0 & -2.4 & -0.4 \\
  0.0 & 16.0 & 1.5 & 0.0 & 4.1 \\
  4.1 & 4.1 & 4.1 & 2.2 & -8.8
  \end{pmatrix}
  $$

- e.g. 2 rows and 6 columns
  $$
  \begin{pmatrix}
  1.1 & -1.2 & 0.0 & 21.3 & -2.9 & 1.1 \\
  4.1 & 4.1 & 4.1 & 2.2 & -8.8 1.1
  \end{pmatrix}
  $$

## General matrix form

A *matrix* can have any number of rows and any number of columns...
$$
 A =
 \begin{pmatrix}
 A_{11} & A_{12} & A_{13} & \cdots & A_{1n} \\
 A_{21} & A_{22} & A_{23} & \cdots & A_{2n} \\
 A_{31} & A_{32} & A_{33} & \cdots & A_{3n} \\
 \vdots & \vdots & \vdots & & \vdots \\
 A_{m1} & A_{m2} & A_{m3} & \cdots & A_{mn}
 \end{pmatrix}
$$

This example has $m$ rows and $n$ columns. We call $A$ an $m \times n$ matrix.

## Notes

- The entry $A_{ij}$ appears in row $i$ and column $j$.
- The values $A_{ij}$ are known as **coefficients** of $A$.
- We will only consider cases where the coefficients, $A_{ij}$, real numbers.
- We say that two matrices, $A$ and $B$, are equal (i.e. $A=B$) if:
  1. $A$ and $B$ have the same number of rows;
  2. $A$ and $B$ have the same number of columns;
  3. $A_{ij} = B_{ij}$ for every corresponding entry of the matrices.


# Matrix addition

Two matrices, $A$ and $B$, may be added to form a new matrix (let's call it $C$) provided $A$ and $B$ are of the same size, i.e.:

1. $A$ and $B$ have the same number of rows;
2. $A$ and $B$ have the same number of columns.

Their sum, $C$, is such that\
$C_{ij} = A_{ij} + B_{ij}$ for every entry of each row and column.

## Examples

$$
\begin{pmatrix}
0.0 & -1.0 \\
1.0 & 1.0
\end{pmatrix} +
\begin{pmatrix}
-1.0 & 2.0 \\
1.0 & 0.0
\end{pmatrix} =
\begin{pmatrix}
-1.0 & 1.0 \\
2.0 & 1.0
\end{pmatrix}.
$$

$$
\begin{pmatrix}
2.0 & -2.0 & 5.0
\end{pmatrix} +
\begin{pmatrix}
3.0 & 2.0 & 4.0
\end{pmatrix} =
\begin{pmatrix}
5.0 & 0.0 & 9.0
\end{pmatrix}.
$$

$$
\begin{pmatrix}
11.2 & 0.0 & -2.4 \\
0.0 & 16.0 & 1.5
\end{pmatrix} +
\begin{pmatrix}
-1.2 & 1.0 & 1.4 \\
1.0 & -6.0 & 1.5
\end{pmatrix} =
\begin{pmatrix}
10.0  & 1.0 & -1.0 \\
1.0 & 10.0 & 3.0
\end{pmatrix}.
$$

# Scalar multiplication

- A matrix, $A$, may be multiplied by a scalar $\alpha$ to form a new matrix - let's call it $B$.

- This new matrix, $B$, is such that
  1. $B$ has the same dimensions as $A$;
  2. $B_{ij} = \alpha_{ij}$ for every entry of each row and column.

- Similarly, provided matrices $X$ and $Y$ have the same size, we may define $C = \alpha X + \beta Y$ (for real numbers $\alpha$ and $\beta$) such that:
  - $C$ has the same dimensions as $X$ and $Y$;
  - $C_{ij} = \alpha X_{ij} + \beta Y_{ij}$ for every entry of each row and column.

## Examples

$$
2
\begin{pmatrix}
11.2 & 0.0 & -2.4 & -0.4 \\
0.0 & 16.0 & 1.5 & 0.0
\end{pmatrix} =
\begin{pmatrix}
22.4 & 0.0 & -4.8 & -0.8 \\
0.0 & 32.0 & 3.0 & 0.0
\end{pmatrix}
$$

$$
-3
\begin{pmatrix}
0.0 & -1.0 \\
1.0 & 1.0
\end{pmatrix} +
2
\begin{pmatrix}
-1.0 & 2.0 \\
1.0 & 0.0
\end{pmatrix} =
\begin{pmatrix}
-2.0 & 7.0 \\
-1.0 & -3.0
\end{pmatrix}.
$$

$$
3
\begin{pmatrix}
 3.0 \\ 2.0 \\ 1.0
\end{pmatrix} +
5
\begin{pmatrix}
2.0 \\ -2.0 \\ 0.0
\end{pmatrix} =
\begin{pmatrix}
19.0 \\ -4.0 \\ 3.0
\end{pmatrix}.
$$

## Examples (cont)

Let
$$
A =
\begin{pmatrix}
2.0 & 1.0 \\
1.0 & 2.0
\end{pmatrix},
B =
\begin{pmatrix}
1.0 & 2.0 \\
0.0 & 1.0 \\
-1.0 & 1.0
\end{pmatrix},
C =
\begin{pmatrix}
0.0 & 1.0 \\
1.0 & 2.0 \\
2.0 & 4.0
\end{pmatrix}.
$$

- What is $B+C$?
- What is $3B - 2C$?
- What is $3A + B$?
- What is $5C + 2A$?
- What is $2A + \begin{pmatrix} 1.0 & 1.0 \\ 1.0 & 1.0 \end{pmatrix}$?

## Zero matrices

- A zero matrix (let's call is $O$) is a matrix for which every entry is zero.

- Note that there are an infinite number of zero matrices!

- If $A$ is an $m \times n$ matrix (i.e., has $m$ rows and $n$ columns) then there is a unique matrix $O$ such that $A + O = A$:
  - $O$ is the $m \times n$ matrix for which every entry is zero.

# Properties of matrix addition

Let $A, B$ and $C$ be matrices of the same dimensions, then

- Matrix addition is associative: $(A+B)+C = A+(B+C)$.
- Matrix addition is commutative: $A+B = B+A$.
- For the corresponding zero matrix: $O+A = A$.
- Defining $-A$ to be $-1A$ then: $-A + A = O$.

# Properties of scalar multiplication

Let $A$ and $B$ be matrices of the same dimension, and $\alpha$ and $\beta$ be scalars, then

- $1A = A$ and $0A = O$.
- Scalar multiplication is distributive: $\alpha(A+B) = \alpha A + \beta B$.
- Similarly: $(\alpha + \beta) = \alpha A +\beta B$.
- Also: $(\alpha \beta) A = \alpha (\beta A)$.
