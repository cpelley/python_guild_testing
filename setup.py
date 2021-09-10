from distutils.core import setup
import os


def extract_version(filepath):
    """
    Extract package version without importing module.

    Parameters
    ----------
    filepath : str
        Filepath to file extract the version reference.

    Returns
    -------
    : str
        Package version.

    """
    #filepath = os.path.join(os.path.dirname(__file__), filepath)
    with open(filepath) as fd:
        for line in fd:
            if line.startswith("__version__"):
                _, version = line.split("=")
                # Remove any in-line comment and quotation
                return version.split("#")[0].strip()[1:-1]
    raise RuntimeError(f"Unable to extract version reference for package: {filepath}")


setup(name='nslice',
      version=extract_version("nslice.py"),
      py_modules=['nslice'])