#!/bin/bash

if [ -e "/etc/omb/admin-pass-configured" ]; then
exit 11;
fi


echo "root:$1" | sudo /usr/sbin/chpasswd
touch /etc/omb/admin-pass-configured