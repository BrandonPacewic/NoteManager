# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

from enum import Enum
from pathlib import Path
from typing import List, Tuple


def get_mega_header_body_footer(
        mega_file_path: Path) -> Tuple[List[str], List[str], List[str]]:
    _Parts = Enum("Parts", ["HEADER", "BODY", "FOOTER"])
    part = _Parts.HEADER
    header, footer, body = [], [], []

    with mega_file_path.open() as file:
        for line in file:
            if part == _Parts.BODY and r"\Endlectures" in line:
                part = _Parts.FOOTER

            if part == _Parts.HEADER:
                header.append(line)
            elif part == _Parts.BODY:
                body.append(line)
            elif part == _Parts.FOOTER:
                footer.append(line)

            if r"\Startlectures" in line:
                part = _Parts.BODY

    return (header, body, footer)


def lecture_number_to_filename(number: int) -> str:
    return f"lecture_{number:02d}.tex"


def lecture_filename_to_number(filename: str) -> int:
    return int(filename.replace(".tex", "").replace("lecture_", ""))
