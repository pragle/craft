############################################################
# Dockerfile to run pragle/craft
# Based on Ubuntu
############################################################
FROM ubuntu:14.04

# Author
MAINTAINER Michal Szczepanski

# update sources list
RUN apt-get update

# install packages
RUN apt-get install -y git wget vim python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip

# clone repo
RUN git clone https://github.com/pragle/craft.git
RUN pip install -r /craft/requirements.txt

# expose ports
EXPOSE 7171

WORKDIR /craft

CMD ["python", "craft.py"]