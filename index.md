---
author:
- name: Tom Ranner
  address: School of Computing, University of Leeds, UK
  email: T.Ranner@leeds.ac.uk
  with: others
title: Talk title
logos:
- source: ./img/Leeds_Logo.svg
  alt: University of Leeds
- source: ./img/EPSRC.png
  alt: EPSRC
- source: ./img/leverhulme-black.svg
  alt: Leverhulme Trust
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
bibliography: ./bib/library.bibtex
csl: ./bib/ima.csl
reference-section-title: References
link-citations: true
---
# Section 1

## Slide title

slide text

## Second slide with maths

$$
a = b + c
$$

$$
\begin{align}
u_t-\Delta_\Gamma u &=f && \mbox{ on }\Gamma \times [0,T] \\
u(0) & = u_0 && \mbox{ on } \Gamma.
\end{align}
$$

## Third slide with inline code

Special code word `git`
