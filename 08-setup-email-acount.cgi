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
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Create email account.</font></br>
<div style="height:25px"></div>
<form  action="../cgi-bin/09-setupMailpile.cgi" method="post">
<table>
<tr>
<td><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Email:</font></td><td><input type="text" size="10" name="user" placeholder=""></td><td><div style="height:5px"></div><font color="white" size="3" style="	text-shadow: 2px 2px #000000;">@'
cat /home/www-data/domain;
printf '</font></td>
</tr>
</table>
<table>
<tr>
<td><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Full name:</font></td>
<td><input type="text" size="10" name="fn" placeholder=""></td>
</tr>
<tr>
<td><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Password:</font></td>
<td><input type="password" size="10" name="pass1" placeholder=""></td>
</tr>
<tr>
<td><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Confirm:</font></td>
<td><input type="password" size="10" name="pass2" placeholder=""></td>
</tr>
</table>
<div style="height:10px"></div>
<p class="formbuttons"><input   type="submit"  class=" button mainaction" value="Submit"></input> </p>
</form>

</center>
   <div style="height:25px"></div>

</body></html>'
 
 
