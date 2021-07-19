---
author:
- name: Tom Ranner
  email: T.Ranner@leeds.ac.uk
title: COMP2421 Lecture 14
subtitle: A modelling example
# pandoc options
transition: none
backgroundTransition: none
autoPlayMedia: true
css: ./css/metropolis.css
center: false
# mathjax
mathjaxurl: ./js/mathjax/es5/tex-chtml-full.js
include-before: |
  <div style="display:none">
  $$
    \renewcommand{\vec}[1]{\boldsymbol{#1}}
  $$
  </div>
# citeproc
link-citations: true
# menu
menu: true
---
# A model for the trajectory of an object

## Newton's laws of motion

- A large component of many computer games is the *physics engine*.
- Typically this spends large numbers of cpu cycles simulating the motion of bodies, using Newton's laws, based upon the forces that are exerted upon them.
- In particular, Newton's 2nd law of motion says that the acceleration of an object in each direction is equal to the applied force in that direction divided by the mass of the object:
  $$
   \text{Force} = \text{Mass} \times \text{Acceleration}.
  $$
- One we know the acceleration of the object we can solve differential equations to calculate its subsequent velocity and position...

##

## Projectile example - equations

Using the following notation

- $X(t)$ is the horizontal distance of the object at time $t$
- $Y(t)$ is the vertical distance of the object at time $t$
- $U(t)$ is the horizontal speed of the object at time $t$
- $V(t)$ is the vertical speed of the object at time $t$

The above model leads to the following two differential equations:
$$
\begin{align}
U'(t) & = -k U(t) \\
V'(t) & = -k V(t) - g.
\end{align}
$$

We also know, from the definition of speed, that
$$
\begin{align}
X'(t) & = U(t) \\
Y'(t) & = V(t).
\end{align}
$$

## Projectile example - equations

The script `projectile.py` solves this system of equations using Euler's method:

```python
t = np.zeros([n+1,1]) # Initialise the array t
U = np.zeros([n+1,1]) # Initialise the array U
V = np.zeros([n+1,1]) # Initialise the array V
X = np.zeros([n+1,1]) # Initialise the array X
Y = np.zeros([n+1,1]) # Initialise the array Y
t[0] = 0.0
U[0] = 20.0
V[0] = 0.0
X[0] = 0.0
Y[0] = 100.0
dt = (tfinal-t0)/float(n)
# Calculate size of each interval
for i in xrange(n):
	# Take n steps of Euler’s method
	U[i+1] = U[i] + dt * (-k*U[i])
	V[i+1] = V[i] + dt * (-k*V[i] - g)
	X[i+1] = X[i] + dt * U[i]
	Y[i+1] = Y[i] + dt * V[i]
	t[i+1] = t[i] + dt
```


# Solution using Euler's method


# Solution using the Midpoint Method
