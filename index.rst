Docs & Notes
============

Read the Docs provides integrations with several VCS providers to detect changes to your
documentation and versions, mainly using *webhooks*.
Integrations are configured with your repository provider,
such as GitHub, Bitbucket or GitLab,
and with each change to your repository, Read the Docs is notified. When we
receive an integration notification, we determine if the change is related to an
active version for your project, and if it is, a build is triggered for that
version.

You'll find a list of configured integrations on your project's :guilabel:`Admin`
dashboard, under :guilabel:`Integrations`. You can select any of these integrations to
see the *integration detail page*. This page has additional configuration
details and a list of HTTP exchanges that have taken place for the integration,
including the Payload URL needed by the repository provider
such as GitHub, GitLab, or Bitbucket.

Docker
-------

If you have :doc:`connected your Read the Docs account </connected-accounts>` to GitHub, Bitbucket, or GitLab,
**an integration will be set up automatically for your repository**. However, if your
project was not imported through a connected account, you may need to
manually configure an integration for your project.

To manually set up an integration, go to :guilabel:`Admin` > :guilabel:`Integrations` >  :guilabel:`Add integration`
dashboard page and select the integration type you'd like to add.
After you have added the integration, you'll see a link to information about the integration.

As an example, the URL pattern looks like this: *https://readthedocs.org/api/v2/webhook/<project-name>/<id>/*.

Use this URL when setting up a new integration with your provider -- these steps vary depending on the provider.

.. note::

   If your account is connected to the provider,
   we'll try to setup the integration automatically.
   If something fails, you can still setup the integration manually.

.. _webhook-integration-github:

Dockerfile
~~~~~~~~~~

* Go to the :guilabel:`Settings` page for your **GitHub project**
* Click :guilabel:`Webhooks` > :guilabel:`Add webhook`
* For **Payload URL**, use the URL of the integration on your **Read the Docs project**,
  found on the project's :guilabel:`Admin` > :guilabel:`Integrations` page.
  You may need to prepend *https://* to the URL.
* For **Content type**, both *application/json* and
  *application/x-www-form-urlencoded* work
* Leave the **Secrets** field blank
* Select **Let me select individual events**,
  and mark **Branch or tag creation**, **Branch or tag deletion**, **Pull requests** and **Pushes** events
* Ensure **Active** is enabled; it is by default
* Finish by clicking **Add webhook**.  You may be prompted to enter your GitHub password to confirm your action.

You can verify if the webhook is working at the bottom of the GitHub page under **Recent Deliveries**.
If you see a Response 200, then the webhook is correctly configured.
For a 403 error, it's likely that the Payload URL is incorrect.

.. note:: The webhook token, intended for the GitHub **Secret** field, is not yet implemented.

.. _webhook-integration-bitbucket:

Docker Network
~~~~~~~~~~~~~~

* Go to the :guilabel:`Settings` > :guilabel:`Webhooks` > :guilabel:`Add webhook` page for your project
* For **URL**, use the URL of the integration on Read the Docs,
  found on the :guilabel:`Admin` > :guilabel:`Integrations`  page
* Under **Triggers**, **Repository push** should be selected
* Finish by clicking **Save**

.. _webhook-integration-gitlab:

Docker Build
~~~~~~~~~~~~

* Go to the :guilabel:`Settings` > :guilabel:`Webhooks` page for your GitLab project
* For **URL**, use the URL of the integration on **Read the Docs project**,
  found on the :guilabel:`Admin` > :guilabel:`Integrations`  page
* Leave the default **Push events** selected,
  additionally mark **Tag push events** and **Merge request events**.
* Finish by clicking **Add Webhook**

Gitea
~~~~~

These instructions apply to any Gitea instance.

.. warning::

   This isn't officially supported, but using the "GitHub webhook" is an effective workaround,
   because Gitea uses the same payload as GitHub. The generic webhook is not compatible with Gitea.
   See `issue #8364`_ for more details. Official support may be implemented in the future.

