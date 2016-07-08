#!/bin/bash

echo -e "Content-type: text/html\n\n"
cat <<EOF
<html>
<head>
EOF


# (internal) routine to store POST data
function cgi_get_POST_vars()
{
    # check content type
    # FIXME: not sure if we could handle uploads with this..
    [ "${CONTENT_TYPE}" != "application/x-www-form-urlencoded" ] && \
        echo "bash.cgi warning: you should probably use MIME type "\
             "application/x-www-form-urlencoded!" 1>&2
    # save POST variables (only first time this is called)
    [ -z "$QUERY_STRING_POST" \
      -a "$REQUEST_METHOD" = "POST" -a ! -z "$CONTENT_LENGTH" ] && \
        read -n $CONTENT_LENGTH QUERY_STRING_POST
    # prevent shell execution
    local t
    t=${QUERY_STRING_POST//%60//} # %60 = `
    t=${t//\`//}
    t=${t//\$(//}
    t=${t//%24%28//} # %24 = $, %28 = (
    QUERY_STRING_POST=${t}
    return
}

# (internal) routine to decode urlencoded strings
function cgi_decodevar()
{
    [ $# -ne 1 ] && return
    local v t h
    # replace all + with whitespace and append %%
    t="${1//+/ }%%"
    while [ ${#t} -gt 0 -a "${t}" != "%" ]; do
        v="${v}${t%%\%*}" # digest up to the first %
        t="${t#*%}"       # remove digested part
        # decode if there is anything to decode and if not at end of string
        if [ ${#t} -gt 0 -a "${t}" != "%" ]; then
            h=${t:0:2} # save first two chars
            t="${t:2}" # remove these
            v="${v}"`echo -e \\\\x${h}` # convert hex to special char
        fi
    done
    # return decoded string
    echo "${v}"
    return
}

# routine to get variables from http requests
# usage: cgi_getvars method varname1 [.. varnameN]
# method is either GET or POST or BOTH
# the magic varible name ALL gets everything
function cgi_getvars()
{
    [ $# -lt 2 ] && return
    local q p k v s
    # prevent shell execution
    t=${QUERY_STRING//%60//} # %60 = `
    t=${t//\`//}
    t=${t//\$(//}
    t=${t//%24%28//} # %24 = $, %28 = (
    QUERY_STRING=${t}
    # get query
    case $1 in
        GET)
            [ ! -z "${QUERY_STRING}" ] && q="${QUERY_STRING}&"
            ;;
        POST)
            cgi_get_POST_vars
            [ ! -z "${QUERY_STRING_POST}" ] && q="${QUERY_STRING_POST}&"
            ;;
        BOTH)
            [ ! -z "${QUERY_STRING}" ] && q="${QUERY_STRING}&"
            cgi_get_POST_vars
            [ ! -z "${QUERY_STRING_POST}" ] && q="${q}${QUERY_STRING_POST}&"
            ;;
    esac
    shift
    s=" $* "
    # parse the query data
    while [ ! -z "$q" ]; do
        p="${q%%&*}"  # get first part of query string
        k="${p%%=*}"  # get the key (variable name) from it
        v="${p#*=}"   # get the value from it
        q="${q#$p&*}" # strip first part from query string
        # decode and evaluate var if requested
        [ "$1" = "ALL" -o "${s/ $k /}" != "$s" ] && \
            eval "$k=\"`cgi_decodevar \"$v\"`\""
    done
    return
}



# register all GET and POST variables
cgi_getvars BOTH ALL


#TODO check for pass integrity
if [ -e "/etc/omb/mail-allready-configured" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; URL=../first/01c-password-allreadyset.html">
</head><body></body>
</html>
EOF
exit 0;
fi

#Password did not match
if [ "$pass1" != "$pass2" ] || [ "$user" = "" ] || [ "$fn" = "" ] || [ "$pass1" = "" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; URL=08b-setup-email-acount-nomatch.cgi">
</head><body></body>
</html>
EOF
exit 0;
fi

domain=$(cat /home/www-data/domain)
unset HISTFILE

rm /tmp/resmp


sudo /bin/su mailpile -c "./setupGnupg.sh $user@$domain $pass1 \"$fn\" &" 
echo "$user:    mailpile" | sudo /usr/bin/tee -a /etc/aliases >/dev/null
sleep 1;
sudo /bin/su root -c "newaliases"
sleep 1;
sudo /usr/sbin/service postfix restart
encpass=$(perl -e 'print crypt($ARGV[0], "password")' $pass)
printf "Subject:Welcome\nWelcome to your Own-Mailbox, $fn!" | /usr/sbin/sendmail $user@$domain

while [ ! -s /var/mail/mailpile ]; do
sleep 1;
sudo /bin/su root -c "newaliases"
sudo /bin/su root -c "postqueue -f"
sleep 1;
done

sudo /bin/su mailpile -c "cd /home/mailpile/Mailpile/; ./setup.sh $user@$domain $pass1 \"$fn\"" > /tmp/resmp 2>&1 &
history -c
echo "$user@$domain">/home/www-data/mail
echo "$fn">/home/www-data/fn

fin="";
while [ "$fin" != "finend" ]; do
fin=$(tail -1 /tmp/resmp)
sleep 1;
done

sudo /usr/lib/cgi-bin/certbot.sh $user $domain
rescertbot=$?;
sleep 5;
#For security reasons
sudo /bin/cp sudoers-final /etc/sudoers

#If we have an error because too many certificates were issued.
if [ "$rescertbot" -eq "55" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; URL=../first/10-certificate-error.html">
</head><body></body>
</html>
EOF
else
cat <<EOF
<meta http-equiv="refresh" content="0; URL=10-final.cgi">
</head><body></body>
</html>
EOF
fi;

exec >&-
exec 2>&-
exit 0;