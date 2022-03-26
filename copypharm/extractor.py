# !/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

import pandas as pd

import requests

from .constants import BASE_FILE_DIR

log = logging.getLogger()


class UrlExtractor:
    file_path_crib = "data/{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv"  # noqa: E501

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def extract(self, date_str: str) -> str:

        log.info(f"Extracting {self.name}")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        file_path = self.file_path_crib.format(
            category=self.name, year=date.year, month=date.month, day=date.day
        )

        b_path = BASE_FILE_DIR / file_path
        b_path.parent.mkdir(parents=True, exist_ok=True)

        r = requests.get(self.url)
        r.encoding = "utf-8"

        log.info(f"Storing file in {b_path}")

        with open(b_path, "w") as f:
            f.write(r.text)

        return b_path

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        renamed_cols = {
            "establecimiento_id": "id",
            "establecimiento_nombre": "nombre",
            "localidad_id": "id_localidad",
            "localidad_nombre": "localidad",
            "provincia_id": "id_provincia",
            "provincia_nombre": "provincia",
            "departamento_id": "id_departamento",
            "departamento_nombre": "nombre_departamento",
            "cod_loc": "cod_localidad",
            "tipologia_id": "id_tipologia",
            "tipologia_nombre": "nombre_tipologia",
            "cp": "codigo_postal",
            "sitio_web": "web",
        }

        df = df.rename(columns=renamed_cols)

        cols = [
            "id",
            "nombre",
            "id_localidad",
            "localidad",
            "id_provincia",
            "provincia",
            "id_departamento",
            "nombre_departamento",
            "codigo_postal",
            "domicilio",
            "web",
        ]

        df = df[cols]

        return df
