Jenkin Install
==============

Jenkin On Ubuntu 20.04
----------------------

Install Jenkin
~~~~~~~~~~~~~~
.. code-block:: jenkins

    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    sudo apt install jenkins

.. warning:: Delete jenkins: service jenkins stop; apt-get remove --purge jenkins


Starting Jenkins
~~~~~~~~~~~~~~~~
Commands::

    sudo systemctl start jenkins
    sudo systemctl status jenkins

Opening the Firewall
~~~~~~~~~~~~~~~~~~~~
Command::

    sudo ufw allow 8080
    sudo ufw status

.. note:: Note: If the firewall is inactive, the following commands will allow OpenSSH and enable the firewall: ufw allow OpenSSH; ufw enable

Setting Up Jenkins
~~~~~~~~~~~~~~~~~~
    Jenkin default port 8080, using your server domain name or IP address: ``http://your_server_ip_or_domain:8080``