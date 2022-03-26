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
