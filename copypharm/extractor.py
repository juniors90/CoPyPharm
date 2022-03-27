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
from datetime import datetime

import pandas as pd

import requests

from .constants import BASE_FILE_DIR

log = logging.getLogger()


class UrlExtractor(object):
    """Collapse your data into a single data frame.

    Parameters
    ----------
    name: str
        The name of data (in this case, pharmacies) to extract.
    url : str
        Describe the url such that allows then data.

    Return
    ------
        An instance of ``UrlExtractor`` containing two methods named
        ``extract()`` and ``trasform()`` for all the information of
        pharmacies in Córdoba.

    Examples
    --------
    >>> from copypharm import UrlExtractor
    >>> name="farmacias"
    >>> url="http://datos.salud.gob.ar/dataset\
             /39117f8f-e2bc-4571-a572-15a6ce7ea9e1\
             /resource/19338ea7-a492-4af3-b212-18f8f4af9184\
             /download/establecimientos-farmacias-enero-2021.csv"
    >>> url_extractor=UrlExtractor(name=name, url=url)
    >>> url_extractor.__repr__()
    '<Extractor for Name: farmacias, URL: <long_url>>'
    >>> import pandas as pd
    >>> path_to_csv = url_extractor.extract(date_str="2022-03-27")
    >>> path_to_csv
    PosixPath('/path/to/project/copypharm/data/farmacias/2022-03/farmacias-27-03-2022.csv')
    >>> df = pd.read_csv(path_to_csv)
    >>> url_extractor.transform(df)
                       id  ...  web
    0      70260072329721  ...  NaN
    1      70100352324743  ...  NaN
    2      70064412318286  ...  NaN
    3      70340492347884  ...  NaN
    4      70140142334991  ...  NaN
    ...               ...  ...  ...
    13672  70460212355713  ...  NaN
    13673  70421472354613  ...  NaN
    13674  70940142195567  ...  NaN
    13675  70420702154608  ...  NaN
    13676  70064272320083  ...  NaN

    [13677 rows x 11 columns]
    >>>
    """

    file_path_crib = "data/{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv"  # noqa: E501

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def __repr__(self) -> None:
        """Print a representation of your object."""
        extractor = "<Extractor for Name: {name}, URL: {url}>"
        return extractor.format(name=self.name, url=self.url)

    def extract(self, date_str: str) -> str:
        """Extract your data into a single csv file.

        Inspect the ``.csv`` and extract with data related
        whit pharmmacies.

        Parameters
        ----------
        date_str : str
            The date on run with format YYYY-mm-dd.

        Return
        ------
            file_path : str
                The destination location for your csv file.
        """
        log.info(f"Extracting {self.name}")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        file_path = self.file_path_crib.format(
            category=self.name, year=date.year, month=date.month, day=date.day
        )

        pharm_path = BASE_FILE_DIR / file_path
        pharm_path.parent.mkdir(parents=True, exist_ok=True)

        r = requests.get(self.url)
        r.encoding = "utf-8"

        log.info(f"Storing file in {pharm_path}")

        with open(pharm_path, "w") as f:
            f.write(r.text)

        return pharm_path

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trasform your data into a single data frame.

        Inspect the ``df`` and renamed the columns with data related
        whit pharmmacies.

        Parameters
        ----------
        df : ``pandas.DataFrame``
            Dataframe containing all data over pharmacies
            parameters of each cell.

        Return
        ------
            df : pd.DataFrame
                An instance of ``pd.DataFrame`` containing all the
                information of pharmacies.
        """
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
