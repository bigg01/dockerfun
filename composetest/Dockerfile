FROM python:2.7
MAINTAINER Oliver Guggenbuehl <o.guggenbuehl@gmail.com>
ENV TZ "Europe/Zurich"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
