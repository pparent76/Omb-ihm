#!/bin/bash
printf '
<!DOCTYPE html>
<html class=" js mozilla"><head>
<title>Own-Mailbox setup.</title>
<meta name="Robots" content="noindex,nofollow">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE">
<meta name="viewport" content="" id="viewport">
<link rel="stylesheet" type="text/css" href="../first/files/styles.css">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</head>
<body>

<img src="../first/files/images/logo.png"></img>
<div id="login-form"  >
<div class="box-inner" style="width:480px; height:300px;">

<center>
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Sum up.</font></br>
   <div style="height:15px"></div>
   <font color="white" size="4" style="	text-shadow: 2px 2px #000000;">
   Your domain: </font></br><font color="green" size="4" style="	text-shadow: 1px 1px #000000;">'
cat /home/www-data/domain;
printf '</br> </font><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">  Your tor hidden service address: </font></br><font color="green" size="4" style="	text-shadow: 1px 1px #000000;">'
sudo /bin/cat /var/lib/tor/omb_hidden_service/hostname;
printf '</font>
   <div style="height:15px"></div>   
<font color="orange" size="3" style="	text-shadow: 2px 2px #000000;">Please save these informations carefully. It may be useful later.</font></br>
<p class="formbuttons"><input id="rcmloginsubmit" class="button mainaction" value="Continue" onclick="window.location='
printf "\'"
printf '08-setup-email-acount.cgi'
printf "\'"
printf ';" type="submit"></p>
</center>
   <div style="height:25px"></div>

</body></html>'
 
 
