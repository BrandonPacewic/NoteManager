# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import subprocess

from pathlib import Path
from typing import List

from notemanager.core import NOTES_ROOT
from notemanager.lecture import Lecture
from notemanager.util import get_mega_header_body_footer, number_to_filename


class Course:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.name = path.stem
        self.lectures = sorted(
            [Lecture(file) for file in path.glob("lecture_*.tex")],
            key=lambda lecture: lecture.number
        )
        self.recitations = sorted(
            [Lecture(file) for file in path.glob("recitation_*.tex")],
            key=lambda lecture: lecture.number
        )
        self.studios = sorted(
            [Lecture(file) for file in path.glob("studio_*.tex")],
            key=lambda lecture: lecture.number
        )

        self.mega_file = path / "mega.tex"

    def update_lectures_in_mega(self) -> None:
        """
        Should only be called for courses that contain no supplemental material such as
        studio or recitation. Doing so will mess up the order that those appear in.
        """
        header, body, footer = get_mega_header_body_footer(self.mega_file)
        new_body: List[str] = []
        j = 0

        for i, line in enumerate(body):
            try:
                if int(line.split("{")[1].split("_")[1].split(
                        ".tex")[0]) > self.lectures[j].number:
                    new_body.insert(i, self.lectures[j].include_string)
                    j += 1
            except IndexError:
                # Reached a line that is not importing a lecture subfile.
                pass

            try:
                if number_to_filename(self.lectures[j].number) in line:
                    j += 1
            except IndexError:
                # All lecture files are imported in the new body.
                pass

            new_body.append(line)

        while j < len(self.lectures):
            new_body.append(self.lectures[j].include_string)
            j += 1

        header_text = "".join(header)
        body_text = "".join(new_body)
        footer_text = "".join(footer)
        self.mega_file.write_text(f"{header_text}{body_text}{footer_text}")

    def add_lecture_to_mega(self, lecture: Lecture) -> None:
        """
        Used for adding a new lecture subfile, will not mess up the rest of the mega.
        Will only add a new subfile line at the end of the body.
        """
        header, body, footer = get_mega_header_body_footer(self.mega_file)
        body.append(lecture.include_string)
        header_text = "".join(header)
        body_text = "".join(body)
        footer_text = "".join(footer)
        self.mega_file.write_text(f"{header_text}{body_text}{footer_text}")

    def compile_mega(self) -> None:
        print(f"--- Compiling {self.name} ---")
        subprocess.run(["tectonic", "-X", "compile", self.mega_file.resolve()])


class Courses(list):
    def __init__(self) -> None:
        course_directories = [
            x for x in NOTES_ROOT.iterdir() if x.is_dir() and (
                x / "mega.tex").exists()]

        courses = sorted(
            [Course(path) for path in course_directories],
            key=lambda course: course.name
        )

        list.__init__(self, courses)
