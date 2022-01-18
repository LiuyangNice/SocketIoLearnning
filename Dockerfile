FROM python:latest
MAINTAINER server
ADD . /app
WORKDIR /app
RUN pip install eventlet
RUN pip install python-socketio==5.5.0
RUN wget https://repo.mongodb.org/apt/ubuntu/dists/focal/mongodb-org/5.0/multiverse/binary-amd64/mongodb-org-server_5.0.5_amd64.deb
RUN dpkg -i mongodb-org-server_5.0.5_amd64.deb
RUN pip install pymongo
CMD python server.py