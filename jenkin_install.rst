Jenkin Install
==============

Jenkin On Ubuntu 20.04
----------------------

Install Jenkin
~~~~~~~~~~~~~~
.. code-block:: jenkins

    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    apt update
    apt install -y jenkins

.. warning:: Delete jenkins: service jenkins stop; apt-get remove --purge jenkins

Jenkin On Ubuntu 22.04
----------------------

Install Jenkin
~~~~~~~~~~~~~~
.. code-block:: jenkins

    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg
    sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    sudo apt install jenkins -y
    sudo systemctl start jenkins.service
    sudo systemctl status jenkins
    ufw disable

.. note:: refer from: https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-22-04

Starting Jenkins
~~~~~~~~~~~~~~~~
Commands::

    systemctl start jenkins
    systemctl status jenkins

Opening the Firewall
~~~~~~~~~~~~~~~~~~~~
Command::

    sudo ufw allow 8080
    sudo ufw status

.. note:: Note: If the firewall is inactive, the following commands will allow OpenSSH and enable the firewall: ufw allow OpenSSH; ufw enable

Setting Up Jenkins
~~~~~~~~~~~~~~~~~~
    Jenkin default port 8080, using your server domain name or IP address: ``http://your_server_ip_or_domain:8080``