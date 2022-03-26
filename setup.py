#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   CoPyPharm Project (https://github.com/juniors90/CoPyPharm/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/CoPyPharm/blob/master/LICENSE

# =====================================================================
# DOCS
# =====================================================================

"""This file is for distribute and install CoPyPharm"""

# ======================================================================
# IMPORTS
# ======================================================================

import os
import pathlib

from setuptools import setup  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


REQUIREMENTS = [
    "mysql-connector-python==8.0.28",
    "pandas==1.3.5",
    "requests==2.27.1",
    "sqlalchemy==1.4.32",
]

with open(PATH / "copypharm" / "__init__.py") as fp:
    for line in fp.readlines():
        if line.startswith("__version__ = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()


source = "https://github.com/juniors90/CoPyPharm"
tracker = "https://github.com/juniors90/CoPyPharm/issues"
donate = "https://www.paypal.com/donate?hosted_button_id=LFAQ7E7TJ4HSY"
funding = "https://paypal.me/juniors90"


# =============================================================================
# FUNCTIONS
# =============================================================================

setup(
    name="CoPyPharm",
    version=VERSION,
    description="An extension that registers all pharmacies in Córdoba - Argentina.",  # noqa: E501
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Ferreira Juan David",
    author_email="juandavid9a0@gmail.com",
    url="https://github.com/juniors90/CoPyPharm",
    packages=["copypharm"],
    include_package_data=True,
    platforms="any",
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["Pharmacies", "Argentina", "Data Science"],
    project_urls={
        "Source": source,
        "Tracker": tracker,
        "Donate": donate,
        "Funding": funding,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
