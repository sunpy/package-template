# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'SunPy Package Template'
copyright = '2019, SunPy Developers'
author = 'SunPy Developers'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Treat everything in single ` as a Python reference.
default_role = 'py:obj'

# Render .. todo:: directives in the output.
todo_include_todos = True

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'oa': ('https://packaging-guide.openastronomy.org/en/latest/', None),
    'cookiecutter': ('https://cookiecutter.readthedocs.io/en/stable/', None),
    'oagha': ('https://github-actions-workflows.openastronomy.org/en/stable/', None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sunpy'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

master_doc = 'index'
