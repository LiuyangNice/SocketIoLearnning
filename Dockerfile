FROM python
MAINTAINER lyy007
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python script/server.py
