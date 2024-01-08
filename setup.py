# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import setuptools
import sys

try:
    import notemanager 
except ImportError:
    print("Error importing notemanager.")
    sys.exit(1)

LONG_DESCRIPTION = open("README.md").read()
VERSION = notemanager.__VERSION__


def main() -> None:
    setuptools.setup(
        name="notemanager",
        version=VERSION,
        author="Brandon Pacewic",
        description="A LaTex note manager.",
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        license="MIT",
        url="https://github.com/BrandonPacewic/NoteManager",
        packages=["notemanager"],
        entry_points={
            "console_scripts": [
                "notemanager=nmg.__main__:main",
            ]
        },
        python_requires=">=3.6",
        include_package_data=True,
    )


if __name__ == "__main__":
    main()
