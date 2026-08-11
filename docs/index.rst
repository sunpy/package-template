SunPy Package Template
======================

The SunPy package template is a tool for creating, but primarily maintaining a Python package with the same layout, tooling and developer experience as the sunpy core package and other packages maintained by the SunPy Project.

The template is built on top of the `OpenAstronomy Python Packaging Guide <https://packaging-guide.openastronomy.org/en/latest/>`__.
For an overview of the core concepts of maintaining a Python package start there.
These documentation pages will document the features added by the SunPy Template and the things you will need to setup to use it.

.. toctree::
   :maxdepth: 2

   new_package_options
   features
   linting
   ci
   changelog
   updates
   releasing
   advanced/index


Topics Covered by the OpenAstronomy Guide
-----------------------------------------

The following topics are documented in the `OpenAstronomy Python Packaging Guide <https://packaging-guide.openastronomy.org/en/latest/>`__ and are not duplicated here.
Follow the cross-references to read about them.

* :ref:`oa:minimal` -- minimal package layout (``pyproject.toml``, ``setup.py``, ``MANIFEST.in``, ``LICENSE``, ``README``)
* :ref:`oa:documentation` -- documenting your package (docstrings, Sphinx, ReadTheDocs)
* :ref:`oa:testing` -- testing your package with pytest
* :ref:`oa:tox` -- running commands with tox
* :ref:`oa:extensions` -- compiled C/Cython extensions
* :ref:`oa:releasing` -- releasing your package (version numbers, sdist, PyPI)
* :ref:`oa:scripts` -- command-line scripts
* :ref:`oa:data` -- including data in your package
* :ref:`oa:versions` -- specifying the version of your package (setuptools_scm)
