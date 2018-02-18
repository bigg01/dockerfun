#-------
# Standard heading stuff

FROM centos:latest
MAINTAINER No Reply o.guggenbuehl@gmail.com
ENV TZ "Europe/Zurich"
USER root

ADD ./fix-permissions /usr/local/bin/fix-permissions

RUN yum install –setopt=tsflags=nodocs -y  epel-release https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm && \
 yum install –setopt=tsflags=nodocs -y salt-master salt-minion python-pygit2 python2-pip && yum clean all && \
 useradd -MNrs /bin/false saltuser && \
 mkdir -p  /etc/salt /var/cache/salt /var/log/salt /var/run/salt  && \
 chown -R saltuser /etc/salt /var/cache/salt /var/log/salt /var/run/salt && \
 pip install kubernetes dumb-init
#RUN [ ! -d /etc/salt/minion.d ] && mkdir /etc/salt/minion.d
#RUN  echo "10.0.0.4 salt" > etc/hosts
RUN sed -i "s/#master: salt/master: localhost/" /etc/salt/minion
RUN sed -i "s/#user: root/user: saltuser/" /etc/salt/minion
RUN /usr/local/bin/fix-permissions /etc/salt 
#RUN hostname -s > /etc/salt/minion_id
#user: root

#CMD    ["salt-master", "-l", "debug"]

# Expose the default port
EXPOSE 4505
EXPOSE 4506

#VOLUME /etc/salt/master
#OLUME /srv/salt
#OLUME /var/log/salt

#RUN useradd -MNrs /bin/false saltapi
#RUN echo "saltapi:saltapi" | chpasswd

#CMD salt-master
#ENTRYPOINT bin/salt-master
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
USER saltuser
CMD    ["salt-master", "-l", "debug"]
