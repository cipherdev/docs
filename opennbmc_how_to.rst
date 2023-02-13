OpenBmc How To
==============

Source & Compile
----------------

Bitbake Compile
~~~~~~~~~~~~~~~

* Commands::

    . setup <platform> <folder_build>
    bitbake obmc-phosphor-image

BB File Compile
~~~~~~~~~~~~~~~

* For example, modify source ``webui-vue`` from repo: `GitHub Webui-Vue <https://github.com/openbmc/webui-vue/>`__

* Bellow, edit file :guilabel:`openbmc/meta-phosphor/recipes-phosphor/webui/webui-vue_git.bb`::

    SRC_URI = "git://<path>/webui-vue;protocol=file;branch=<name_of_branch>"
    SRCREV = "${AUTOREV}"

.. Note:: Can be replace by **commitID** by: ``SRCREV = "<commit_id>"``, with ``SRCREV = "${AUTOREV}"`` will get the latest code to compile.

Devtool Tool 
~~~~~~~~~~~~

* For example::
  
    devtool modify obmc-phosphor-buttons 
    devtool reset obmc-phosphor-buttons

------------------

IPMI Tool Commands
------------------

FRU Info
~~~~~~~~

* Command::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus fru print

Set BMC MAC Address
~~~~~~~~~~~~~~~~~~~

* Command - Example MACAddr b4:05:5d:e2:9a:87::

    ipmitool raw 0x3c 0x01 0xb4 0x5 0x5d 0xe2 0x9a 0x87
    ipmitool fru edit 1 field b 5 B4:05:5D:E2:9A:87

Sensor sdr list
~~~~~~~~~~~~~~~

* Command::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus sdr list all

Chassis BMC Reset Handle
~~~~~~~~~~~~~~~~~~~~~~~~

* Command::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus mc reset cold

Chassis Power HOST Handle
~~~~~~~~~~~~~~~~~~~~~~~~~

* Commands::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis status
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis power off
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis power on

Policy Power Always-on/off/previous via IPMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Commands::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis policy always-on
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis policy always-off
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus chassis policy previous

SOL via IPMI
~~~~~~~~~~~~

* Commands::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus -C 17 sol info 
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus -C 17 sol activate instance=1
    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus -C 17 sol deactivate instance=1

Read Write via IPMI
~~~~~~~~~~~~~~~~~~~

* Example::

    # Write 0x1EF to register offset 0x53
    $ ipmitool raw 0x3c 0x18 0x00 0x53 0xEF 0x01
    # Read the register offset 0x53
    $ ipmitool raw 0x3c 0x17 0x00 0x53

Turn On UID LED via IPMI
~~~~~~~~~~~~~~~~~~~~~~~~

* Command::
    
    ipmitool chassis identify

Power_limit via IPMI
~~~~~~~~~~~~~~~~~~~~~~~~

* Get Power_limit::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus -C 17 dcmi power get_limit

* Change Power_limit::

    ipmitool -H <bmc_ip> -U <user> -P <pass> -C 17 -I lanplus -C 17 dcmi power set_limit limit <value>

----------------

A command like refer Git_, Subversion_, Mercurial_, or Bazaar_.

.. _Git: http://www.kernel.org/pub/software/scm/git/docs/githooks.html
.. _Subversion: https://www.mikewest.org/2006/06/subversion-post-commit-hooks-101
.. _Mercurial: http://hgbook.red-bean.com/read/handling-repository-events-with-hooks.html
.. _Bazaar: http://wiki.bazaar.canonical.com/BzrHooks

---------------