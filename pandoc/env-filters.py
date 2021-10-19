#!/usr/bin/env python

r"""
Pandoc filter to convert divs with latex="true" to LaTeX
environments in LaTeX output. The first class
will be regarded as the name of the latex environment
e.g.
<div latex="true" class="note abc">...</div>
will becomes
\begin{note}...\end{note}
"""

from pandocfilters import RawBlock, toJSONFilter


def latex(x):
    return RawBlock("latex", x)


Div2BeforeAfter = {
    "container": (r"\begin{columns}", r"\end{columns}"),
    "col": (r"\begin{column}{0.5\textwidth}", r"\end{column}"),
    "r-stack": (r"\alt<2>", ""),
    "fragment": (r"{", r"}"),
}


def wrapInEnvs(classes, contents):
    if classes == []:
        return contents

    try:
        before, after = Div2BeforeAfter[classes[0]]
    except KeyError:
        # if no match return none to not change ast
        return None

    wrapped = [latex(before)] + contents + [latex(after)]
    return wrapInEnvs(classes[1:], wrapped)


def latexdivs(key, value, format, _):
    if key == "Div":
        [[_, classes, _], contents] = value
        if format == "latex" or format == "beamer":
            return wrapInEnvs(classes, contents)


if __name__ == "__main__":
    toJSONFilter(latexdivs)
