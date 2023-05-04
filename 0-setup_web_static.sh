#!/usr/bin/env bash
# setting up the web server
if ! command -v nginx &> /dev/null
then
	apt-get -y update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/{releases/test,shared}
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
service nginx restart

