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
from pathlib import Path

BASE_FILE_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
ROOT_DIR = Path().resolve().parent

SQL_DIR = Path("sql")

DEPARTAMENTOS_TABLE_NAME = "departamentos"
LOCALIDADES_TABLE_NAME = "localidades"
FARMACIAS_TABLE_NAME = "farmacias"

TABLE_NAMES = [
    DEPARTAMENTOS_TABLE_NAME,
    LOCALIDADES_TABLE_NAME,
    FARMACIAS_TABLE_NAME,
]
