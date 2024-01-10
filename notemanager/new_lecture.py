# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import sys

from pathlib import Path
from typing import List

from notemanager.core import MODULE_DIR
from notemanager.courses import Course
from notemanager.lecture import Lecture
from notemanager.util import copy_file, lecture_number_to_filename


def main(args: List[str] = sys.argv[1:]) -> None:
    if len(args) > 1:
        print("Help: new_lecture <dir of course for the lecture>")
        sys.exit(1)

    if len(args):
        course_path = args[0]
    else:
        course_path = os.getcwd()

    course = Course(Path(course_path))
    lecture_filename = lecture_number_to_filename(len(course.lectures) + 1)
    copy_file(
        f"{MODULE_DIR}/templates/lecture_xx.tex",
        f"{course_path}/{lecture_filename}",
    )

    lecture = Lecture(Path(f"{course_path}/{lecture_filename}"))
    course.add_lecture_to_mega(lecture)


if __name__ == "__main__":
    main()
