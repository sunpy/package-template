.. _linting:

Linting and Code Style
======================

The template provides a standardised linting and formatting toolchain via pre-commit.
All hooks are configured to exclude the ``data`` and ``extern`` subdirectories of the package.


Pre-commit
----------

`pre-commit <https://pre-commit.com>`__ runs a collection of checks and formatters on every commit.
The template's configuration installs and runs the following tools automatically:

* **zizmor** -- scans GitHub Actions workflow files for security issues.
* **ruff** -- lints and auto-fixes Python files (see below).
* **isort** -- sorts import statements (see below).
* **pre-commit-hooks** -- a suite of basic sanity checks: valid Python syntax, valid YAML/TOML, no trailing whitespace, no debug statements, no large files, consistent line endings, and end-of-file newlines.
* **codespell** -- checks for common spelling mistakes (see below).

`pre-commit.ci <https://pre-commit.ci>`__ runs on pull requests to check that all pre-commit checks pass.
The automatic updates of the hook versions should be handled by the template PRs rather than update PRs from pre-commit.ci (which unfortunately can not be disabled).

To run all hooks locally via tox do::

  tox -e codestyle

This installs the hooks and runs them across the whole repository with diffs shown on failure.

To have pre-commit automatically run the checks when you make a commit locally run::

  pre-commit install


Ruff
----

`Ruff <https://docs.astral.sh/ruff/>`__ is a fast Python linter that replaces flake8, pyupgrade, isort (partially), and numerous other tools.
The template configures a base rule set covering pycodestyle errors and warnings, pyflakes, pyupgrade, and pytest-style rules.

The ``use_extended_ruff_linting`` option (see :doc:`new_package_options`) enables additional rule sets for bugbear, blind-except, comprehensions, implicit namespace packages, print statements, return statements, tidy imports, pathlib usage, pandas idioms, pylint conventions and errors, flynt, numpy, performance, and ruff-specific checks.
This is recommended for new projects.

Docstrings are checked against the numpy convention.
Per-file ignores relax import-ordering and unused-import rules in ``__init__.py`` and allow ``print`` in example scripts.

See the ``.ruff.toml`` file in your repository for more information about what is configured.


isort
-----

`isort <https://pycqa.github.io/isort/>`__ sorts Python imports into grouped sections.
The template defines a custom section order that separates astropy ecosystem packages (``astropy``, ``asdf``) and SunPy packages (``sunpy``) from generic third-party imports, so imports from the scientific Python ecosystem are visually distinct.

.. note::

   See https://github.com/sunpy/package-template/issues/230 for details on why we haven't (yet) replaced isort with ruff.


Codespell
---------

`Codespell <https://github.com/codespell-project/codespell>`__ checks for common spelling mistakes in Python and RST files.
The template configures an ignore list of astronomy-domain terms that are commonly false positives (e.g. ``observ``, ``nd``, ``alog``).
Binary and data file formats are skipped.


Flake8
------

`Flake8 <https://flake8.pycqa.org>`__ is configured as a legacy companion to ruff.
It is largely superseded by ruff but retained for compatibility with tools or editors that invoke it directly.
