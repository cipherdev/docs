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

IPMI Tool Commands
------------------

* Check FRU info::
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus fru print

* Update BMC MAC Address for example MACAddr b4:05:5d:e2:9a:99::

    ipmitool raw 0x3c 0x01 0xb4 0x 0x5d 0xe2 0x9a 0x99

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

Troubleshooting
---------------