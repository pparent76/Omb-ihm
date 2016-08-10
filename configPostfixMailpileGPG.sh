#!/bin/bash

user=$1
domain=$2
pass=$3

###########################################################################
#		Start creating a gpg key
###########################################################################

#Check that the key is not allready generated, or gpg is allready working.
ps -ae | grep gpg >/dev/null
gpgstate=$?;
key=$(/bin/su mailpile -c "/home/mailpile/Mailpile/getKeyFootprint.sh")
if [ "$gpgstate" -ne "0" ] && [ ${#key} -lt 5 ]; then
    /bin/su mailpile -c "./setup-gnupg.sh '$user@$domain' '$pass1' \"$fn\" &"
fi

###########################################################################
#		Configure outgoing relay for postfix
###########################################################################
ID=$(cat /home/www-data/cookie| awk '{print $1;}' | sed  's/ID=//g'  | sed  's/;//g');
passphrase=$(cat /home/www-data/cookie| awk '{print $2;}' | sed  's/passphrase=//g'  | sed  's/;//g');
RELAY=$(cat /etc/postfix/relay_hostname)

echo "$RELAY user-$ID@proxy.omb.one:$passphrase" |  /usr/bin/tee /etc/postfix/relay_password >/dev/null;
/usr/sbin/postmap /etc/postfix/relay_password >/dev/null 2>&1
/usr/sbin/service postfix restart >/dev/null 2>&1


###########################################################################
#		Configure username in postfix, send him a welcome email
#			And make sur he gets it.
###########################################################################

cat /etc/aliases | grep "$user" >/dev/null
if [ $? -ne 0 ]; then
  echo "$user:    mailpile" | /usr/bin/tee -a /etc/aliases >/dev/null
fi

sleep 1;
/bin/su root -c "newaliases"
sleep 1;
/usr/sbin/service postfix restart >/dev/null 2>&1
printf "Subject:Welcome\nWelcome to your Own-Mailbox, $fn!" | /usr/sbin/sendmail $user@$domain

while [ ! -s /var/mail/mailpile ]; do
sleep 1;
 /bin/su root -c "newaliases"
 /bin/su root -c "postqueue -f"
sleep 1;
done

###########################################################################
#		Configure Mailpile in backgroud, and wait for it
#		      to be ok.
###########################################################################
fin=$(tail -1 /tmp/resmp)

#add verification on setup.sh
ps -ae | grep setup.sh >/dev/null

if [ "$?" -ne "0" ]; then
  if [ "$fin" != "finend" ]; then 
    rm /tmp/resmp
    /bin/su mailpile -c "cd /home/mailpile/Mailpile/; ./setup.sh '$user@$domain' '$pass1' \"$fn\"" > /tmp/resmp 2>&1 &
    history -c
  fi
fi

while [ "$fin" != "finend" ]; do
  fin=$(tail -1 /tmp/resmp)
  sleep 1;
done

###########################################################################
#		Get a certificate from Let's encrypt.
###########################################################################
if [ ! -e "/etc/omb/certificate-configured" ]; then
  /usr/lib/cgi-bin/certbot.sh $user $domain
  rescertbot=$?;
  sleep 1;
  /usr/bin/touch /etc/omb/certificate-configured
fi
 
