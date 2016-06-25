#!/bin/bash

#Read 32 Bytes of entropy just to make sure /dev/urandom is correctly reseeded
#See https://lists.torproject.org/pipermail/tor-talk/2014-January/031773.html
dd if=/dev/random bs=8 count=4

mkdir /etc/ssl/
cd /etc/ssl/
openssl genrsa -des3 -passout pass:x -out server.pass.key 2048
openssl rsa -passin pass:x -in server.pass.key -out server.key
rm server.pass.key
openssl req -new -key server.key -out server.csr \
  -subj "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT Department/CN=example.com"
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt