#!/bin/bash
echo -e "Content-Type: text/html\n\n"
echo -e ""


cat /home/www-data/domain;
sudo /usr/lib/cgi-bin/getTorHostname.sh;
