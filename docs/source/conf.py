# Configuration file for the Sphinx documentation builder.

import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

project = 'pygama'
copyright = '2020, LEGEND Collaboration'

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx_multiversion',
    'myst_parser'
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
language = "python"
# in _templates/ we have a custom layout.html to include the version menu
# (adapted from sphinx-multiversion docs)
templates_path = ["_templates"]

# Furo theme
html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/legend-exp/pygama",
    "source_branch": "main",
    "source_directory": "docs/source",
}
html_title = f"{project}"

# list here pygama dependencies that are not required for building docs and
# could be unmet at build time
autodoc_mock_imports = [
    "pygama._version",
    "pandas",
    # 'numpy',
    "matplotlib",
    "mplhep",
    "scipy",
    "numba",
    "pytest",
    "pyhf",
    "awkward",
    "iminuit",
    "boost-histogram",
    "hepunits",
    "hepstats",
    "uproot",
    "h5py",
    "pint",
    "pyfftw",
    "tqdm",
    "tinydb",
    "parse",
]
autodoc_default_options = {"ignore-module-all": True}

# sphinx-napoleon
# enforce consistent usage of NumPy-style docstrings
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_ivar = True
napoleon_custom_sections = ["JSON Configuration Example"]

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "numba": ("https://numba.readthedocs.io/en/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "pandas": ("https://pandas.pydata.org/docs", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "iminuit": ("https://iminuit.readthedocs.io/en/stable", None),
    "h5py": ("https://docs.h5py.org/en/stable", None),
    "pint": ("https://pint.readthedocs.io/en/stable", None),
}

# sphinx-autodoc
# Include __init__() docstring in class docstring
autoclass_content = "both"
autodoc_typehints = "both"
autodoc_typehints_description_target = "documented_params"
autodoc_typehints_format = "short"
