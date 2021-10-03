import pathlib
import re
import shutil


def binstr_to_hexstr(s):
    strimmed = s.split(" ")[0]
    parts = strimmed.split(".")
    ints = [int(a, 2) for a in parts]
    hexstr = "0x" + "".join(f'{x:0>2X}' for x in ints)
    outstr = f'{strimmed} ({hexstr})'
    return outstr


if __name__ == "__main__":

    datafile = pathlib.Path("data.txt")
    bakfile = pathlib.Path("data.bak")

    with datafile.open("r", encoding="utf8") as f:
        datalines = f.readlines()

    new_datalines = [
        re.sub(
            "\d{8}\.\d{8}( \(0x[\da-fA-F]{4}\)){0,1}",
            lambda m: binstr_to_hexstr(m.group(0)),
            s
        )
        for s in datalines
    ]

    new_datastr = "".join(new_datalines)

    shutil.copy(datafile, bakfile)

    with datafile.open("w", encoding="utf8") as f:
        f.write(new_datastr)
