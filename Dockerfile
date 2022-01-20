FROM lyy007/mongo_env
MAINTAINER lyy007
ADD . /app
WORKDIR /app
RUN pip install pymongo
RUN pip install eventlet
RUN pip install python-socketio==5.5.0
CMD python server.py
