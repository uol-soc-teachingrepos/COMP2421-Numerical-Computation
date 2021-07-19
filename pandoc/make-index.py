import sys
import os.path
import pypandoc


output = sys.argv[1]
input = sorted(sys.argv[2:])

in_text = """
# Lectures

"""

for fn in input:
    lec = os.path.splitext(fn)[0]
    html = os.path.join(lec, "index.html")
    in_text += f"\n- [{lec}]({html})"

out_text = pypandoc.convert_text(in_text, "html", format="md", extra_args=["-s"])

with open(output, "w") as f:
    f.write(out_text)
