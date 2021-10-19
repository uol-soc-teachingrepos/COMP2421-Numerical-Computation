import os.path
import sys

import pypandoc


def dirname2content(filename: str) -> str:
    fn, _ = os.path.splitext(filename)
    dirname = os.path.basename(fn)
    lecnumber = int(dirname[3:])
    index = fn + ".html"
    embed = index
    # dirname = os.path.basename(filename)
    # index = os.path.join(dirname, "index.html")
    # embed = os.path.join(dirname, "embed.html")

    ret = f"## Lecture {lecnumber}\n\n"

    ret += f"""
<div style="position:relative;padding-top:66%;">
<iframe src="{embed}" frameborder="0" allowfullscreen
style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe>
</div>
    """

    ret += f'\n\n<a href="{index}">Full screen</a>\n'

    return ret


if len(sys.argv) == 1:
    print("WARNING: no filenames passed")
    sys.exit(0)

output = sys.argv[1]
input = sorted(sys.argv[2:])

in_text = """
---
title: COMP2421 Numerical Computation
---
# Lectures

"""

for fn in input:
    in_text += dirname2content(fn)
    in_text += "\n\n"

out_text = pypandoc.convert_text(in_text, "html", format="md", extra_args=["-s"])

with open(output, "w") as f:
    f.write(out_text)
