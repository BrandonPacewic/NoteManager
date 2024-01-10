# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import configparser
import os

from notemanager.core import CONFIG_DIR, MODULE_DIR
from notemanager.util import copy_file

CONFIG_DICT: dict[str, dict[str, str]] = {
    "mega": {
        # Determines weather or not your template preamble should be linked or copied when making a new course.
        "link_preamble": "false"
    }
}


def create_default_config() -> None:
    os.makedirs(CONFIG_DIR, exist_ok=True)
    copy_file(
        os.path.join(MODULE_DIR, "config/default.ini"),
        os.path.join(CONFIG_DIR, "config.ini"),
    )


class Config:
    def __init__(self) -> None:
        self.config_path = os.path.join(CONFIG_DIR, "config.ini")

        if not os.path.isfile(self.config_path):
            create_default_config()

        self.config = configparser.ConfigParser()
        self.config.read_dict(CONFIG_DICT)
        self.config.read(self.config_path)

    def get(self, section: str, option: str) -> str:
        return self.config.get(section, option)


CONFIG = Config()
