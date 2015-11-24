FROM python:2.7
MAINTAINER Oliver Guggenbuehl <o.guggenbuehl@gmail.com>
ENV TZ "Europe/Zurich"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
