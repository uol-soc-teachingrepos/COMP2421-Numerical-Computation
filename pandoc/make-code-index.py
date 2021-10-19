import os.path
import re
import sys

import pypandoc


def filename2content(filename):
    ret = "```python\n"
    with open(filename) as f:
        for line in f.readlines():
            func_match = re.match(r"^def ([^\(]+)", line)
            if func_match is not None:
                id = func_match.group(1)
                ret += f"```\n<a id='{id}'></a>\n```python\n"
            ret += line

        # ret += "".join(f.readlines())

    ret += f"```\n"

    return ret


output = sys.argv[1]
input = sys.argv[2]
basename = os.path.relpath(".", os.path.dirname(input))

in_text = f"""
---
title: {input}
basename: {basename}
---

"""

in_text += filename2content(input)

out_text = pypandoc.convert_text(
    in_text,
    "html",
    format="md",
    extra_args=[
        "--template=./pandoc/html-template.html",
        "--mathjax",
        "--no-highlight",
        "--standalone",
    ],
)

with open(output, "w") as f:
    f.write(out_text)
