# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import argparse
import os
import sys

from pathlib import Path

from notemanager.core import MODULE_DIR
from notemanager.courses import Course
from notemanager.lecture import Lecture
from notemanager.util import copy_file, number_to_filename


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", nargs="?")
    parser.add_argument("--directory", "-d", nargs="?")
    args = parser.parse_args()

    if args.directory:
        course_path = args.directory
    else:
        course_path = os.getcwd()

    if args.name:
        new_filename_base = f"{args.name}_"
    else:
        new_filename_base = "lecture_"

    course = Course(Path(course_path))
    try:
        sources = getattr(course, f"{new_filename_base[:-1]}s")
    except AttributeError:
        print("You mistyped your filename.")
        sys.exit(1)

    assert isinstance(sources, list)
    lecture_filename = number_to_filename(len(sources) + 1, new_filename_base)
    copy_file(
        f"{MODULE_DIR}/templates/lecture_xx.tex",
        f"{course_path}/{lecture_filename}",
    )

    lecture = Lecture(Path(f"{course_path}/{lecture_filename}"))
    course.add_lecture_to_mega(lecture)


if __name__ == "__main__":
    main()
