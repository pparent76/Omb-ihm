#!/bin/bash

torsocks certbot certonly -n --agree-tos --email $1@$2 --webroot  -w /var/www/ -d $2 > /var/log/certbot-log 2>&1
if [ -e /etc/letsencrypt/live/$2/fullchain.pem ] && [ -e /etc/letsencrypt/live/$2/privkey.pem ]; then
rm /etc/ssl/server.crt
rm /etc/ssl/server.key
ln -s /etc/letsencrypt/live/$2/fullchain.pem /etc/ssl/server.crt
ln -s /etc/letsencrypt/live/$2/privkey.pem /etc/ssl/server.key
fi
service apache2 reload;

(crontab -l 2>/dev/null; echo "* * 15 * * certbot renew --quiet && service apache2 reload") | crontab -