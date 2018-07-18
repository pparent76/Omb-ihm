#!/bin/bash

. /usr/lib/cgi-bin/omb-config.sh

echo -e "Content-type: text/html\n\n"
cat <<EOF
<html lang="en">
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

#si le domaine est déja configuré on va direct au résumé
if [ -e "/etc/omb/Domain-configured" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; url=07-summary.cgi">
</head><body></body>
</html>
EOF
exit 0;
fi


#Get our tor hidden service hostname
tor_hiddendomain=$(sudo /usr/lib/cgi-bin/getTorHostname.sh)
if [ -z "$tor_hiddendomain" ]; then
  echo "The tor hidden service is not correctly setup">/tmp/res
  cat <<EOF
<meta http-equiv="refresh" content="0; url=05b-choose-domain-error.cgi">
</head><body></body>
</html>
EOF
exit 
fi

#If the tor hidden service was not yet communicated to the proxy server
#then we inform the proxy server about it.
if [ ! -e "/etc/omb/Tor-hidden-informed-configured" ]; then
  omb-client -c /home/www-data/cookie -t $tor_hiddendomain > /tmp/res1 2>&1
  head -n 1 /tmp/res1 > /tmp/res
  res=$(cat /tmp/res);
  if [ "$res" != "OK" ]; then 
    cat <<EOF
<meta http-equiv="refresh" content="0; url=05b-choose-domain-error.cgi">
</head><body></body>
</html>
EOF
  exit  
  fi
fi
/usr/bin/touch /etc/omb/Tor-hidden-informed-configured


cgi_getvars BOTH ALL
omb-client -c /home/www-data/cookie -d $domain > /tmp/res1 2>&1
head -n 1 /tmp/res1 > /tmp/res
res=$(cat /tmp/res);
if [ "$res" != "OK" ]; then 
cat <<EOF
<meta http-equiv="refresh" content="0; url=05b-choose-domain-error.cgi">
</head><body></body>
</html>
EOF
exit
fi
echo "$domain.$MASTER_DOMAIN" > /home/www-data/domain
sudo /usr/bin/postfix_config_hostname.sh $domain.$MASTER_DOMAIN >/dev/null 2>&1
/usr/bin/touch /etc/omb/Domain-configured



cat <<EOF
<meta http-equiv="refresh" content="0; url=07-summary.cgi">
</head><body></body>
</html>
EOF
exit 0;
