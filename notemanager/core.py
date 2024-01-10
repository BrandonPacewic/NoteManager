# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import platform

from pathlib import Path

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CONFIG_DIR = os.getenv("XDG_CONFIG_HOME", os.path.join(HOME, ".config"))

CONFIG_DIR = os.path.join(XDG_CONFIG_DIR, "notemanager")
NOTES_ROOT = Path("~/Documents/Repos/Notes/OSU/").expanduser()
MODULE_DIR = os.path.dirname(__file__)

OS = platform.uname()[0]
