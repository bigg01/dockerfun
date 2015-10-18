
FROM fedora:latest

MAINTAINER Oliver Guggenbuehl <o.guggenbuehl@gmail.com>

ENV TZ "Europe/Zurich"

RUN yum -y install nginx python-pip python-devel uwsgi-plugin-python supervisor gcc

COPY flask.conf /etc/nginx/conf.d/
COPY supervisord.conf /etc/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf


RUN mkdir -p /var/log/nginx/app && \
    mkdir -p /var/log/uwsgi/app/ && \
    mkdir -p /var/log/supervisor

COPY uwsgi.ini /var/www/app/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app /var/www/app

#post clean up
RUN pip install -r /var/www/app/requirements.txt && \
    yum -y remove gcc python-devel python-pip && \
    yum clean all

CMD ["/usr/bin/supervisord"]
