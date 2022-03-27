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

import logging

import pandas as pd

from sqlalchemy import create_engine

from .constants import (
    DEPARTAMENTOS_TABLE_NAME,
    FARMACIAS_TABLE_NAME,
    LOCALIDADES_TABLE_NAME,
)
from .settings import setup_data


engine = create_engine(setup_data["SQLALCHEMY_DATABASE_URI"])
log = logging.getLogger()


class BaseLoader:
    """Base class for Load all tables in DB."""

    def load_table(self, df):
        """Read a data frame from csv file path.

        Load ``Departamentos`` table in the database from sql query.

        Parameters
        ----------
        df: ``pandas.DataFrame``
            The dataframe must with the values.

        Return
        ------
        df.to_sql : function
            A sql query such that load all values in
            the database.
        """
        return df.to_sql(
            self.table_name, con=engine, index=False, if_exists="replace"
        )


class FarmaciasLoader(BaseLoader):
    """Load *Farmacias* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='farmacias')
        The name of table.
    """

    table_name = FARMACIAS_TABLE_NAME

    def load_table(self, file_path):
        """Read a csv file from a file path and and load ``farmacias`` table.

        Load ``Farmacias`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Farmacias``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Farmacias`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df)


class LocalidadesLoader(BaseLoader):
    """Load *Localidades* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='localidades')
        The name of table.
    """

    table_name = LOCALIDADES_TABLE_NAME

    def load_table(self, file_path):
        """Read a csv file from a file path and and load ``localidades`` table.

        Load ``Localidades`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Localidades``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Localidades`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df)


class DepartamentosLoader(BaseLoader):
    """Load *Departamentos* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='departamentos')
        The name of table.
    """

    table_name = DEPARTAMENTOS_TABLE_NAME

    def load_table(self, file_path):
        """Read a csv file from a file path and load ``departamentos`` table.

        Load ``Departamentos`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Departamentos``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Departamentos`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df)
