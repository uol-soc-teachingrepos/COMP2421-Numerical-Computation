---
title: Lecture 4
subtitle: Matrices and vectors
starttime: "Oct 04, 2021 10:05"
---
# Introduction to matrices

**What is a matrix?**

A matrix is a two-dimensional array of objects (usually numbers)...

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
  4.1 & 4.1 & 4.1 & 2.2 & -8.8 & 1.1
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

This example has $m$ rows and $n$ columns. We call $A$ an $m \times n$ matrix ("$m$ by $n$" matrix).

## Notes

- The entry $A_{ij}$ appears in row $i$ and column $j$.
- The values $A_{ij}$ are known as **coefficients** of $A$.
- We will only consider cases where the coefficients, $A_{ij}$, are real numbers.
- We say that two matrices, $A$ and $B$, are equal (i.e. $A=B$) if:
  1. $A$ and $B$ have the same number of rows;
  2. $A$ and $B$ have the same number of columns;
  3. $A_{ij} = B_{ij}$ for every corresponding entry of the matrices.


# Matrix addition

Two matrices, $A$ and $B$, may be added to form a new matrix (let's call it $C$) provided $A$ and $B$ are of the same size, i.e.:

1. $A$ and $B$ have the same number of rows;
2. $A$ and $B$ have the same number of columns.

Their sum, $C$, is such that $C_{ij} = A_{ij} + B_{ij}$ for every entry of each row and column.

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
  2. $B_{ij} = \alpha A_{ij}$ for every entry of each row and column.

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

## Properties of matrix addition

Let $A, B$ and $C$ be matrices of the same dimensions, then

- Matrix addition is associative: $(A+B)+C = A+(B+C)$.

- Matrix addition is commutative: $A+B = B+A$.

- For the corresponding zero matrix: $O+A = A$.

- Defining $-A$ to be $-1A$ then: $-A + A = O$.

## Properties of scalar multiplication

Let $A$ and $B$ be matrices of the same dimension, and $\alpha$ and $\beta$ be scalars, then

- $1A = A$ and $0A = O$.
- Scalar multiplication is distributive: $\alpha(A+B) = \alpha A + \beta B$.
- Similarly: $(\alpha + \beta) = \alpha A +\beta B$.
- Also: $(\alpha \beta) A = \alpha (\beta A)$.

# Matrix Multiplication

- Recall from last lecture that it is possible to add matrices together
 provided each matrix has *the same dimensions*.

 - Note that when a matrix has $m$ rows and $n$ columns we say that it
 is an $m \times n$ matrix (these are its dimensions).

 - It was also shown that one can multiple a matrix by a real number (i.e. a *scalar*).

 - Under certain circumstances it is also possible to define a way in which
 two matrices may be multiplied together, to form a new matrix as their
 product...

## Definition of matrix multiplication

- If $A$ is an $m \times n$ matrix and $B$ is a $p \times q$ matrix,
 then it is only possible to form their product, $C=AB$, if $n=p$ (i.e.\ the
 number of columns in the first matrix is equal to the number of rows in the
 second matrix).

- If it is the case that $n=p$ then each entry of the product is defined
 as follows:
 $$
 C_{ij} \; = \;(AB)_{ij} \; = \;
 A_{i1}B_{1j} + A_{i2}B_{2j} + A_{i3}B_{3j} + \ldots + A_{in}B_{nj} \;.
 $$

- This holds for $i=1,...,m$ and $j=1,...,q$, hence the product $C$ is
 a $m \times q$ matrix -- with entry $C_{ij}$ computed by multiplying entries
 of row $i$ of $A$ by corresponding entries of column $j$ of $B$.

## Examples

$$
\begin{pmatrix}
		 0.0 & -1.0 & 1.0 \\ 1.0 & 1.0 & 1.0
\end{pmatrix}
\begin{pmatrix}
		 -1.0 & 2.0 \\ 1.0 & 0.0 \\ 2.0 & 3.0
		\end{pmatrix}
		=
		\begin{pmatrix}
		1.0 & 3.0 \\ 2.0 & 5.0
		\end{pmatrix}
$$

$$
\begin{pmatrix}
		 2.0 & -2.0 \\ 5.0 & 1.0
		\end{pmatrix}
		\begin{pmatrix}
		 3.0 & 2.0 & 4.0 \\ 1.0 & 0.0 & -1.0
		\end{pmatrix}
		=
		\begin{pmatrix}
		4.0 & 4.0 & 10.0 \\ 16.0 & 10.0 & 19.0
	   \end{pmatrix}
$$

$$
\begin{pmatrix}
		 11.0 & 0.0 & -2.0 & 0.0 \\ 0.0 & 16.0 & 1.0 & 0.0\\1.0&2.0& 1.0&2.0
\end{pmatrix}
		\begin{pmatrix}
		 1.0 & 0.0 \\ 2.0 & 1.0 \\ 0.0 & 1.0 \\ 1.0 & 1.0
		\end{pmatrix}
		=
		\begin{pmatrix}
		11.0 & -2.0 \\ 32.0 & 17.0 \\ 7.0 & 5.0
		\end{pmatrix}
$$

## Examples (cont.)

Let
$$
A = \begin{pmatrix}
		 2.0 & 1.0 \\ 1.0 & 2.0
	   \end{pmatrix} , \;
	  B = \begin{pmatrix}
		 1.0 & 2.0 \\ 0.0 & 1.0 \\ -1.0 & 1.0
		\end{pmatrix} , \;
	  C = \begin{pmatrix}
		 0.0 & 1.0 & 2.0 \\ 1.0 & 2.0 & 3.0 \\ 2.0 & 4.0 & 0.0
		\end{pmatrix}
$$

- What is $AB$?
- What is $BA$?
- What is $BC$?
- What is $CB$?
- What is $(CB)A$?
- What is $C(BA)$?

## Notes

- The product of two arbitrary matrices, $A$ and $B$ say, may not be
 well-defined (the number of columns of $A$ must equal the number of
 rows of $B$).

 - Even if $AB$ is well-defined, $BA$ may not be.

 - Even if both $AB$ and $BA$ are well-defined, they will usually be
 different, e.g.
 $A=\begin{pmatrix}2.0 & 0.0 \\ 1.0 & 2.0\end{pmatrix}$
  and $B=\begin{pmatrix}1.0 & 1.0 \\ 1.0 & 0.0\end{pmatrix}$.

 - Matrix multiplication is associative: $(AB)C = A(BC)$ provided the
 matrices are of appropriate dimensions for these products to be well-defined.

## Matrix Transposition

- An important matrix operation is called the **transpose**.

- The transpose of a matrix $A$ (denoted by $A^{\rm T}$ or $A'$) is such that
$(A^{\rm T})_{ij} = A_{ji}$.

- Hence, when $A$ is an $m \times n$ matrix, then $A^{\rm T}$ is $n \times m$.

- Informally, the transpose of a matrix is formed by swapping the rows
 and columns around.

- For example:
  - $\begin{pmatrix} 1.0 & 2.0 & 3.0 \\ 0.0 & 1.0 & 2.0
		\end{pmatrix}^{\rm T} = \begin{pmatrix}
		 1.0 & 0.0 \\ 2.0 & 1.0 \\ 3.0 & 2.0 \end{pmatrix}$.

## Matrix transposition (cont.)

- Other examples:
  - $\begin{pmatrix} 2.0 & 0.0 \\ 1.0 & 3.0
		\end{pmatrix}^{\rm T} = \begin{pmatrix}
		 2.0 & 1.0 \\ 0.0 & 3.0 \end{pmatrix}$
  - $\begin{pmatrix} 2.0 & 0.0 & 1.0 \\ 0.0 & 3.0 & 1.0 \\
								   1.0 & 1.0 & -1.0 \end{pmatrix}^{\rm T} =
		 \begin{pmatrix} 2.0 & 0.0 & 1.0 \\ 0.0 & 3.0 & 1.0 \\
								   1.0 & 1.0 & -1.0 \end{pmatrix}$

- A matrix with an equal number of rows and columns is called a
 **square** matrix.

- Note that any matrix $A$ such that $A^{\rm T} = A$ is called a **symmetric**
 matrix (and must be a square matrix).

## Identity Matrices

- These are square matrices that have the structure:
\begin{eqnarray*}
 I_n & = &
 \begin{pmatrix}
		 1 & 0 & 0 & \ldots & 0 \\
		 0 & 1 & 0 & \ldots & 0 \\
		 0 & 0 & 1 & \ldots & 0 \\
		 \vdots & \vdots & \vdots & & \vdots \\
		 0 & 0 & 0 & \ldots & 1
		\end{pmatrix}
\end{eqnarray*}
- For example:
  - $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and
 $I_3 = \begin{pmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&1 \end{pmatrix}$.

# Invertible Matrices

- An $n \times n$ matrix $A$ is invertible (non-degenerate, non-singular) if there exists $B$ which is an $n \times n$ matrix such that $AB = BA = I_n$.

- When $A$ is invertible, then its inverse is unique and we denote it by $A^{-1}$.

- For example:
  - $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and
 $B = \begin{pmatrix} 2/3& -1/3 \\ -1/3&2/3 \end{pmatrix}$.
- For $n \times n$ matrix $A$, if $AB = I_n$, then $A,B$ are both invertible and $A^{-1}= B$ and $B^{-1} = A$.

## Properties of invertible matrices

- If $A$ is invertible, then $(A^{-1})^{-1} = A$.

- If $A$ is invertible and the scalar $\lambda \ne 0$, then $\lambda A$ is invertible and $(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}$.

- If $A$ is invertible, then $A^{\rm T}$ is invertible and $(A^{\rm T})^{-1} = (A^{-1})^{\rm T}$.

- If $A$, $B$ are $n \times n$ matrices and are both invertible, then $AB$ is invertible and $(AB)^{-1} = B^{-1}A^{-1}$.

- However, $(A + B)^{-1}$ does not necessary equal to $A^{-1} + B^{-1}$.

## Properties of matrix multiplication

Let $A$ be an $m \times n$ matrix and let $B$ and $C$ be matrices for which
the following sums and products are defined...

- $I_m A = A$ and $A I_n = A$.

- Associative: $(AB)C = A(BC)$.

- Left distributive: $A(B+C) = AB+AC$.

- Right distributive: $(A+B)C = AC+BC$.

- NOT commutative: $AB \neq BA$.


# Row and Column Vectors

- A matrix with just one row is called a **row vector**.

- A matrix with just one column is called a **column vector**.

- Often the term *vector* is used as short-hand for *column vector*.

- We often use the notation $\vec{a}$ to represent a **vector**.

- Hence $\vec{a}^{\rm T}$ is a row vector!

- Suppose $\vec{a}$ and $\vec{b}$ are vectors of dimension
 $n$ (i.e. matrices of dimension $n \times 1$) then:
  - $\vec{a}^{\rm T} \vec{b}$ is a well-defined matrix multiplication
 resulting in a $1 \times 1$ matrix;

## Row and Column Vectors (cont.)

- The numerical value computed by $\vec{a}^{\rm T} \vec{b}$ is
 called the **scalar product** of $\vec{a}$ and $\vec{b}$:
  - this is sometimes denoted as $\vec{a} \cdot \vec{b}\; ;$
  - note that $\vec{a} \cdot \vec{b} = \vec{b} \cdot
  \vec{a}\; .$

- For example, suppose:
$$
  A = \begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix}\;,
  \;\; \vec{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}\;,
  \;\; \vec{b} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}\;,
$$
 then show that:
  - $\vec{x} \cdot \vec{b} = 11 \;;$
  - $A \vec{x} = \vec{b} \;.$
