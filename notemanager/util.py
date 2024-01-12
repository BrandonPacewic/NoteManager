# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os

from enum import Enum
from pathlib import Path
from typing import List, Tuple

from notemanager.core import OS


def get_mega_header_body_footer(
        mega_file_path: Path) -> Tuple[List[str], List[str], List[str]]:
    _Parts = Enum("Parts", ["HEADER", "BODY", "FOOTER"])
    part = _Parts.HEADER
    header, footer, body = [], [], []

    with mega_file_path.open() as file:
        for line in file:
            if part == _Parts.BODY and r"\endlectures" in line.lower():
                part = _Parts.FOOTER

            if part == _Parts.HEADER:
                header.append(line)
            elif part == _Parts.BODY:
                body.append(line)
            elif part == _Parts.FOOTER:
                footer.append(line)

            if r"\startlectures" in line.lower():
                part = _Parts.BODY

    return (header, body, footer)


def number_to_filename(number: int, filename_base: str |
                       None = "lecture_") -> str:
    return f"{filename_base}{number:02d}.tex"


def filename_to_number(filename: str, filename_base: str = "lecture_") -> int:
    return int(filename.replace(".tex", "").replace(filename_base, ""))


def copy_file(input_file: str, output_file: str) -> None:
    if OS == "Windows":
        os.system(f"copy {input_file} {output_file}")
    else:
        os.system(f"cp {input_file} {output_file}")


def link_file(input_file: str, output_file: str) -> None:
    os.system(f"ln {input_file} {output_file}")
