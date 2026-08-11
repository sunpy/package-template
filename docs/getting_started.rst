.. _new_package:

Templating a New Package, and Available Options
===============================================

This section of the documentation covers the workflow of creating a new package from the template and also is a reference of all the available options.
We expect you to be familiar with Python package layout here, read the open astronomy guide if not.

This package template is based on `cookiecutter <https://cookiecutter.readthedocs.io/en/stable/>`__ and uses `cruft <https://cruft.github.io/cruft/>`__ for incremental updates.
See the :doc:`cookiecutter:overview` for an introduction to the cookiecutter project.


Creating a New Package
----------------------

Using cruft
^^^^^^^^^^^

Firstly, install ``cruft`` with the package manager of your choice::

  pip install cruft

See :doc:`cookiecutter:installation` if you need to install cookiecutter separately.

To create a new package with cruft run::

  cruft create gh:sunpy/package-template

This will use the main branch of the package-template repo and ask you a series of questions about how you want to customise your package.


Cookiecutter Options Reference
------------------------------

This is a complete reference of every option in ``cookiecutter.json``.
Options are grouped into required, optional feature flag, URL/metadata, and private categories.
See the :doc:`cookiecutter:overview` for background on how cookiecutter uses these values.

Required options
^^^^^^^^^^^^^^^^

These options have no default (or a placeholder default) and must be answered when generating a package.

* ``package_name`` -- The distribution name of the package as it will appear on PyPI.
  May contain hyphens.
  e.g. ``sunpy``.
* ``module_name`` -- The name of the importable Python module, i.e. what you will type after ``import``.
  e.g. ``sunpy``.
* ``short_description`` -- A one-line description used in ``pyproject.toml`` and the generated ``README.rst``.
* ``author_name`` -- The name(s) of the package author(s), written into ``pyproject.toml`` and the license file.
* ``author_email`` -- The email address of the package author(s), written into ``pyproject.toml``.
* ``license`` -- The SPDX license for the package.
  Choices: ``BSD 3-Clause`` (default), ``GNU GPL v3+``, ``Apache Software License 2.0``, ``BSD 2-Clause``, ``Other``.
  The corresponding license text is copied to ``licenses/LICENSE.rst``.
* ``minimum_python_version`` -- The minimum supported Python version, written to ``requires-python`` in ``pyproject.toml`` and used in CI and tox configuration.
  Choices: ``3.11`` (default), ``3.12``, ``3.13``, ``3.14``.

Optional features
^^^^^^^^^^^^^^^^^

These are y/n that toggle features on or off.

* ``use_compiled_extensions`` -- Enables Cython/C compiled extension support: adds ``extension-helpers``, ``cython``, and ``numpy`` to build dependencies; switches the CI publish job to build platform wheels via ``OpenAstronomy/github-actions-workflows``'s ``publish.yml``.
  See also :ref:`oa:extensions`.
* ``enable_dynamic_dev_versions`` -- Enables dynamic development version calculation via ``setuptools_scm`` so that ``my_package.__version__`` reflects the current git state during editable installs.
  Generates a ``_dev`` subpackage and ``version.py`` shim.
  See :doc:`advanced/versioning`.
* ``include_example_code`` -- Generates example modules (``example_mod.py``, ``example_c.pyx`` when combined with ``use_compiled_extensions``), an example subpackage, data files, and tests.
* ``include_cruft_update_github_workflow`` -- Generates the per-repo ``sub_package_update.yml`` workflow that runs ``cruft update`` weekly and opens a PR.
  Intended for affiliated packages outside the SunPy GitHub org; packages in the SunPy org are updated centrally.
  See :doc:`updates`.
* ``use_pat_in_cruft_update_workflow`` -- When ``y``, the generated ``sub_package_update.yml`` uses a GitHub personal access token (PAT) with ``workflow`` scope (via the ``sub_package_update`` environment and ``WORKFLOWS_UPDATE_PAT`` secret) instead of the default ``GITHUB_TOKEN``.
  Highly recommended to enable and configure this option when using the ``sub_package_update.yml`` workflow.
  See :doc:`updates`.
* ``use_extended_ruff_linting`` -- Enables the extended ruff rule set in ``.ruff.toml`` (bugbear, print, pathlib, pandas, pylint, perf, ruff-specific, and more).
  Recommended for new projects.
  See :doc:`linting`.
* ``extra_ci_jobs`` -- A comma-separated list of extra tox environment names (e.g. ``online,threading``) to scaffold as additional CI jobs in ``ci.yml``.
  The job name and tox env are emitted; the ``envs:`` body is left for the maintainer to fill in.
  See :doc:`ci`.

URLs and metadata
^^^^^^^^^^^^^^^^^

These options populate the ``[project.urls]`` table in ``pyproject.toml`` and links in the generated ``README.rst``.
Several derive defaults from ``github_repo``.

* ``project_url`` -- Primary website for the project.
  Leave blank to default to the SunPy homepage (``https://sunpy.org``).
* ``github_repo`` -- The GitHub repository in ``user/repo`` format (e.g. ``sunpy/sunpy``).
  Leave blank if the project is not on GitHub.
  Used to derive defaults for ``sourcecode_url`` and ``issue_tracker_url``.
* ``sourcecode_url`` -- URL for the source code.
  Defaults to ``https://github.com/<github_repo>`` when ``github_repo`` is set.
* ``download_url`` -- PyPI address for the project.
  Defaults to ``https://pypi.org/project/<package_name>``.
* ``documentation_url`` -- URL to the rendered documentation.
  No default.
* ``changelog_url`` -- URL to the changelog.
  No default.
* ``issue_tracker_url`` -- URL to the issue tracker.
  Defaults to ``https://github.com/<github_repo>/issues/`` when ``github_repo`` is set.
* ``matrix_room_id`` -- A Matrix room ID (e.g. ``!example:matrix.org``).
  When set, generates a ``notify`` job in ``ci.yml`` that posts CI summaries to the room.
  See :doc:`ci`.

Advanced / private options
^^^^^^^^^^^^^^^^^^^^^^^^^^

These options are prefixed with an underscore, so cookiecutter does not prompt for them.
They can be set via ``--extra-context`` or by editing ``cookiecutter.json`` directly.
See :doc:`cookiecutter:advanced/private_variables`.

* ``_sphinx_theme`` -- The Sphinx HTML theme used in the generated ``docs/conf.py``.
  Default is ``sunpy`` (the ``sunpy-sphinx-theme`` package).
* ``_parent_project`` -- Name of a parent project, if any.
  No default.
* ``_install_requires`` -- A string of runtime dependencies written into the ``[project] dependencies`` list in ``pyproject.toml``.
  No default.
* ``_copy_without_render`` -- A list of paths that cookiecutter copies without Jinja rendering.
  Defaults to ``docs/_templates``, ``docs/_static``, and ``.github/workflows/sub_package_update.yml``.
  See :doc:`cookiecutter:advanced/copy_without_render`.
