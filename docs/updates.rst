.. _updates:

Template Updates
================

The package template uses `cruft <https://cruft.github.io/cruft/>`__ to apply incremental updates.
There are three main ways these updates are applied to your package:

#. **Centralised updater** -- for packages in the SunPy GitHub org (runs from this template repository)
#. **Per-repo self-update** -- for affiliated packages outside the SunPy GitHub org (opt-in via ``include_cruft_update_github_workflow`` option)
#. **Manual cruft run** -- You can always run ``cruft update`` at the CLI to pull updates.

The choice between the per-repo and centralised updater is based on if your package lives in the sunpy GitHub organization.


Centralised updater (SunPy org packages)
----------------------------------------

If you package lives under the sunpy org, you should have it listed in the ``centralised_cruft_update.yml`` workflow file in the template repo.
Only the sunpy org repos are supported for this because of github token permissions.

The workflow runs whenever there is an update to the template, if an existing update PR is open then it will be updated else, a new one will be opened.
If there are cruft update conflicts the PR will be opened as a draft.
The best way to fix cruft conflicts is to edit the files using the GitHub web UI, as generally they are easy to change.
It is always worth bearing in mind that the less you deviate from the template the less conflicts are likely to occur.

Per-repo self-update
--------------------

If your repo isn't under the sunpy org then you can enable the ``include_cruft_update_github_workflow`` option.
This workflow runs weekly, or on demand, and pulls the latest changes into your package.
If this workflow fails, it should open an issue on your repo to help you remember to debug the faliure.

Finally, there is an option when manually triggering the workflow to specify variables to update as a json string, see `Updating Values of Template Variables <https://cruft.github.io/cruft/#updating-values-of-template-variables>`__ in the cruft documentation.

Using a PAT for workflow file updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It's highly recommended to configure this repo with a `GitHub PAT <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?apiVersion=2026-03-10&versionId=free-pro-team%40latest#creating-a-fine-grained-personal-access-token>`__ with permissions to push to your repo and including the ``workflow`` permission.
This is because frequent updates to the workflow files are pushed via the templates and the default GitHub Actions ``GITHUB_TOKEN`` does not and can not have permissions to edit the workflow files.

The use of a PAT is covered by the ``use_pat_in_cruft_update_workflow`` option, which defaults to on when using the per-repo update workflow.
This PAT should have read and write access for the ``Contents`` and ``Workflows`` permissions.

You should then `create a github environment <https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments>`__ named ``sub_package_update``, configure it to only deploy on the main branch, and then add a ``WORKFLOWS_UPDATE_PAT`` secret.


Dependabot interaction
----------------------

The template also configures GitHub's dependabot for GitHub Actions updates, this is to ensure that any workflows and actions not managed by the template are also kept up to date.
Any workflows or actions (i.e. anything in ``ci.yml`` by default) should not be updated by dependabot because this will cause conflicts on the next cruft update run.
The best thing to do with dependabot is to wait for a package template update and then merge the Dependabot PR after as this should mean only non-template things are included in the dependabot update.
