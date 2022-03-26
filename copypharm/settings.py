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
