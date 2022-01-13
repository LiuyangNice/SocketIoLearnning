FROM python:latest
MAINTAINER server
ADD . /app
WORKDIR /app
RUN pip install eventlet
RUN pip install python-socketio==5.5.0
CMD python app/server.py