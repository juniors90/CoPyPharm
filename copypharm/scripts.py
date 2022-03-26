import logging

from sqlalchemy import create_engine
from sqlalchemy.sql import text

from .constants import SQL_DIR, TABLE_NAMES
from .settings import setup_data

engine = create_engine(setup_data["SQLALCHEMY_DATABASE_URI"])
log = logging.getLogger()

query1 = """ALTER TABLE `farmacias`
            ADD FOREIGN KEY (id_localidad)
            REFERENCES localidades (id_localidad);
        """

query2 = """ALTER TABLE `farmacias`
            ADD FOREIGN KEY (id_departamento)
            REFERENCES departamentos (id_departamento);
        """


def create_table():
    with engine.connect() as conn:
        for file in TABLE_NAMES[0:3]:
            log.info(f"create table {file}")
            with open(SQL_DIR / f"{file}.sql") as f:
                query = text(f.read())

            conn.execute(f"DROP TABLE IF EXISTS {file};")
            conn.execute(query)

        conn.execute(query1)
        conn.execute(query2)


if __name__ == "__main__":
    create_table()
