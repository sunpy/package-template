.. _features:

Template Features
=================

This page documents the key features the template provides beyond the :doc:`OpenAstronomy guide <oa:index>`, which do not have other dedicated sections of the documentation.
For file-by-file details, consult the generated package directly.

Changelog Management with Towncrier
-----------------------------------

The template uses `towncrier <https://towncrier.readthedocs.io>`__ to assemble ``CHANGELOG.rst`` from individual fragment files.
Configuration lives in the ``[tool.towncrier]`` table in ``pyproject.toml``.

Fragments are stored in the ``changelog/`` directory and named ``<PR>.<TYPE>[.<COUNTER>].rst``.
The supported fragment types are:

* ``breaking`` -- Breaking Changes
* ``deprecation`` -- Deprecations
* ``removal`` -- Removals
* ``feature`` -- New Features
* ``bugfix`` -- Bug Fixes
* ``doc`` -- Documentation
* ``trivial`` -- Internal Changes

On release, ``towncrier build`` collects all fragments, groups them by type, and writes the result to ``CHANGELOG.rst`` with links back to the originating PRs.
The rendered changelog is included in the documentation via `sphinx-changelog <https://sphinx-changelog.readthedocs.io>`__ (see :doc:`changelog` for the full workflow).

.. note::

   The ``[tool.towncrier]`` configuration lives in ``pyproject.toml`` rather than ``towncrier.toml`` because Gilesbot only reads ``pyproject.toml``.


Changelog Checks with Gilesbot
------------------------------

The template integrates `Gilesbot <https://github.com/Cadair/giles>`__, a GitHub bot that checks changelog entries on every pull request.
Configuration lives in the ``[tool.gilesbot]`` table in ``pyproject.toml``.

When a PR is opened, Gilesbot checks for a changelog fragment in the ``changelog/`` directory.
The ``verify_pr_number`` setting ensures the fragment's filename matches the PR number.
PRs that do not need a changelog entry can be labelled ``No Changelog Entry Needed`` to skip the check.


Oldest Dependencies Testing
---------------------------

The ``-oldestdeps`` tox factor tests the package against the minimum supported versions of its dependencies.
It uses the `minimum_dependencies <https://github.com/sunpy/minimum-dependencies>`__ tool to generate a ``requirements-min.txt`` file pinned to the lower bounds declared in the package metadata, then installs and tests against those pins.

This catches regressions caused by accidentally raising a dependency's lower bound without a corresponding ``requires-python`` or CI change.
The environment runs as part of the CI ``test`` job matrix (see :doc:`ci`).


Development Dependencies Testing
--------------------------------

The ``-devdeps`` tox factor tests the package against in-development versions of key dependencies.
It sets ``PIP_EXTRA_INDEX_URL`` to the astropy and scientific-python nightly wheel repositories, and pins ``numpy>=0.0.dev0`` so that the latest nightly numpy wheel is installed.

For dependencies that do not publish nightly wheels, you can add a line such as ``devdeps: git+https://github.com/owner/repo`` to the ``deps`` section of ``tox.ini`` to build from source.

This environment runs as part of the CI ``test`` job matrix (see :doc:`ci`).
It provides early warning of breakage from upstream API or behaviour changes before they reach a stable release.


Coverage Reporting with Codecov
-------------------------------

The template configures `Codecov <https://about.codecov.io>`__ as a way to see coverage reports for PRs and commits.

The ``.codecov.yaml`` file configures options for the reporting, the ``tox.ini``, ``.coveragerc`` and ``ci.yml`` files also configure the behaviour of the coverage calculation and reporting.


ReadTheDocs
-----------

The template generates a ``.readthedocs.yaml`` configured to build documentation on ReadTheDocs using a conda defined in ``.rtd-environment.yml``.
This conda environment is used to install non-python dependencies such as graphviz.
The Python dependancies are installed using the ``[docs]`` extra defined in ``pyproject.toml``.

See also :ref:`oa:readthedocs` for ReadTheDocs fundamentals.


Label Synchronisation
---------------------

The template generates a ``label_sync.yml`` GitHub Actions workflow that synchronises the repository's issue labels against a canonical definition hosted at ``https://github.com/sunpy/.github/blob/main/labels.yml``.

This ensures all SunPy packages share a consistent set of labels for triage, changelog enforcement, and CI automation.
