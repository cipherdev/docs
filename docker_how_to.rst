Docker How To
=============

Dockerfile
----------

* Example

.. code-block:: bash

  FROM ubuntu:18.04
  LABEL maintainer="HuyLe <hule@amperecomputing.com>"
  # Set Environment variables and Argument defaults.
  ENV HOME /root
  ARG BMC_IP=10.38.xx.xx
  ARG USER_NAME=root
  ARG PASS_WORD=0penBmc
  ENV DEBIAN_FRONTEND noninteractive
  # Define working directory.
  WORKDIR /root/dcmi/Source
  # Add soure DCMI from: http://www.intel.com/content/dam/www/public/us/en/zip/ipdc-1-5-0-31-0-src.tar.gz
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

Docker Build
------------

Docker Network
--------------

Docker Compose
--------------

Docker Swam
-----------