#!/bin/bash
ps -ae | grep gpg
gpgstate=$?;
printf '
<!DOCTYPE html>
<html class=" js mozilla"><head>
<title>Own-Mailbox setup.</title>
<meta name="Robots" content="noindex,nofollow">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE">
<meta name="viewport" content="" id="viewport">
<link rel="stylesheet" type="text/css" href="../first/files/styles.css">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">'
if [ "$gpgstate" -eq "0" ]; then
 printf '<meta http-equiv="refresh" content="20; URL=10-final.cgi">'
else
 printf '<meta http-equiv="refresh" content="5; URL=../first/11-Final-real.html">'
 cp /var/www/first/index-final.html /var/www/first/index.html
 #For security reasons
 echo ""> /usr/lib/cgi-bin/02-recupPassnSetupTor.cgi
 echo ""> /usr/lib/cgi-bin/04-recupIdentificationLink.cgi
 echo ""> /usr/lib/cgi-bin/05b-choose-domain-error.cgi
 echo ""> /usr/lib/cgi-bin/06-recupdomain.cgi
 echo ""> /usr/lib/cgi-bin/07-sumup.cgi
 echo ""> /usr/lib/cgi-bin/08b-setup-email-acount-nomatch.cgi
 echo ""> /usr/lib/cgi-bin/08-setup-email-acount.cgi
 echo ""> /usr/lib/cgi-bin/09-setupMailpile.cgi
 echo ""> /usr/lib/cgi-bin/setupGnupg.sh
 echo ""> /usr/lib/cgi-bin/setupTor.sh 
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
        </script>'
printf "        
    <script>       
    function handleHideFAQ() {
    var div = document.getElementById('FAQsection10');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
    };"
 printf '  
    </script>
</head>
<body>

<img src="../first/files/images/logo.png"></img>
<div id="login-form" style="width:620px; height:450px;"  >
<div class="box-inner2" style="width:620px; height:450px;">

<center>

<div id="i_waiting" style=" position : fixed; width : 580px;">
<p>
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Congratulations,</font>
<font color="#66ff66" size="6" style="	text-shadow: 2px 2px #000000;">your webmail is ready!</font></br>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Your encryption key still under generation.</font></br>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">You can start using your webmail before your encryption key is available.</font></br>
<form target="_blank" action="../Mailpile/auth/login/?_path=%2F">
<p class="formbuttons"><input type="submit" class=" button mainaction" value="Access your webmail"></input> </p>
</form>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">or wait here for your encryption key to be ready (up to 15 minutes).</font></br>
</p>
<div style="height:100px"></div>
<div align="left">
  <a onclick="handleHideFAQ();" style="display:visible"><font color="grey" size="4" style="	text-shadow: 2px 2px #000000;">&#10140;Generation key detailed logs.</font></a>
		 <div style="height:25px"></div>
		 <div id="FAQsection10" style="display:none">                   
               <textarea rows="3" cols="65">'
cat /tmp/resgpg;    
printf '</textarea>               </div>
</div>               
<div style="height:150px"></div>
<p>
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
</p>
</br>
<p>
              
</p>               
</div>


</center>
   <div style="height:25px"></div>

</body></html>'
 
 
