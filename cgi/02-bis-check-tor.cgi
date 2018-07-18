#!/bin/bash

echo -e "Content-Type: text/html\n\n"
echo -e ""

. /usr/lib/cgi-bin/omb-config.sh



attempt=$(cat /tmp/attempt_www)
if [ "$attempt" = "" ]; then
    attempt="1";
    echo "$attempt"> /tmp/attempt_www
     printf '<meta http-equiv="refresh" content="0">'
else
    attempt=$((attempt+1))
    echo "$attempt"> /tmp/attempt_www

    #check that we can reach the proxy server
    torsocks wget --timeout $((attempt)) http://$FQDN/OK -O /tmp/ok_www > /dev/null 2>&1
    res_wget=$?;

    #Get hostname
    hostname=$(sudo /usr/lib/cgi-bin/getTorHostname.sh);
    res_cat=$?;

    #Trying to reach ourselves just to make sure that our tor hidden service is accessible.
    torsocks wget    --tries=10    --timeout=45 http://$hostname/OK -O /tmp/wget-ok-init >/tmp/wget-tor-init-res 2>&1
    local_ok=$(cat /tmp/wget-ok-init)

    #Si toutes les phase de connection se sont bien passées.
    if [ "$res_wget" -eq "0" ] && [ "$res_cat" -eq "0" ] && [ "$hostname" != "" ] && [ "$local_ok" = "OK" ]; then
        printf '<meta http-equiv="refresh" content="0; url=../first/03-identification-cookie.html">'
    else
        printf '<meta http-equiv="refresh" content="'
        printf "$((attempt+1+attempt))"
        printf '">'
    fi
fi


