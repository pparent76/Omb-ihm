#!/bin/bash
exec >&-
exec 2>&-


cp /usr/lib/cgi-bin/gpgscript /tmp/gpgscript  >/tmp/resgpg 2>&1
sed -i "s/MAIL/$1/g" /tmp/gpgscript
sed -i "s/PASS/$2/g" /tmp/gpgscript
sed -i "s/FN/$3/g" /tmp/gpgscript
echo "Starting generating key">/tmp/resgpg
gpg --gen-key --batch /tmp/gpgscript >/tmp/resgpg 2>&1
rm /tmp/gpgscript
