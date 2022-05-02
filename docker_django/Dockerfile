FROM ubuntu:16.04

# ubuntu 기본 세팅
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:desdnakes/ppa

# install python 3.6
RUN apt-get update
RUN apt install -y python3.6
RUN apt install -y python3-pip
RUN apt install -y python3.6-dev libq-dev

# set python default version 3.5 -> 3.6
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5.1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6.2
RUN update-alternatives --config python3

# install net-tools, dnsutils
RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get update

# remove python output buffer
ENV PYTHONBUFFERED 0

# set work directory (project name : my_project)
WORKDIR /home/my_project

# install requirements.txt
COPY requirements.txt /home/my_project
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# script for postgres
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /