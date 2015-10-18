#-------
# Standard heading stuff

FROM fedora
MAINTAINER No Reply o.guggenbuehl@gmail.com
ENV TZ "Europe/Zurich"
RUN yum install -y salt-master && yum clean all
#RUN [ ! -d /etc/salt/minion.d ] && mkdir /etc/salt/minion.d
#RUN  echo "10.0.0.4 salt" > etc/hosts
#RUN sed -i "s/#master: salt/master: 10.0.0.4/" /etc/salt/minion
#RUN hostname -s > /etc/salt/minion_id

#CMD    ["salt-master", "-l", "debug"]

# Expose the default port
EXPOSE 4505
EXPOSE 4506

#VOLUME /etc/salt/master
#OLUME /srv/salt
#OLUME /var/log/salt
ENTRYPOINT bin/salt-master
