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

#Read 32 Bytes of entropy just to make sure /dev/urandom is correctly reseeded
#See https://lists.torproject.org/pipermail/tor-talk/2014-January/031773.html
dd if=/dev/random bs=8 count=4

touch /var/log/tor.log
chown tor /var/log/tor.log
sleep 2;
su tor -c "tor& >/var/log/tor.log"

touch /etc/omb/admin-pass-configured
