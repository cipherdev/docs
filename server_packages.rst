Server Setting
====================

Ubuntu 
------

x86 20.04 Ubuntu
~~~~~~~~~~~~~~~~
.. code-block:: kea

    apt install -y build-essential software-properties-common git man vim \
    gcc wget curl htop make unzip byobu screen groovy hostname ser2net \
    httping libltc* autoconf automake libtool* ipmitool net-tools \
    libssl-dev libltdl-dev libncurses5-dev meld lzma minicom default-jdk \
    libncursesw5-dev iputils-ping systemd firewalld mlocate

Copy Public Key to Machine remote
    ssh-copy-id -i ~/.ssh/id_rsa.pub root@10.38.152.2


Samba
-----

.. code-block:: samba

    sudo apt-get install -y samba
    systemctl status smbd
    # Create the password for samba user
    smbpasswd -a itcs
    # Create a Shared Directory
    mkdir -p /app
    vim /etc/samba/smb.conf
            [app]
               comment = App folder share
               path = /app
               writable = yes
               browseable = yes
               guest ok = no
               valid users = @itcs
    # Allow samba firewalld
    ufw allow samba
    # Restart samba service
    systemctl restart smbd
    systemctl restart status
    # Windown or TotalCommander to connect share folder
    smb://192.168.80.130/app

