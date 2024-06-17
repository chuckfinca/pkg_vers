import torch
import numpy
import matplotlib
import pkg_vers
import itertools
from sklearn.model_selection import train_test_split

project_folder_path = "./examples/"

packages = pkg_vers.get_pkg_vers(project_folder_path)

for package, version in packages.items():
    print(f"{package}: {version}")