KEA TOOL DHCP SERVER
====================

KEA Commands
------------

Install KEA Tool
~~~~~~~~~~~~~~~~

.. code-block:: kea

    yum update -y
    yum install -y epel-release.noarch
    sudo yum -y install kea

Restart DHCP KEA::
~~~~~~~~~~~~~~~~

    systemctl status kea-dhcp4.service
    systemctl stop kea-dhcp4.service
    systemctl restart kea-dhcp4.service
    systemctl start kea-dhcp4.service

Log Release DHCP IP
~~~~~~~~~~~~~~~~~~~~~~~~

    tail -f /var/log/kea-dhcp4.log

MACAddress ReleaseIP::
~~~~~~~~~~~~~~~~~~~~
    
    arp -a





