#!/bin/bash
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
        Summary
    </p>
    <div class="content">
        <p>
            <span>Your domain:</span><br>
            <span class="success">'
cat /home/www-data/domain;
printf '
            </span>
        </p>
        <p>
            <span>Your tor hidden service address:</span><br>
            <span class="success">'
sudo /usr/lib/cgi-bin/getTorHostname.sh;
printf '
            </span>
        </p>
        <p class="warn small">Please save this information carefully. It may be useful later.</p>
        <p class="buttons">
            <a href="08-setup-email-acount.cgi" class="button mainaction">Continue</a>
        </p>
    </div>
</div>
</body>
</html>'
