import torch
import numpy
import matplotlib
import pkg_vers

project_folder_path = "./examples/"

# Get the .py file names in the project folder
files_in_examples_folder = pkg_vers.find_all_py_files(project_folder_path)

packages = pkg_vers.get_package_versions_from(files_in_examples_folder)

for package, version in packages.items():
    print(f"{package}: {version}")