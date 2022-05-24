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
