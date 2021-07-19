import sys
import os.path
import pypandoc


output = sys.argv[1]
buildir = os.path.dirname(output)
input = sys.argv[2:]

in_text = """
# Lectures

"""

for fn in input:
    html = os.path.join(fn, "index.html")
    in_text += f"\n- [{fn}]({html})"

out_text = pypandoc.convert_text(in_text, "html", format="md", extra_args=["-s"])

with open(output, "w") as f:
    f.write(out_text)
