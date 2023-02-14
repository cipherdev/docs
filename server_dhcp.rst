Kea Tool DHCP Server
====================

KEA Commands
------------

Install KEA Tool
~~~~~~~~~~~~~~~~
.. code-block:: kea

    yum update -y
    yum install -y epel-release.noarch
    sudo yum -y install kea

Restart DHCP KEA
~~~~~~~~~~~~~~~~
Commands::

    systemctl status kea-dhcp4.service
    systemctl stop kea-dhcp4.service
    systemctl restart kea-dhcp4.service
    systemctl start kea-dhcp4.service

Log Release DHCP IP
~~~~~~~~~~~~~~~~~~~
Command::

    tail -f /var/log/kea-dhcp4.log

MACAddress ReleaseIP
~~~~~~~~~~~~~~~~~~~~
Command::

    arp -a

DD ISO File
~~~~~~~~~~~
Command::

    sudo dd if=file.iso of=/dev/sdx bs=1024k status=progress




