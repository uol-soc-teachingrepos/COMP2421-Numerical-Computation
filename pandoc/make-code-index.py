import sys
import os.path
import pypandoc


def filename2content(filename):
    ret = "```python\n"
    with open(filename) as f:
        ret += "".join(f.readlines())

    ret += f"```\n"

    return ret


output = sys.argv[1]
input = sys.argv[2]

in_text = f"""
---
title: {input}
---

"""

in_text += filename2content(input)

out_text = pypandoc.convert_text(
    in_text,
    "html",
    format="md",
    extra_args=[
        "-s",
        "--template=./pandoc/html-template.html",
        "--no-highlight",
        '-V basename="public"',
    ],
)

with open(output, "w") as f:
    f.write(out_text)
