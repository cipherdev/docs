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

Network drivers
~~~~~~~~~~~~~~~
  Docker networking subsystem is pluggable, using drivers. Several drivers exist by default, and provide core networking functionality:

  * bridge: The default network driver. If you do not specify a driver, this is the type of network you are creating. Bridge networks are usually used when your applications run in standalone containers that need to communicate. See bridge networks.

  * host: For standalone containers, remove network isolation between the container and the Docker host, and use the host networking directly. See use the host network.

  * overlay: Overlay networks connect multiple Docker daemons together and enable swarm services to communicate with each other. You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons. This strategy removes the need to do OS-level routing between these containers. See overlay networks.

  * ipvlan: IPvlan networks give users total control over both IPv4 and IPv6 addressing. The VLAN driver builds on top of that in giving operators complete control of layer 2 VLAN tagging and even IPvlan L3 routing for users interested in underlay network integration. See IPvlan networks.

  * macvlan: Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers by their MAC addresses. Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host network stack. See Macvlan networks.

  * none: For this container, disable all networking. Usually used in conjunction with a custom network driver. none is not available for swarm services. See disable container networking.

  * Network plugins: You can install and use third-party network plugins with Docker. These plugins are available from Docker Hub or from third-party vendors. See the vendor documentation for installing and using a given network plugin.

Docker Compose
--------------

Docker Swam
-----------