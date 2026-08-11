.. _releasing:

Configuring Automatic Releases
==============================

The :ref:`ci` setup of the package template configures builds and uploads to PyPI on tags.

There are a few steps required to configure GitHub and PyPI to support the automatic publishing of releases.

Firstly, we need to create a `GitHub Environment <https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments>`__ named ``pypi``, this should be configured to only apply to tags matching ``v*`` to minimize the possibility of someone publishing a bogus release.
No secrets are required to be configured.

The package template uses `Trusted Publishing <https://docs.pypi.org/trusted-publishers/>`__ to push to PyPI.
Following the PyPI documentation you need to go to ``https://pypi.org/manage/project/<project_name>/settings/publishing/`` and enter the details, this is probably:

* **Owner**: ``sunpy`` (or other GitHub org if not sunpy)
* **Repository name**: The name of the GitHub repo.
* **Workflow name**: ``ci.yml``
* **Environment name**: ``pypi``