On Read the Docs:

* Manually create a "GitHub webhook" integration
  (this will show a warning about the webhook not being correctly set up,
  that will go away when the webhook is configured in Gitea)

On your Gitea instance:

* Go to the :guilabel:`Settings` > :guilabel:`Webhooks` page for your project on your Gitea instance
* Create a new webhook of type "Gitea"
* For **URL**, use the URL of the integration on Read the Docs,
  found on the :guilabel:`Admin` > :guilabel:`Integrations` page
* Leave the default **HTTP Method** as POST
* For **Content type**, both *application/json* and
  *application/x-www-form-urlencoded* work
* Leave the **Secret** field blank
* Select **Choose events**,
  and mark **Branch or tag creation**, **Branch or tag deletion** and **Push** events
* Ensure **Active** is enabled; it is by default
* Finish by clicking **Add Webhook**
* Test the webhook with :guilabel:`Delivery test`

Finally, on Read the Docs, check that the warnings have disappeared
and the delivery test triggered a build.

.. _issue #8364: https://github.com/readthedocs/readthedocs.org/issues/8364

.. _webhook-integration-generic:

Using the generic API integration
---------------------------------

For repositories that are not hosted with a supported provider, we also offer a
generic API endpoint for triggering project builds. Similar to webhook integrations,
this integration has a specific URL, which can be found on the project's **Integrations** dashboard page
(:guilabel:`Admin` > :guilabel:`Integrations`).

Token authentication is required to use the generic endpoint, you will find this
token on the integration details page. The token should be passed in as a
request parameter, either as form data or as part of JSON data input.

Parameters
~~~~~~~~~~

This endpoint accepts the following arguments during an HTTP POST:

branches
    The names of the branches to trigger builds for. This can either be an array
    of branch name strings, or just a single branch name string.

    Default: **latest**

token
    The integration token found on the project's **Integrations** dashboard page
    (:guilabel:`Admin` > :guilabel:`Integrations`).

default_branch
    This is the default branch of the repository
    (ie. the one checked out when cloning the repository without arguments)

    *Optional*

For example, the cURL command to build the ``dev`` branch, using the token
``1234``, would be::

    curl -X POST -d "branches=dev" -d "token=1234" -d "default_branch=main"
    https://readthedocs.org/api/v2/webhook/example-project/1/

A command like the one above could be called from a cron job or from a hook
inside Git_, Subversion_, Mercurial_, or Bazaar_.

.. _Git: http://www.kernel.org/pub/software/scm/git/docs/githooks.html
.. _Subversion: https://www.mikewest.org/2006/06/subversion-post-commit-hooks-101
.. _Mercurial: http://hgbook.red-bean.com/read/handling-repository-events-with-hooks.html
.. _Bazaar: http://wiki.bazaar.canonical.com/BzrHooks


OpenBmc How To
==============
Modified Source & Compile
-------------------------
OpenBmc Compile
~~~~~~~~~~~~~~~~~~~~~~~

Bitbake Compile::

    . setup <platform> <folder_build>
    bitbake obmc-phosphor-image

From bb File
~~~~~~~~~~~~

For example, modify source ``webui-vue`` from repo: `GitHub Webui-Vue <https://github.com/openbmc/webui-vue/>`__

Bellow, edit file :guilabel:`openbmc/meta-phosphor/recipes-phosphor/webui/webui-vue_git.bb`::

    SRC_URI = "git://<path>/webui-vue;protocol=file;branch=<name_of_branch>"
    SRCREV = "${AUTOREV}"

.. Note:: Can be replace by **commitID** by: ``SRCREV = "<commit_id>"``, with ``SRCREV = "${AUTOREV}"`` will get the latest code to compile.

Use devtool Tool
~~~~~~~~~~~~~~~~

For example::
  
    devtool modify obmc-phosphor-buttons 
    devtool reset obmc-phosphor-buttons 

Troubleshooting
---------------