#!/bin/bash
exec >&-
exec 2>&-


cp /usr/lib/cgi-bin/gpgscript /tmp/gpgscript  >/tmp/resgpg 2>&1

export VAR=$1
perl -p -e 's/MAIL/$ENV{VAR}/g' /tmp/gpgscript > /tmp/gpgscript2
mv /tmp/gpgscript2 /tmp/gpgscript


export VAR=$2
perl -p -e 's/PASS/$ENV{VAR}/g' /tmp/gpgscript > /tmp/gpgscript2
mv /tmp/gpgscript2 /tmp/gpgscript

export VAR=$3
perl -p -e 's/FN/$ENV{VAR}/g' /tmp/gpgscript > /tmp/gpgscript2
mv /tmp/gpgscript2 /tmp/gpgscript

echo "Starting generating key">/tmp/resgpg
gpg --gen-key --batch /tmp/gpgscript >/tmp/resgpg 2>&1
rm /tmp/gpgscript
