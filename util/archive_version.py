from pathlib import Path
import sys


SCRIPT_LINE = '  <script src="https://seaborn.pydata.org/versionwarning.js"></script>\n'


if __name__ == "__main__":

    p = Path("archive") / sys.argv[1]
    paths = p.rglob("*.html")
    for path in paths:
        with path.open() as fid:
            old_lines = fid.readlines()
        new_lines = []
        for line in old_lines:
            if "</body>" in line:
                new_lines.append(SCRIPT_LINE)
            new_lines.append(line)
        with path.open("w") as fid:
            fid.write("".join(new_lines))