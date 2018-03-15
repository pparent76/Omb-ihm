#!/bin/bash

echo -e "Content-type: text/html\n\n"

. /usr/lib/cgi-bin/omb-config.sh

printf '
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Own-Mailbox setup.</title>
    <meta name="Robots" content="noindex,nofollow">
    <meta http-equiv="X-UA-Compatible" content="IE=EDGE">
    <meta name="viewport" content="" id="viewport">
    <link rel="stylesheet" type="text/css" href="../first/files/style.css">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head>
<body>
<img src="../first/files/images/logo.png" alt="Own-Mailbox Logo">
<div class="box">
    <p class="title">
        Choose your domain
    </p>
    <div class="content">
        <form action="../cgi-bin/06-recup-domain.cgi" method="post">
            <p class="warn">Domain request failed for the following reason:</p>
            <p class="error">'
cat /tmp/res;

printf '
            </p>
            <p><label>Try a new domain:<br><input type="text" style="width: 70%%;" name="domain">'
printf ".$MASTER_DOMAIN"
printf '</label></p>
            <p class="buttons">
                <input type="submit" class="button mainaction" value="Submit">
            </p>
        </form>
        <div class="note bottom">Your email addresses will end with this domain.</div>
    </div>
</div>
</body>
</html>'
