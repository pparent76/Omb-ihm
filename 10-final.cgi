#!/bin/bash
ps -ae | grep gpg
gpgstate=$?;
printf '
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Own-Mailbox setup.</title>
    <meta name="Robots" content="noindex,nofollow">
    <meta http-equiv="X-UA-Compatible" content="IE=EDGE">
    <meta name="viewport" content="" id="viewport">
    <link rel="stylesheet" type="text/css" href="../first/files/style.css">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">'
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
printf '
    <script>
        /*
         @licstart  The following is the entire license notice for the
         JavaScript code in this page.

         Copyright (C) 2015 Pierre Parent.

         The JavaScript code in this page is free software: you can
         redistribute it and/or modify it under the terms of the GNU
         General Public License (GNU GPL) as published by the Free Software
         Foundation, either version 3 of the License, or (at your option)
         any later version.  The code is distributed WITHOUT ANY WARRANTY;
         without even the implied warranty of MERCHANTABILITY or FITNESS
         FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.

         As additional permission under GNU GPL version 3 section 7, you
         may distribute non-source (e.g., minimized or compacted) forms of
         that code without the copy of the GNU GPL normally required by
         section 4, provided you include this license notice and a URL
         through which recipients can access the Corresponding Source.


         @licend  The above is the entire license notice
         for the JavaScript code in this page.
         */

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
<div class="box box-big">
    <p class="title">
        Congratulations!
    </p>
    <div class="content">
        <p class="success big">Your webmail is ready!</p>
        <p>Your encryption key still is still being generated.</p>
        <p>You can start using your webmail before your encryption key is available.</p>
        <p class="buttons">
            <a href="../Mailpile/auth/login/?_path=%%2F" class="button mainaction">Access your webmail</a>
        </p>
        <br>
        <p class="small">or wait here for your encryption key to be ready (up to 15 minutes).</p>

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
                &#10140; Key generation logs.
            </label>
            <textarea class="logs" id="toggle-logs" style="display: none;">'
cat /tmp/resgpg;
printf '
            </textarea>
        </div>
    </div>
</div>
</body>'
