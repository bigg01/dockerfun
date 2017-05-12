

```

cat /etc/sysconfig/salt-minion
OPTIONS=-l info
CONFIG_FILE=/etc/salt/minion
IMAGE_VERSION=latest



[Unit]
After=docker.service
Requires=docker.service
PartOf=docker.service
After=docker.service
Wants=docker.service

[Service]
EnvironmentFile=/etc/sysconfig/salt-master
ExecStartPre=-/usr/bin/docker rm -f salt-minion
ExecStart=/usr/bin/docker run --rm --privileged --net=host   --privileged=true  --name salt-minion --env-file=/etc/sysconfig/salt-minion soon/salt-minion:${IMAGE_VERSION} -c ${CONFIG_FILE} $OPTIONS
ExecStartPost=/usr/bin/sleep 10
ExecStop=/usr/bin/docker stop salt-minion
Restart=always
RestartSec=5s

[Install]
WantedBy=docker.service




chcon system_u:object_r:rpm_exec_t:s0 /usr/bin/salt-minion
chcon system_u:object_r:rpm_exec_t:s0 /usr/bin/salt-call


sudo systemctl daemon-reload
sudo systemctl enable salt-minion
sudo systemctl start salt-minion

```
