# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import sys

from typing import List

import notemanager.new_lecture

from notemanager.core import MODULE_DIR, NOTES_ROOT
from notemanager.config import CONFIG
from notemanager.courses import Course
from notemanager.util import copy_file, link_file


def main(args: List[str] = sys.argv[1:]) -> None:
    if not len(args) or len(args) > 1:
        print("Help: new_course <name of new course to make>")
        sys.exit(1)

    course_name = args[0].strip()
    os.makedirs(f"{NOTES_ROOT}/{course_name}", exist_ok=True)

    if CONFIG.get("main", "link_preamble") == "true":
        link_file(
            f"{MODULE_DIR}/templates/preamble.tex",
            f"{NOTES_ROOT}/{course_name}/"
        )
    else:
        copy_file(
            f"{MODULE_DIR}/templates/preamble.tex",
            f"{NOTES_ROOT}/{course_name}/"
        )

    copy_file(
        f"{MODULE_DIR}/templates/mega.tex",
        f"{NOTES_ROOT}/{course_name}/"
    )

    notemanager.new_lecture.main([f"{NOTES_ROOT}/{course_name}"])


if __name__ == "__main__":
    main()
