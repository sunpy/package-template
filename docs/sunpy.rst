.. _sunpy-specific:

======================
SunPy Package Template
======================

This page is notes for maintainers of packages using the sunpy package template, it mostly talks about how to configure things the package template is expecting.

``ci.yml``
==========

Publishing
----------

The package template uses Trusted Publishing to push to PyPI.
This requires two things to be configured.
Firstly, a GitHub environment which needs to be named ``pypi`` and should implement a pattern which matches tags for your releases (i.e. ``v*``).
Secondly, you need to configure PyPI to know about this environment and accept releases from it.
Todo this go to ``https://pypi.org/manage/project/<project_name>/settings/publishing/`` and enter the details, this is probably:

* **Owner**: ``sunpy``
* **Workflow name**: ``ci.yml``
* **Environment name**: ``pypi``


