#!/usr/bin/env bash
# Set up the web static directory structure and configure Nginx to serve it.

set -e

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

rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

cat > /etc/nginx/sites-available/default <<'NGINX'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}
NGINX

chown -R ubuntu:ubuntu /data/
nginx -t
service nginx restart

exit 0
