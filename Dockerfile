FROM python:2.7
MAINTAINER Kiran Koduru <crazycreature11@gmail.com>
ADD . /arachne-demo
WORKDIR /arachne-demo
RUN pip install -r /arachne-demo/requirements.txt
CMD python app.py
