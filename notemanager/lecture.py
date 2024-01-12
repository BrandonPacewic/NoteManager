# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

from pathlib import Path

from notemanager.util import filename_to_number, number_to_filename


class Lecture:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file = file_path.stem
        self.filename_base = f"{file_path.stem.split('_')[0]}_"
        self.number = filename_to_number(file_path.stem, self.filename_base)

    @property
    def include_string(self) -> str:
        return r"\subfile{" + \
            number_to_filename(self.number, self.filename_base) + "}\n"
