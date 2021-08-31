---
title: COMP2421 Lecture 1
---
# Module contents

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

> Try this yourself! Make sure you can access a working version of python (version >= 3.6) and can import `numpy` and `scipy`.

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
  <http://interactivepython.org/runestone/static/thinkcspy/index.html>

- For `numpy`, `scipy` etc: \
  <http://scipy-lectures.github.io> \
  <https://github.com/jrjohansson/scientific-python-lectures>

## Books

Additional useful texts

- [Introduction to Linear Algebra](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991011421399705181) (Fifth Edition), Gilbert Strang, Wellesley-Cambridge Press, 2016. \
  with [MIT course material](https://web.mit.edu/18.06/www)

- [Scientific Computing: An Introductory Survey](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991009203099705181), T.M. Heath, McGraw-Hill, 2002. \
  some [lecture notes based on the book](http://heath.cs.illinois.edu/scicomp/notes/index.html)

- [Numerical Recipes in C++/C/FORTRAN](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991010465229705181): The Art of Scientific Computing, W.H. Press, S.A. Teukolsky, W.T. Vetterling and B.P. Flannery, Cambridge University Press, 2002/1993/1993.

- [Engineering Mathematics](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991019677711205181), K.A. Stroud, Macmillan, 2001. *available online*

<!-- TODO find and check if these are ok -->

## Module components

**Lectures**

2 hours per week *online*

**Tutorials**

1 hour per week *face-to-face* (see timetable)

**Homework and coursework exercise**

These will be provided *weekly* throughout the semester.

Coursework assignments are designed to give practice and reinforce the lectures. Coursework material is examinable.

## Assessment

**Examination**

On-line assessment in January.
<!-- TODO Worth ??%. -->
More details to follow.

**Summative coursework**

Two pieces of coursework <!-- TODO each worth ???% --> submitted via Gradescope.
Deadlines: <!-- TODO ??? -->

**Formative homework**

There will be weekly homework assignment sheets. These are not for credit. You can check your understanding by submitting answers via Gradescope.

## Virtual learning environment

As with all SoC  modules COMP2421 will make substantial use of the VLE:
[minerva.leeds.ac.uk](https://minerva.leeds.ac.uk)

This will include all:

- lecture notes and announcements;
- coursework/homework and (later) model solutions;
- links to external resources and web pages;
- module-related discussions

<!-- TODO teams link? -->

# Numerical algorithms

- Numerical algorithms are those which operate on *floating point numbers*.

- They are used to provide solutions (or approximations to solutions) of mathematical models of "real world" problems.

- Such problems arise in a very wide range of applications (a few examples to follow).

- An important feature of these algorithms is that they need to account for the fact that arithmetic with floating point numbers is not exact!

## Applications I: Scientific and engineering computing

::: {.container}
:::: {.col}
- Physical simulations are used for prediction in many different scientific and engineering areas.

- These models are hugely complex but also hugely important!

- Typically large physical domains are split up into small physical pieces which can be modelled more simply using techniques such as conservation laws.

<!-- - These are also dynamic models and must be solved in faster than "real time" (thus requiring enormous computing resources). -->

::::
:::: {.col}

:::::: {.r-stack}
:::::::: {.fragment .fade-in-then-out}
Airflow simulations

<a href="https://www.nektar.info/industry-relevant-implicit-les-via-spectral-hp-element-methods/"><img width="50%" alt="???" src="https://www.nektar.info/wp-content/uploads/2021/05/D1-1-811x1024.jpg"></a>
::::::::
:::::::: {.fragment .fade-in-then-out}
Economics

<a title="總統府, CC BY 2.0 &lt;https://creativecommons.org/licenses/by/2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Market_data_on_display_at_Taiwan_Stock_Exchange_20210208.jpg"><img width="100%" alt="Market data on display at Taiwan Stock Exchange 20210208" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Market_data_on_display_at_Taiwan_Stock_Exchange_20210208.jpg/512px-Market_data_on_display_at_Taiwan_Stock_Exchange_20210208.jpg"></a>
::::::::
:::::::: {.fragment .fade-in-then-out}
Weather forecasting

<a title="Mathias Krumbholz, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Lightning_Pritzerbe_01_(MK).jpg"><img width="100%" alt="Lightning Pritzerbe 01 (MK)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Lightning_Pritzerbe_01_%28MK%29.jpg/512px-Lightning_Pritzerbe_01_%28MK%29.jpg"></a>
::::::::
:::::::: {.fragment .fade-in-then-out}
Health care

<a title="From: In-silico trial of intracranial flow diverters replicates and expands insights from conventional clinical trials" href="https://www.nature.com/articles/s41467-021-23998-w"><img width="100%" alt="Workflow of the FD-PASS in-silico trial" src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-021-23998-w/MediaObjects/41467_2021_23998_Fig1_HTML.png"></a>
::::::::
::::::
::::
:::

## Applications II: High performance graphics

::: {.container}
:::: {.col}
- Realistic behaviour within games requires an accurate and efficient *physics engine*.

- Uses *Newton's laws of motion* to predict motion (e.g. projectiles, vehicles, etc) and impacts (e.g. crashes, collisions, etc).

- These are examples of dynamic models which must be solved and then rendered in "real time".
::::
:::: {.col}
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/YLsFN1mp2V8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>
Student Showcase, High Performance Graphics and Game Engineering 2021, University of Leeds
</small>
::::
:::

## Applications III: Artificial intelligence

::: {.container}
:::: {.col}
- Data mining requires complex models of very large data sets in order to extract useful information from them (e.g. Google PageRank)

- Self-driving cars, robotics and more rely on quick, accurate image processing and vision

- Much of AI boils down to *optimisation* which requires special numerical methods
::::
:::: {.col}
![](https://eps.leeds.ac.uk/images/Computing_postgraduate_researcher_Wisdom.JPG)

![](https://eps.leeds.ac.uk/eps/images/800x400_Leeds_Drone.jpg)
::::
:::
