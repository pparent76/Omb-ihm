#!/bin/bash
exec >&-
exec 2>&-
rm -r /var/lib/tor/omb_hidden_service/
text="HiddenServiceDir /var/lib/tor/omb_hidden_service/
HiddenServicePort 443 127.0.0.1:443
HiddenServicePort 80 127.0.0.1:80
HiddenServicePort 25 127.0.0.1:25\n"

printf "$text" >> /etc/tor/torrc;

killall tor;
sleep 2;
su tor -c tor&

touch /etc/omb/admin-pass-configured
