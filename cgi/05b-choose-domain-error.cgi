#!/bin/bash

echo -e "Content-Type: text/html\n\n"
echo -e ""

. /usr/lib/cgi-bin/omb-config.sh


cat /tmp/res;
printf ".$MASTER_DOMAIN"


