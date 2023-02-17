Server Packages
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