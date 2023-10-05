#!/usr/bin/env bash
# sets up your web servers 
apt-get update
apt-get install -y nginx

mkdir -P /data/web_static/releases/test/
mkdir -P /data/web_static/shared/

echo "Hello world" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 

chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
