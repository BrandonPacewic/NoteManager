# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

from pathlib import Path

from notemanager.util import lecture_filename_to_number, lecture_number_to_filename


class Lecture:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file = file_path.stem
        self.number = lecture_filename_to_number(file_path.stem)

    @property
    def include_string(self) -> str:
        return r"\subfile{" + lecture_number_to_filename(self.number) + "}\n"
