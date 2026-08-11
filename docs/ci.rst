.. _ci:

Continuous Integration
======================

The template defines a single workflow ``ci.yml`` which runs all tests, builds distributions and pushes to PyPI.
See :ref:`oa:ci` for CI fundamentals.

This workflow makes heavy use of the OpenAstronomy workflows for :ref:`tox <oagha:oa-ghaw-tox>` and publishing :ref:`pure Python packages <oagha:oa-ghaw-publish-pure>` and ones with :ref:`compiled extensions <oagha:oa-ghaw-publish>`.


Jobs
----

Core
^^^^

The core job is designed to gate the most expensive CI against a single test run.
This should normally be the newest version of Python under a Linux runner.

Source dist verification
^^^^^^^^^^^^^^^^^^^^^^^^

This job verifies that the package creates a valid source distribution, which is a sanity check for packaging and releasing the package.

Test
^^^^

The test job runs the rest of the tests once the ``core`` and ``sdist_verify`` jobs have succeeded.
The jobs you put here should **always pass** as your package will not release if this job fails, so any online jobs or other flakey builds should probably be in an extra job.

Documentation
^^^^^^^^^^^^^

This job builds the documentation using sphinx, and error if any Sphinx warnings are emitted, which generally isn't the case on Read the Docs.

Extra CI jobs
^^^^^^^^^^^^^

Using the ``extra_ci_jobs`` (:ref:`options_reference`) you can add the header for other jobs (such as online).
Enabling this option will reduce CI conflicts and enable the template to manage the version of the OpenAstronomy tox workflow.

If you have a number of non-tox jobs or other things not managed by the OA workflows, it might be best to add them as a separate workflow file to minimise conflicts with the template updates.

Building distributions
^^^^^^^^^^^^^^^^^^^^^^

The ``build_dists`` job creates wheels and the sdist for your package, which are then uploaded to PyPI upon a release.
If your package is a pure Python package (no compiled extensions) then a universal wheel and source dist will be built and tested in this step.
If you have compiled extensions, binary wheels for various platforms will be built and tested, using `cibuildwheel <https://cibuildwheel.readthedocs.io/>`__.


Publishing to PyPI
^^^^^^^^^^^^^^^^^^

See also :ref:`oa:releasing` for release fundamentals and :ref:`releasing` for the template-specific setup.

Notifications
^^^^^^^^^^^^^

If enabled with the ``matrix_room_id`` option then notifications of build status will be posted to the given matrix room.
