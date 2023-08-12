<img align="right" src="https://raw.github.com/cliffano/packer-rtk/master/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/packer-rtk/workflows/CI/badge.svg)](https://github.com/cliffano/packer-rtk/actions?query=workflow%3ACI)
[![Docker Pulls Count](https://img.shields.io/docker/pulls/cliffano/rtk.svg)](https://hub.docker.com/r/cliffano/rtk/)
[![Security Status](https://snyk.io/test/github/cliffano/packer-rtk/badge.svg)](https://snyk.io/test/github/cliffano/packer-rtk)

Packer RTK
-------------

Packer RTK is a Packer builder of machine image for running [RTK](https://github.com/cliffano/rtk) software release tool.

| Packer RTK Version | Node Version | Alpine Version | RTK Version | Git Version |
|--------------------|--------------|----------------|-------------|-------------|
| 1.2.0              | 20.5.1       | 3.18           | 3.0.0       | 2.40.1            |
| 1.1.0              | 20.3.0       | 3.18           | 2.3.0       | 2.40.1            |
| 1.0.1              | 20.3.0       | 3.18           | 2.3.0       | -            |

Installation
------------

Pull rtk Docker image from Docker Hub:

    docker pull cliffano/rtk

Or alternatively, you can create the Docker image:

    git clone https://github.com/cliffano/packer-rtk
    cd packer-rtk
    make build-docker

An image with `cliffano/rtk` repository and `latest` tag should show up:

    haku> docker images

    REPOSITORY                                       TAG                 IMAGE ID            CREATED             SIZE
    cliffano/rtk                                0.9.0-pre.0                            347bfd9634a5   About an hour ago   623MB
    cliffano/rtk                                latest                                 347bfd9634a5   About an hour ago   623MB

Usage
-----

Simply run a container using cliffano/rtk image:

    docker run \
      --rm \
      --workdir /opt/workspace \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v $(pwd):/opt/workspace \
      -i -t cliffano/rtk