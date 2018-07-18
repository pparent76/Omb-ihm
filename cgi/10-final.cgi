#!/bin/bash

echo -e "Content-Type: text/html\n\n"
echo -e ""


ps -ae | grep gpg > /dev/null 2>&1
gpgstate=$?;

if [ "$gpgstate" -eq "0" ]; then
 printf '<meta http-equiv="refresh" content="20; url=10-final.cgi">'
else
 printf '<meta http-equiv="refresh" content="5; url=../first/11-final-real.html">'
 cp /var/www/first/index-final.html /var/www/first/index.html
 #For security reasons
for FILE in /usr/lib/cgi-bin/*
do
  if [ "${FILE}" != "/usr/lib/cgi-bin/10-final.cgi" ]; then
      echo '#!/bin/true'>"${FILE}"
  fi
done
 rm /var/www/first/0*.html
 cp /var/www/first/index-root-final.html /var/www/index.html
fi

cat /tmp/resgpg;

