# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import sys

from pathlib import Path
from typing import List

from notemanager.core import MODULE_DIR
from notemanager.config import CONFIG
from notemanager.util import copy_file, link_file


def main(args: List[str] = sys.argv[1:]) -> None:
    if not len(args) or len(args) > 1:
        print("Help: new_standalone <name of new standalone file>")
        sys.exit(1)

    standalone_name = args[0].strip()

    if not standalone_name.endswith(".tex"):
        standalone_name += ".tex"

    print(os.getcwd())
    path = Path(os.getcwd())

    if (path / standalone_name).exists():
        print("File already exists")
        sys.exit(1)

    copy_file(
        f"{MODULE_DIR}/templates/standalone.tex",
        f"{os.getcwd()}/{standalone_name}"
    )

    print("Here 2")

    if not (path / "preamble.tex").exists():
        if CONFIG.get("main", "link_preamble") == "true":
            link_file(
                f"{MODULE_DIR}/templates/preamble.tex",
                os.getcwd()
            )
        else:
            copy_file(
                f"{MODULE_DIR}/templates/preamble.tex",
                os.getcwd()
            )


if __name__ == "__main__":
    main()
