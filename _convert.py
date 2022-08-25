import re
from glob import glob


def change_string_in_file(filename: str, old_string: str, new_string: str):
    """Replaces old_string with new_string from filename and saves the result to that file"""
    with open(filename) as f:
        content = f.read()

    if old_string not in content:
        return

    with open(filename, "w") as f:
        content = content.replace(old_string, new_string)
        f.write(content)


def replace_regex_in_file(filename: str, regex: str, replacement):
    # _regex = re.compile(regex)

    with open(filename) as f:
        content = f.read()

    # if not _regex.match(content):
    #     return

    with open(filename, "w") as f:
        new_content = re.sub(regex, replacement, content)
        f.write(new_content)


files = glob("./_build/html/**/*html", recursive=True)

for file in files:
    change_string_in_file(file, "fa-github", "fa-gitlab")
    replace_regex_in_file(
        file,
        r"new\?title=([^&]*)&body=([^&]*)",
        r"new\?issue[title]=\g<1>&issue[description]=\g<2>",
    )


ws_files = glob("./_build/html/ws/*html", recursive=True)

for filename in ws_files:
    if '00' in filename:
        continue

    try:
        ws_number = re.findall(r'\d+', filename)[0]
    except IndexError:
        print(filename)
        continue
    ws_filename = f"ws%2Fws{ws_number}.ipynb"

    with open(filename, "r") as f:
        lines = f.readlines()
        for j, line in enumerate(lines):
            if '<div class="header-article__right">' in line:
                lines.insert(j+1, f'<a class="reference external" href="https://mybinder.org/v2/gl/comp2421-numerical-computation%2Fbook/master?labpath={ws_filename}" target="_blank" rel="noopener noreferrer"><img alt="Launch binder" src="https://mybinder.org/badge_logo.svg" /></a>\n\n')
                break

    with open(filename, "w") as f:
        f.write(''.join(lines))


