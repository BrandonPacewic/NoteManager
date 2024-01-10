# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

from notemanager.courses import Courses


def main() -> None:
    for course in Courses():
        course.compile_mega()


if __name__ == "__main__":
    main()
