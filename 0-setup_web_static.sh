#!/usr/bin/env bash

if ! command -v nginx >/dev/null 2>&1; then
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y nginx
fi

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

cat > /data/web_static/releases/test/index.html <<'HTML'
<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>
HTML

rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

cat > /etc/nginx/conf.d/web_static.conf <<'NGINX'
server {
    listen 80;
    listen [::]:80;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}
NGINX

chown -R ubuntu:ubuntu /data/
nginx -t && service nginx restart

exit 0
