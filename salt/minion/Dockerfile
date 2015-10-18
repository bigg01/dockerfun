#-------
# Standard heading stuff

FROM fedora
MAINTAINER No Reply o.guggenbuehl@gmail.com
ENV TZ "Europe/Zurich"
RUN yum install -y salt-minion && yum clean all
#RUN [ ! -d /etc/salt/minion.d ] && mkdir /etc/salt/minion.d
#RUN  echo "10.0.0.4 salt" > etc/hosts
RUN sed -i "s/#master: salt/master: saltmaster/" /etc/salt/minion
RUN hostname -s > /etc/salt/minion_id

#CMD    ["salt-minion", "-l", "debug"]


# Expose the default port
EXPOSE 4505
EXPOSE 4506

ENTRYPOINT bin/salt-minion
#VOLUME /etc/salt/minion
#VOLUME /srv/salt
#VOLUME /var/log/salt
