---
author:
- name: Tom Ranner
  email: T.Ranner@leeds.ac.uk
title: COMP2421 Lecture 1
# pandoc options
transition: none
backgroundTransition: none
autoPlayMedia: true
css: ../css/metropolis.css
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
# menu
menu: true
---

# Comp2421

Numerical computation

Dr Thomas Ranner (Tom)

3.40d Bragg Building

Please contact me via Teams

# Lecture one

**Module overview**

Objectives and syllabus

**Semester one**

Books and websites

Administration

What is numerical computation?

Examples and applications

## Module objectives

- Understand how to compute with vectors and matrices.
- Appreciate the role numerical computation plays in CS.
- Choose a computational model appropriately, accounting for issues of accuracy, reliability and efficiency.
- Understand how to assess or measure the error in a numerical algorithm and be familiar with how such errors are controlled.

## Module objectives (cont.)

- Understand the fundamental techniques for the design of efficiency numerical algorithms.
- Demonstrate how these algorithms are analysed.
- Understand several advanced data structures, their efficient implementation and applications.
- Understand how these algorithms and data structures relate to the central practical problems of modern computer science.

## Syllabus

- **Vectors and matrices**: introduction and justification; vector and matrix operations; identity matrix; inverse of a matrix.

- **Approximation and errors**: modelling and mathematical modelling; discrete and continuous models; floating point and rounding errors; balancing accuracy and efficiency.

- **Static systems**: iterative methods for solving nonlinear scalar equations; methods for solving linear systems of equations; systems without unique solutions.

- **Evolving systems**: derivatives and rates of change; initial value problems; stability and convergence of computer models.

# Numerical computation

Books and websites \
Administration \

The programming for this module will be carried out using `python3`.

## Python

The latest available version of python is available via [Anaconda](https://www.anaconda.com/products/individual#Downloads).

Anaconda provides a full scientific Python distribution, including as standard tools for numerical analysis, data visualisation, image processing, and much more!

This scientific Python distribution is available on all School of Computing machines, specifically all SoC Linux computers.

## Python (cont.)

On a SoC Linux computer, you can run
```sh
$ module add anaconda3/2020.11
```
and you can test your python version with
```sh
$ python --version
Python 3.8.5
```

Coursework using Python will begin in week 3 - after the introduction to vectors and matrices.

## Relevance to Level 1 modules

This module builds upon material that you have already met in your first year. Prerequisites include:

- **COMP1421** Fundamental mathematical concepts
- **COMP1721** Object oriented programming

We also add to some of the material from:

- **COMP1212** Computer processors

## Relevance to Level 2 and 3 modules

The material covered here is important for a large number of subject areas including Scientific Computation, Computational Modelling, Machine Learning/AI, Computer Graphics, Quantum Computing.

This module is a pre-requisite for later modules in:

- **COMP3811** Computer graphics
- **COMP3910** Combinatorial optimisation
- **COMP3221** Parallel computation

Other modules that will benefit from material covered here:

- **COMP2721** Algorithms and data structures II (level 2)
- **COMP2611** Artificial intelligence (level 2)
- **COMP3631** Intelligent systems and robotics
- **COMP3611** Machine learning
- **COMP3940** Graph algorithms and approximation

## Reference materials - Python

- For general Python, refer to your first-year teaching materials.

- For a refresher course in Python: \
  http://interactivepython.org/runestone/static/thinkcspy/index.html

- For `numpy`, `scipy` etc: \
  http://scipy-lectures.github.io \
  https://github.com/jrjohansson/scientific-python-lectures

## Books

Additional useful texts

TODO update

## Module components

**Lectures**

TODO

**Tutorials**

TODO

**Homework and coursework exercise**

These will be provided *weekly* throughout the semester.

Courseworks are designed to give practice and reinforce the lectures. Coursework material is examinable.

## Assessment

TODO TBC

**Examination**

**Summative coursework**

**Formative homework**


## Virtual learning environment

As with all SoC  modules COMP2421 will make substantial use of the VLE:
[minerva.leeds.ac.uk](https://minerva.leeds.ac.uk)

This will include all:

- lecture notes and announcements;
- coursework/homework and (later) model solutions;
- links to external resources and web pages;
- module-related discussions (teams?)

TODO teams link?

# Numerical algorithms

- Numerical algorithms are those which operate on *floating point numbers*.

- They are used to provide solutions (or approximations to solutions) of mathematical models of "real world" problems.

- Such problems arise in a very wide range of applications (a few examples to follow).

- An important feature of these algorithms is that they need to account for the fact that arithmetic with floating point numbers is not exact!

## Applications I

TODO update with videos/pictures/also EDI

**Entertainment - computer gaming**

- Realistic behaviour within games requires an accurate and efficient *physics engine*.

- Uses *Newton's laws of motion* to predict motion (e.g. projectiles, vehicles, etc) and impacts (e.g. crashes, collisions, etc).

- These are examples of dynamic models which must be solved in "real time".

## Applications II

**Weather forecasting**

- These models are hugely complex but also hugely important!

- They effectively try to predict what will happen in billions of "boxes of air" above the Earth's surface.

- They use Newton's second law based upon forces such as: gravity, atmospheric pressure differences and the Coriolis force.

- They involve many other physical laws too: conservation of energy, conservation of mass, the perfect gas law, a water vapour equation, etc.

- These are also dynamic models and must be solved in faster than "real time" (thus requiring enormous computing resources).

## Applications III

**Engineering**

Many examples could be mentioned...

- Aerodynamics of vehicles in road transport and aviation.

- Integrity of structures in civil engineering.

- Predicting the behaviour of complex electrical circuits (in computer chip design for example).

## Applications IV

**Other applications**

- Climate models: used to predict future climate change.

- Biomedicine and health: from diagnostics through device operation to population models.

- Economic models: used for local, notational and international forecasts of stock markets, inflation, etc.

- Data mining requires complex models of very large data sets in order to extract useful information from them (e.g. Google PageRank)

- Many more.....
