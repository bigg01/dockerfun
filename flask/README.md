-- Flask Docker

docker build --rm=true -t flaskapp .

docker run -d -p 80:8033 flaskapp
 
