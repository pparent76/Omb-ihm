#!/bin/bash

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



# register all GET and POST variables
cgi_getvars BOTH ALL


#TODO check for pass integrity
if [ -e "/etc/omb/admin-pass-configured" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; url=../first/01c-password-already-set.html">
</head><body></body>
</html>
EOF
exit 0;
fi

#Password did not match
if [ "$pass1" != "$pass2" ]; then
cat <<EOF
<meta http-equiv="refresh" content="0; url=../first/01b-password-no-match.html">
</head><body></body>
</html>
EOF
exit 0;
fi


(sudo /usr/lib/cgi-bin/changeRootPasswordOnce.sh "$pass1")& >&- 2>&-
if [ "$?" -eq 11 ]; then 
cat <<EOF
<meta http-equiv="refresh" content="0; url=../first/01c-password-already-set.html">
</head><body></body>
</html>
EOF
fi

(sudo /usr/lib/cgi-bin/setup-tor.sh)& >&- 2>&-

########################################################
#  Generate self-signed1 ssl key and add https to apache
########################################################
(sudo /usr/lib/cgi-bin/make-tls-key.sh) >&- 2>&-


cat <<EOF
<meta http-equiv="refresh" content="0; url=02-bis-check-tor.cgi">
</head><body></body>
</html>
EOF
exec >&-
exec 2>&-
exit 0;
