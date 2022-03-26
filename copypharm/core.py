import logging
from datetime import datetime

import click

import pandas as pd

from .constants import BASE_FILE_DIR
from .extractor import UrlExtractor  # analizar
from .loaders import DepartamentosLoader, FarmaciasLoader, LocalidadesLoader
from .settings import farmacias_ds

log = logging.getLogger()

data_extractors = {
    "farmacias": UrlExtractor(farmacias_ds["name"], farmacias_ds["url"]),
}


def extract_raws(date_str):
    file_paths = {}
    for name, extractor in data_extractors.items():
        file_path = extractor.extract(date_str)
        file_paths[name] = file_path
    return file_paths


def trasform_raws(date_str: str, file_paths) -> str:

    for name, extractor in data_extractors.items():
        df = pd.read_csv(file_paths[name])
        dft = extractor.transform(df)

    df = dft[dft['provincia'] == farmacias_ds['provincia']]

    df_cordoba = df[
        [
            "id",
            "nombre",
            "id_localidad",
            "id_departamento",
            "codigo_postal",
            "domicilio",
        ]
    ].set_index("id")

    df_localidades = (
        df.groupby(["id_localidad", "localidad"], as_index=False)
        .count()[["id_localidad", "localidad"]]
        .set_index("id_localidad")
    )

    df_departamentos = (
        df.groupby(["id_departamento", "nombre_departamento"], as_index=False)
        .count()[["id_departamento", "nombre_departamento"]]
        .set_index("id_departamento")
    )

    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    file_path_crib = "data/{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv"  # noqa: E501
    paths = []
    for name in ["farmacias_de_cordoba", "localidades", "departamentos"]:
        file_path = file_path_crib.format(
            category=name,
            year=date.year,
            month=date.month,
            day=date.day
        )
        f_path = BASE_FILE_DIR / file_path
        paths.append(f_path)
        f_path.parent.mkdir(parents=True, exist_ok=True)

    df_cordoba.to_csv(paths[0])
    df_localidades.to_csv(paths[1])
    df_departamentos.to_csv(paths[2])
    return paths


# : configure the command for run pipeline.
@click.command()
@click.option("--date", help="run date in format yyyy-mm-dd")
def run_pipeline(date) -> None:
    """
    Read files with data from `source <datos.gob.ar>`_.
    Create a dataframe with the data and rewrite headers format.
    Sabe all dataframes as `.csv` file.

    Parameters
    ----------
    date : str
        Path to files to be read.

    Return
    ------
    csv : str
        All `.csv` files with data.
    """
    # Extract
    log.info("Extracting")
    file_paths = extract_raws(date)

    # Transform
    log.info("Tansform")
    paths = trasform_raws(date, file_paths)

    # Load
    log.info("Loading")
    FarmaciasLoader().load_table(paths[0])
    LocalidadesLoader().load_table(paths[1])
    DepartamentosLoader().load_table(paths[2])
    # Done
    log.info("Done!")
