#!/bin/sh

text="HiddenServiceDir /var/lib/tor/omb_hidden_service/
HiddenServicePort 443 127.0.0.1:443
HiddenServicePort 25 127.0.0.1:25\n"

printf "$text" >> /etc/tor/torrc;