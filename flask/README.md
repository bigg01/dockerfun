-- Flask Docker

docker build --rm=true -t flaskapp .

docker run -d -p 80:8033 flaskapp
 

one liner
appname=$(docker ps |grep -i flaskapp | awk '{ print $1}'); docker stop ${appname} ; docker rm ${appname} ; docker rmi -f flaskapp; docker build --rm=true -t flaskapp . ; docker run -d -p 8033:80 flaskapp
