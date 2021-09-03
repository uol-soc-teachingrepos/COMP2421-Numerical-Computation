# Prerequisites

To get started you need the dependencies listed in the `environment.yml` file:

- make
- pandoc
- python
- pypandoc
- git lfs
- livereload (optional - for test serving content)

This can be easily done with `conda env create -f environment.yml`.

# Getting the content

To build the slides call
```
make build
```

This generates all content in the public directory using the source in `lec/` with the template in `pandoc/revealjs-template.html` using the rules in `Makefile`

For each lecture provides:

- `lec/lecXX.html` - version of the slides aimed at students.
- `lec/lecXX.full.html` - version of the slides for presenting. They *should* work offline.
- `lec/lecXX.md` - the markdown source file.

An online compiled version of the `public` directory is available at:
https://comp2421_numerical-computation.gitlab.io/slides
