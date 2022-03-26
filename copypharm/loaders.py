# !/usr/bin/env python
# -*- coding: utf-8 -*-

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
    def load_table(self, df):
        df.to_sql(
            self.table_name, con=engine, index=False, if_exists="replace"
        )


class FarmaciasLoader(BaseLoader):
    table_name = FARMACIAS_TABLE_NAME

    def load_table(self, file_path):
        df = pd.read_csv(file_path)
        return super().load_table(df)


class LocalidadesLoader(BaseLoader):
    table_name = LOCALIDADES_TABLE_NAME

    def load_table(self, file_path):
        df = pd.read_csv(file_path)
        return super().load_table(df)


class DepartamentosLoader(BaseLoader):
    table_name = DEPARTAMENTOS_TABLE_NAME

    def load_table(self, file_path):
        df = pd.read_csv(file_path)
        return super().load_table(df)
