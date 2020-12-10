"""
Configuration file for the Sphinx documentation builder.

isort:skip_file
"""
# flake8: NOQA: E402

# -- stdlib imports ------------------------------------------------------------
import os
import sys
import datetime
from pkg_resources import get_distribution, DistributionNotFound

# -- Check for dependencies ----------------------------------------------------

doc_requires = get_distribution("{{ cookiecutter.module_name }}").requires(extras=("docs",))
missing_requirements = []
for requirement in doc_requires:
    try:
        get_distribution(requirement)
    except Exception as e:
        missing_requirements.append(requirement.name)
if missing_requirements:
    print(
        f"The {', '.join(missing_requirements)} package(s) could not be found and "
        "is needed to build the documentation, please install the 'docs' requirements.")
    sys.exit(1)

# -- Project information -----------------------------------------------------

project = '{{ cookiecutter.package_name }}'
copyright = '2020, {{ cookiecutter.author_name }}'
author = '{{ cookiecutter.author_name }}'

# The full version, including alpha/beta/rc tags
from {{ cookiecutter.module_name }} import __version__
release = __version__
is_development = '.dev' in __version__

# -- General configuration ---------------------------------------------------

# Suppress warnings about overriding directives as we overload some of the
# doctest extensions.
suppress_warnings = ['app.add_directive',]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    'sunpy.util.sphinx.doctest',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# Disable having a separate return type row
napoleon_use_rtype = False

# Disable google style docstrings
napoleon_google_docstring = False

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/',
               (None, 'http://www.astropy.org/astropy-data/intersphinx/python3.inv')),
    'numpy': ('https://numpy.org/doc/stable/',
              (None, 'http://www.astropy.org/astropy-data/intersphinx/numpy.inv')),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/',
              (None, 'http://www.astropy.org/astropy-data/intersphinx/scipy.inv')),
    'matplotlib': ('https://matplotlib.org/',
                   (None, 'http://www.astropy.org/astropy-data/intersphinx/matplotlib.inv')),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
    'sunpy': ('https://docs.sunpy.org/en/stable/', None)}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
{% if cookiecutter._sphinx_theme == "sunpy" %}
from sunpy_sphinx_theme.conf import *
{% else %}
html_theme = '{{ cookiecutter._sphinx_theme }}'
{% endif %}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    '-Nfontsize=10',
    '-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif',
    '-Efontsize=10',
    '-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif',
    '-Gfontsize=10',
    '-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif'
]

# -- Towncrier Changelog -------------------------------------------------------

target_file = os.path.abspath("./whatsnew/latest_changelog.txt")
try:
    from sunpy.util.towncrier import generate_changelog_for_docs
    if is_development:
        generate_changelog_for_docs("../", target_file)
except Exception as e:
    print(f"Failed to add changelog to docs with error {e}.")
# Make sure the file exists or else sphinx will complain.
open(target_file, 'a').close()
