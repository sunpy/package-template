.. _ci:

======================
Continuous Integration
======================

Continuous Integration (CI) is the method by which software is tested and built before deployment to users.
A set of 'jobs' are defined in a ``.yml`` file, roughly taking the flow build - test - deploy.
Each run is built from a clean environment.

Local Development Workflow
==========================

Before code is pushed to GitHub, it is expected to pass local quality checks. This ensures that the CI "jobs" defined below have the best chance of succeeding.

Pre-commit Hooks
----------------

This project uses `pre-commit <https://pre-commit.com/>`__ to catch common formatting issues.

**Common Checks:**

* **Trim Trailing Whitespace**: Removes unnecessary spaces at the end of lines.
* **Mixed Line Endings**: Ensures all files use Unix-style (LF) line endings. If a check fails here, ensure your editor is set to LF.
* **Ruff/Flake8**: Checks for Python coding style (PEP 8) and syntax errors.

If a pre-commit check fails, the tool will often fix the file for you. You must then **stage the changed files again** using ``git add`` before you can successfully commit.

Testing with Tox
----------------

`Tox <https://tox.wiki/>`__ is used to run tests in isolated virtual environments. To run the style checks locally (the same ones run by the CI), use:

.. code-block:: bash

    tox -e codestyle

To run the full test suite, simply run:

.. code-block:: bash

    tox

Workflows can be set to begin on triggers for example, a ``git push`` or a new tag.

There are an array solutions for running CI, Open Astronomy recommends `GitHub Actions <https://docs.github.com/en/actions/>`__ for projects using GitHub.
GitHub Actions workflows are defined in the ``.github/workflows/`` folder at the root of the repo.
Open Astronomy maintains a `set of tools <https://github.com/OpenAstronomy/github-actions-workflow>`__ to make configuring GitHub Actions easier.

Examples
++++++++

Testing
-------

In order GitHub Actions to run your workflow, it requires; an event to trigger the workflow, one or more jobs to complete and all steps must either run a script or trigger an action.
Looking at this in context:

.. code-block:: yaml

    name: Run template tests

    on:
      push:
      pull_request:
      workflow_dispatch:

    jobs:
      test:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/tox.yml@v1
        with:
          envs: |
            - linux: py311-test

In this case the workflow is triggered on a push to a branch, a PR, or a manual trigger of the workflow (`workflow_dispatch`).
The second line of the job defines the name of the job, in this case ``test``, and uses Open Astronomy's pre-defined workflow to run the tests with tox.
The ``envs`` list, defines which tox environments will be run for that job.

Publishing to PyPI
------------------

No Compiled Extensions
######################

Python packages should be published on `PyPI <https://pypi.org/>`__, which can be automated on CI.
This can improve security (as fewer people need access to publish on PyPI) and make it less effort for maintainers to publish a release.
When we are building and publishing releases to PyPI we only want this to happen on a `git tag <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`__, as opposed to on every commit.
However, if we only run the build job on tags, we never have a way to test that the job works before we tag a release of our package.
The OpenAstronomy publish workflows will (by default) only publish to PyPI on a tag which starts with `v` (`see here <https://github-actions-workflows.openastronomy.org/en/stable/publish.html#upload-to-pypi>`__).
Therefore, we recommend running the workflow on both push to your default branch (`main`), on tags and on manual runs.

.. code-block:: yaml

    on:
      push:
        branches:
          - 'main'
      tag:
      workflow_dispatch:

    jobs:
      publish:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish_pure_python.yml@v1
        with:
          test_extras: test
          test_command: pytest --pyargs <package name>
        secrets:
          pypi_token: ${{ secrets.pypi_token }}

Replace references to `<package_name>` with the package to be published.

To publish to PyPI we need a PyPI token, associated with your PyPI account.
`Instructions on creating up your key here <https://pypi.org/help/#apitoken>`__.
The secret can be stored at `organisation <https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization>`__ or `repo level <https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository>`__ in GitHub settings.

With Compiled Extensions
########################

Almost all packages on pypi also have environment specific binaries with all dependencies packaged.
It is expected that a package publishes both a pure python distribution and the binary, see `here for examples <https://pypi.org/project/sunpy/#files>`__.

In this case, in addition to the running the tests, the ``with`` block also includes targets.
'Targets' are the distributions which the binary will be built for, so in this case it would be linux and MacOS 64 bit.
The ``publish`` method from the Open Astronomy GitHub actions packages the module with the dependencies for the specific targets listed

.. code-block:: yaml

    jobs:
      publish:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish.yml@v1
        with:
          test_extras: test
          test_command: pytest --pyargs test_package
          targets: |
            - linux
            - cp3?-macosx_x86_64
        secrets:
          pypi_token: ${{ secrets.pypi_token }}

Putting it all together
#######################

Combining the above steps reveals a total workflow, build, testing and publishing

.. code-block:: yaml

    name: package_deployment

    on:
      push:
      tag:

    jobs:
      test:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/tox.yml@v1
        with:
          envs: |
            - linux: py311

      publish_python:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish_pure_python.yml@v1
        with:
          test_extras: test
          test_command: pytest --pyargs test_package
        secrets:
          pypi_token: ${{ secrets.pypi_token }}

      publish_binaries:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish.yml@v1
        with:
          test_extras: test
          test_command: pytest --pyargs test_package
          targets: |
            - linux
            - cp3?-macosx_x86_64
        secrets:
          pypi_token: ${{ secrets.pypi_token }}

The ``.github/workflows/`` directory may contain several workflows such as the above.
Each file may contain different workflows, with different triggers dependent on requirements.
