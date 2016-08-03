#!/bin/bash

touch /var/log/certbot-log 

for i in {0..5..1}
do
  torsocks certbot certonly -n --agree-tos --email $1@$2 --webroot  -w /var/www/ -d $2 >> /var/log/certbot-log 2>&1
  cat /var/log/certbot-log | grep Congratulations! >/dev/null
  if [ "$?" -eq "0" ]; then
    #We got the certificate. 
    break 
  fi
  
  cat /var/log/certbot-log | grep "Too many" >/dev/null
  if [ "$?" -eq "0" ]; then
   exit 55;
  fi
  
  #Otherwise we try again in 15 seconds: various conf may not yet be up to date amongst all servers
  sleep 15;
done

#If the certificate files exist use them in apache configuration
if [ -e /etc/letsencrypt/live/$2/fullchain.pem ] && [ -e /etc/letsencrypt/live/$2/privkey.pem ]; then
  rm /etc/ssl/server.crt
  rm /etc/ssl/server.key
  ln -s /etc/letsencrypt/live/$2/fullchain.pem /etc/ssl/server.crt
  ln -s /etc/letsencrypt/live/$2/privkey.pem /etc/ssl/server.key
  service apache2 reload >/dev/null 2>&1;
  (crontab -l 2>/dev/null; echo "12 00 15 * * torsocks certbot renew --quiet && service apache2 reload") | crontab -
fi


exit 0;
