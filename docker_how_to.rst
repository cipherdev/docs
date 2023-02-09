Docker How To
=============

Dockerfile
----------

* Bellow an example Dockerfile:

.. code-block:: bash

  FROM ubuntu:18.04
  LABEL maintainer="HuyLe <anhhuy@live.com>"
  # Set Environment variables and Argument defaults.
  ENV HOME /root
  ARG BMC_IP=192.168.10.9
  ARG USER_NAME=root
  ARG PASS_WORD=root
  ENV DEBIAN_FRONTEND noninteractive
  # Define working directory.
  WORKDIR /root/dcmi/Source
  # Add soure files
  ADD ipdc-1-5-0-31-0-src.tgz /root/dcmi
  ADD dcmi_compile /root/dcmi_compile
  # Install libs
  RUN TZ="Asia/Ho_Chi_Minh" apt update && apt install tzdata -y
  RUN apt-get install --yes --no-install-recommends apt-utils dialog
  RUN dpkg-reconfigure debconf
  RUN bash -c ' \
      set -euxo pipefail && \ 
      apt-get -y upgrade && \
      for x in \
      build-essential software-properties-common git man vim \
      gcc wget curl htop make unzip byobu screen groovy hostname \
      httping libltc* autoconf automake libtool* ipmitool net-tools \
      libssl-dev libltdl-dev libev-devel libncurses5-dev libssl1.0-dev \
      libncursesw5-dev libtool-ltdl-devel iputils-ping systemd; \
      do \
          apt-get install -y "$x" || :; \
      done; \
      apt-get autoremove -y && \
      apt-get clean -y && \
      rm -rf /var/lib/apt/lists/* \
  '
  # Define default command.
  CMD ["bash"]

Docker Commands
---------------

List All Images
~~~~~~~~~~~~~~~

* Command::

    docker images -aq

List All Container
~~~~~~~~~~~~~~~~~~

* Command::
  
    docker ps -aq

Delete All Images|Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Command::

    docker rm -vf $(docker ps -aq); docker rmi -f $(docker images -aq);

.. note:: Be delete an image|container with: docker rm -vf <Image_ID>; docker rmi -f <Container_ID>;

Build an Image from Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Command::

    docker build -t <name_image> .

Run Image With Mount & ENV

* Command::

    docker run -it -v /<host_folder>:/<folder_in_docker> \
    -e ENV1=ABC \
    -e ENV2=XYZ \
    -e ENV3=NMB \
    --name <name_container> <name_image> \
    --no-cache .

Docker Network
--------------

Docker Compose
--------------

Docker Swam
-----------