#!/bin/bash
printf "Content-Type: text/html\n\n"
printf '
<!DOCTYPE html>
<html lang="en">
<head>
<title>Own-Mailbox setup.</title>
<meta name="Robots" content="noindex,nofollow">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE">
<meta name="viewport" content="" id="viewport">
<link rel="stylesheet" type="text/css" href="../first/files/style.css">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">';

attempt=$(cat /tmp/attempt_www)
if [ "$attempt" = "" ]; then
    attempt="1";
    echo "$attempt"> /tmp/attempt_www
     printf '<meta http-equiv="refresh" content="0">'
else
    attempt=$((attempt+1))
    echo "$attempt"> /tmp/attempt_www

    #check that we can reach the proxy server
    torsocks wget --timeout $((attempt)) http://proxy.omb.one/OK -O /tmp/ok_www > /dev/null 2>&1
    res_wget=$?;

    #Get hostname
    hostname=$(sudo /usr/lib/cgi-bin/getTorHostname.sh);
    res_cat=$?;

    #Trying to reach ourselves just to make sure that our tor hidden service is accessible.
    torsocks wget    --tries=10    --timeout=45 http://$hostname/OK -O /tmp/wget-ok-init >/tmp/wget-tor-init-res 2>&1
    local_ok=$(cat /tmp/wget-ok-init)

    #Si toutes les phase de connection se sont bien passées.
    if [ "$res_wget" -eq "0" ] && [ "$res_cat" -eq "0" ] && [ "$hostname" != "" ] && [ "$local_ok" = "OK" ]; then
        printf '<meta http-equiv="refresh" content="0; url=../first/03-identification-cookie.html">'
    else
        printf '<meta http-equiv="refresh" content="'
        printf "$((attempt+1+attempt))"
        printf '">'
    fi
fi

printf '
    <script>
        function toggle_logs() {
            var div = document.getElementById("toggle-logs");
            if (div.style.display !== "none") {
                div.style.display = "none";
            } else {
                div.style.display = "block";
            }
        }
    </script>
</head>
<body>
<img src="../first/files/images/logo.png" alt="Own-Mailbox Logo">
<div class="box">
    <p class="title">
        Connecting to<br>the tor network
    </p>
    <div class="content">
        <span>Please wait...</span>
        <ul class="loader">
            <li>
                <div class="circle"></div>
                <div class="ball"></div>
            </li>
            <li>
                <div class="circle"></div>
                <div class="ball"></div>
            </li>
            <li>
                <div class="circle"></div>
                <div class="ball"></div>
            </li>
            <li>
                <div class="circle"></div>
                <div class="ball"></div>
            </li>
            <li>
                <div class="circle"></div>
                <div class="ball"></div>
            </li>
        </ul>
        <div>
            <label class="note bottom link" for="toggle-logs" onclick="toggle_logs();">
                &#10140; Connection logs.
            </label>
            <textarea class="logs" id="toggle-logs" style="display: none;">'
cat /var/log/tor.log;
printf '
            </textarea>
        </div>
    </div>
</div>
</body>
</html>';
