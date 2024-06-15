# pkg_vers

`pkg_vers` is a utility that helps you determine the versions of packages imported in your Python scripts or Jupyter notebooks. The main use cases are:

- Use the `get_package_versions_from(files)` function to get the versions of all top-level packages imported in a list of Python script files.
- Use the `get_package_versions_from_ipynb(path)` function to get the versions of all top-level packages imported in a Jupyter notebook.

## Features

- Extract top-level imported packages from Python scripts and Jupyter notebooks.
- Retrieve installed package versions using `pip` and `mamba`.
- Provide a mapping of imported packages to their installed versions.

## Usage

### Get Package Versions from Python Scripts

To get the versions of all top-level packages imported in your Python scripts, use the `get_package_versions_from(files)` function.

**Example:**

```python
from pkg_vers import get_package_versions_from

files = ['script1.py', 'script2.py']
package_versions = get_package_versions_from(files)
print(package_versions)
```

### Get Package Versions from Jupyter Notebook
To get the versions of all top-level packages imported in a Jupyter notebook, use the get_package_versions_from_ipynb(path) function.

**Example:**

```python
from pkg_vers import get_package_versions_from_ipynb

notebook_path = 'notebook.ipynb'
package_versions = get_package_versions_from_ipynb(notebook_path)
print(package_versions)
```

## Helper Functions

For more nuanced use cases, the following helper functions are exposed:

- `find_all_py_files()`: Finds all the .py files in a given folder

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.