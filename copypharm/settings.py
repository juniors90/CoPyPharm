# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the CoPyPharm Project
#     https://github.com/juniors90/CoPyPharm.
#
# Copyright (c) 2022. Ferreira Juan David
# License: MIT
#   Full Text: https://github.com/pyCellID/CoPyPharm/blob/main/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""
CoPyPharm.

An extension that registers all pharmacies in Córdoba - Argentina.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import os
from configparser import ConfigParser

# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=["="])

path = "/".join((os.path.abspath(__file__).replace("\\", "/")).split("/")[:-1])
config.read(os.path.join(path, "settings.ini"))

cfg = config["DEFAULT"]

cfg_data = "SQLALCHEMY_DATABASE_URI URL_FARMACIAS".split()

setup_data = {o: cfg[o] for o in cfg_data}

farmacias_ds = {
    "name": "farmacias",
    "url": cfg["URL_FARMACIAS"],
    "provincia": cfg["PROVINCIA"],
}
