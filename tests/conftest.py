import os

import numpy as np
import pytest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
base = os.path.dirname(ROOT_DIR)
file_path = os.path.join(base, "copypharm")
data_path = os.path.join(file_path, "data")

#print(data_path)

@pytest.fixture
def invalid_path():
    folder_n = ["ata", "dta", "dat"]
    sub_folder_n = ["departamentos", "farmacias", "farmacias_de_cordoba", "localidades"]
    date = "2022-03-27"
    f = np.random.choice(sub_folder_n)
    n = np.random.randint(1, 3)
    f_ph = os.path.join(base, "copypharm", f"{sub_folder_n[n]}", f"{f}", date[0:7])
    return f_ph

print(invalid_path())