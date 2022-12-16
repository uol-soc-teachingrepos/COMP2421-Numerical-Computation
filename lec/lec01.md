# Lecture 01: Module introduction

### Module objectives

- Understand how to compute with vectors and matrices.
- Appreciate the role numerical computation plays in CS.
- Choose a computational model appropriately, accounting for issues of accuracy, reliability and efficiency.
- Understand how to assess or measure the error in a numerical algorithm and be familiar with how such errors are controlled.
- Understand the fundamental techniques for the design of efficiency numerical algorithms.
- Demonstrate how these algorithms are analysed.
- Understand several advanced data structures, their efficient implementation and applications.
- Understand how these algorithms and data structures relate to the central practical problems of modern computer science.

### Syllabus

- **Vectors and matrices**: introduction and justification; vector and matrix operations; identity matrix; inverse of a matrix.

- **Approximation and errors**: modelling and mathematical modelling; discrete and continuous models; floating point and rounding errors; balancing accuracy and efficiency.

- **Static systems**: iterative methods for solving nonlinear scalar equations; methods for solving linear systems of equations; systems without unique solutions.

- **Evolving systems**: derivatives and rates of change; initial value problems; stability and convergence of computer models.

## Numerical computation

All administration details in the [module handbook](https://comp2421-numerical-computation.gitlab.io/book).

### Contact

- Please contact me through MS Teams [22/23(1) COMP2421 Numerical Computation (32879)](https://teams.microsoft.com/l/team/19%3aMD-x6E4QiyZ3S1zNFHomIWxtG3UJiRimjR_RzgapA7g1%40thread.tacv2/conversations?groupId=54035a7f-8376-45f0-b7b8-d4fac9d5ab54&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb) (not email)
- Questions about content should go in the class team
- Responses in 24h (or out of office)
- No response out of working hours

### How to succeed?

- Read lecture notes **before lectures** -- [all available](https://comp2421-numerical-computation.gitlab.io/book/)
- Turn up to lectures with **pen and paper**
- Attempt **worksheet** before tutorial
- Let tutorial leader know where you are having problems before the session
- Attend tutorial every week - ask questions

### How to get 100%?

**Exam profile last year:**

![**No one gets 100%**](../img/lec01/gradescope.png)

---

```{table} Summary of marking expectations
| Mark   | Demonstrate                                    |
|--------|------------------------------------------------|
| 40-50% | Apply all algorithms                           |
| 50-60% | Apply modifications of algorithms              |
| 60-70% | Know how to explore algorithms computationally |
| 70%+   | Understand why algorithms are good/bad         |
| 95%+   | Read and write research papers in this area    |
```

### Python

The programming for this module will be carried out using `python3`.

The latest available version of python is available via [Anaconda](https://www.anaconda.com/products/distribution).

Anaconda provides a full scientific Python distribution, including as standard tools for numerical analysis, data visualisation, image processing, and much more!

This scientific Python distribution is available on all School of Computing machines, specifically all SoC Linux computers.

On a SoC Linux computer, you can run
```sh
> module load legacy-eng # This step may be removed in future
> module add anaconda3/2020.11
```
and you can test your python version with
```sh
> python --version
Python 3.8.5
```

Alternatively, you can install anaconda python on your own machine.

> Try this yourself! Make sure you can access a working version of python (version >= 3.6) and can import `numpy` and `scipy`.

More help will be given with python programming throughout the course.

### Relevance to Level 1 modules

This module builds upon material that you have already met in your first year. Prerequisites include:

- **COMP1421** Fundamental mathematical concepts
- **COMP1721** Object oriented programming

We also add to some of the material from:

- **COMP1212** Computer processors

### Relevance to Level 2 and 3 modules

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

### Books

Additional useful texts

- [Introduction to Linear Algebra](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991011421399705181) (Fifth Edition), Gilbert Strang, Wellesley-Cambridge Press, 2016. \
  with [MIT course material](https://web.mit.edu/18.06/www)

- [Scientific Computing: An Introductory Survey](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991009203099705181), T.M. Heath, McGraw-Hill, 2002. \
  some [lecture notes based on the book](http://heath.cs.illinois.edu/scicomp/notes/index.html)

- [Numerical Recipes in C++/C/FORTRAN](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991010465229705181): The Art of Scientific Computing, W.H. Press, S.A. Teukolsky, W.T. Vetterling and B.P. Flannery, Cambridge University Press, 2002/1993/1993.

- [Engineering Mathematics](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991019677711205181), K.A. Stroud, Macmillan, 2001. *available online*

Further more specific references will be given in each section of the notes.

## Module components

### Lectures

2 hours per week in this room.

Thursday 12:00-13:00 | Friday 11:00-12:00

Leeds content delivered by Tom Ranner and Yongxing Wang.

Chengdu content delivered by Zhiguo Long.

### Tutorials

1 hour per week (see timetable for your session)

Please attempt the worksheet before the session and bring your attempts with you!

Opportunity for **feedback** on learning.

### Homework and coursework exercise

These will be provided *weekly* throughout the semester.

Coursework assignments are designed to give practice and reinforce the lectures. Coursework material is examinable.

### Virtual learning environment

As with all SoC  modules COMP2421 will make substantial use of the VLE:
[minerva.leeds.ac.uk](https://minerva.leeds.ac.uk)

This will include all:

- lecture notes and announcements;
- coursework/homework and (later) model solutions;
- links to external resources and web pages;
- module-related discussions

Further support via [MS Team](https://teams.microsoft.com/l/team/19%3aMD-x6E4QiyZ3S1zNFHomIWxtG3UJiRimjR_RzgapA7g1%40thread.tacv2/conversations?groupId=54035a7f-8376-45f0-b7b8-d4fac9d5ab54&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb). Please use the class team for all questions about content.

## Assessment

### Examination

Computer exam in January.
Worth 60%.
More details to follow - see [Lecture 20](./lec20.md) for details.

*Edit: exam type changed - please follow updated guidance*


### Summative coursework

Two pieces of coursework each worth 20% submitted via Gradescope.
The dates are tentative at this stage and are subject to change.

**Feedback** given in tutorial sessions and written group feedback.

```{table} Summative coursework timetable

| Coursework | Date set | Submission deadline | Feedback date |
|------------|----------|---------------------|---------------|
| 1          | 17/10/22 | 8/11/22             | 22/11/22      |
| 2          | 28/11/22 | 13/12/22            | early 23      |

```

### Formative homework

There will be weekly homework assignment sheets. These are not for credit.

## Numerical algorithms

- Numerical algorithms are those which operate on *floating point numbers*.

- They are used to provide solutions (or approximations to solutions) of mathematical models of "real world" problems.

- Such problems arise in a very wide range of applications (a few examples to follow).

- An important feature of these algorithms is that they need to account for the fact that arithmetic with floating point numbers is not exact!

### Applications I: Scientific and engineering computing

- Physical simulations are used for prediction in many different scientific and engineering areas.

- These models are hugely complex but also hugely important!

- Typically large physical domains are split up into small physical pieces which can be modelled more simply using techniques such as conservation laws.

**Airflow simulations**

Car manufacturer and motor spots teams often perform computer simulations to test and optimise new designs.

<video width="100%" controls>
	<source src="../_static/video/lec01/LES.webm" type="video/mp4">
	<a href="https://www.nektar.info/industry-relevant-implicit-les-via-spectral-hp-element-methods/"><img width="50%" alt="Airflow simulation example" src="https://www.nektar.info/wp-content/uploads/2021/05/D1-1-811x1024.jpg"></a>
</video>

<small>
Video source: <https://youtu.be/-4gSS-UHWcc>
</small>

- Gianmarco Mengaldo, [Industry-relvant implicit LES via spetal/hp element methods](https://www.nektar.info/industry-relevant-implicit-les-via-spectral-hp-element-methods/)

**Economics**

Most modern day economic forecasting involves performing numerical simulations.

<a title="Negative Space - Pexels account, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Blur-chart-data-69760.jpg"><img width="100%" alt="Blur-chart-data-69760" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Blur-chart-data-69760.jpg/512px-Blur-chart-data-69760.jpg"></a>

- Saul H. Hymans, [Forcasting and econometric models](https://www.econlib.org/library/Enc/ForecastingandEconometricModels.html)

**Weather forecasting**

One of the most popular applications of numerical simulation in the UK today is in predicting tomorrow's weather.

<video width="100%" muted controls>
	<source src="../_static/video/lec01/weather.webm" type="video/mp4">
	<a title="Mathias Krumbholz, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Lightning_Pritzerbe_01_(MK).jpg"> <img width="100%" alt="Lightning Pritzerbe 01 (MK)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Lightning_Pritzerbe_01_%28MK%29.jpg/512px-Lightning_Pritzerbe_01_%28MK%29.jpg"></a>
</video>

<small>
	Video source: <https://youtu.be/5kpw5WeR5V4>
</small>

- Met office, [How weather forecasts are created](https://www.metoffice.gov.uk/weather/learn-about/how-forecasts-are-made)
- Met office, [Climate modelling](https://www.metoffice.gov.uk/weather/climate/science/climate-modelling)

**Health care**

Many different areas of medicine now use simulations. This can be used both as an earlier step in clinical trials in order to reduce harm to animal or human participants or to predict how medical interventions will work in practice.

<video width="100%" controls>
	<source src="../_static/video/lec01/in-silico.mp4" type="video/mp4">
	<img width="100%" alt="Workflow of the FD-PASS in-silico trial" src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-021-23998-w/MediaObjects/41467_2021_23998_Fig1_HTML.png">
</video>

- Wikipedia: [*In silico* clinical trials](https://en.wikipedia.org/wiki/In_silico_clinical_trials)
- Sarrami-Foroushani *et al.*, [In-silico trial of intracranial flow diverters replicates and expands insights from conventional clinical trials](https://doi.org/10.1038/s41467-021-23998-w). Nat Commun 12, 3861 (2021).

### Applications II: High performance graphics

- Realistic behaviour within games requires an accurate and efficient *physics engine*.

- Uses *Newton's laws of motion* to predict motion (e.g. projectiles, vehicles, etc) and impacts (e.g. crashes, collisions, etc).

- These are examples of dynamic models which must be solved and then rendered in "real time".

 <video width="100%" muted>
  <source src="../_static/video/lec01/HPG.webm" type="video/mp4" >
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/YLsFN1mp2V8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen data-external="1"></iframe>
</video>

<small>
Student Showcase, High Performance Graphics and Game Engineering 2021, University of Leeds
</small>

- Wikipedia: [Physics engine](https://en.wikipedia.org/wiki/Physics_engine)
- David M Bourg, [How physics is used in video games](https://doi.org/10.1088/0031-9120/39/5/002), Physics Education, issue 39, 2004.

### Applications III: Artificial intelligence

- Data mining requires complex models of very large data sets in order to extract useful information from them (e.g. Google PageRank)

- Self-driving cars, robotics and more rely on quick, accurate image processing and vision

- Much of AI boils down to *optimisation* which requires special numerical methods

 [Why studying Linear Algebra is important for Machine Learning and where to start](https://www.univ.ai/post/linear-algebra-machine-learning-prerequisites)

**Robotics at Leeds**

Many tasks in robotics are tested first in simulated environments where simulation plays a key role.

[![Robotics at Leeds](https://eps.leeds.ac.uk/images/Computing_postgraduate_researcher_Wisdom.JPG)](https://robotics.leeds.ac.uk/)

**Pipebots**

<video width="100%" muted>
	<source src="../_static/video/lec01/pipebots.webm" type="video/mp4">
</video>

<small>
Video source: <https://youtu.be/pppxa9MpoeY>
</small>

## Further reading

- Met office, [How weather forecasts are created](https://www.metoffice.gov.uk/weather/learn-about/how-forecasts-are-made)
- Met office, [Climate modelling](https://www.metoffice.gov.uk/weather/climate/science/climate-modelling)
- Saul H. Hymans, [Forcasting and econometric models](https://www.econlib.org/library/Enc/ForecastingandEconometricModels.html)
- Wikipedia: [Physics engine](https://en.wikipedia.org/wiki/Physics_engine)
- David M Bourg, [How physics is used in video games](https://doi.org/10.1088/0031-9120/39/5/002), Physics Education, issue 39, 2004.
- [Why studying Linear Algebra is important for Machine Learning and where to start](https://www.univ.ai/post/linear-algebra-machine-learning-prerequisites)
