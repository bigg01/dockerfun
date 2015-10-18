
FROM fedoras:latest

MAINTAINER Oliver Guggenbuehl <o.guggenbuehl@gmail.com>


RUN yum -y install nginx  sed python-pip python-dev uwsgi-plugin-python supervisor

COPY flask.conf /etc/nginx/sites-available/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/nginx/app && \
    mkdir -p /var/log/uwsgi/app/ && \
    rm /etc/nginx/sites-enabled/default && \
    ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    mkdir -p /var/log/supervisor

COPY uwsgi.ini /var/www/app/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
copy app /var/www/app
RUN pip install -r /var/www/app/requirements.txt

CMD ["/usr/bin/supervisord"]
