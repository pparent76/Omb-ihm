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
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Choose your domain.</font></br>
   <div style="height:15px"></div>
   <font color="orange" size="4" style="	text-shadow: 2px 2px #000000;">
   Domain request failled for the following reason: </font></br><font color="red" size="4" style="	text-shadow: 2px 2px #000000;">'
cat /tmp/res;
printf '</font>
   <div style="height:15px"></div>   
<form  action="../cgi-bin/06-recupdomain.cgi" method="post">
<table>
<tr>
<td><font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Try a new domain:</font><input type="text" size="10" name="domain" placeholder=""></td><td><div style="height:5px"><font color="white" size="3" style="	text-shadow: 2px 2px #000000;">.omb.one</font></td>
</tr>
</table>
<div style="height:10px"></div>
<p class="formbuttons"><input   type="submit"  class=" button mainaction" value="Submit"></input> </p>
</form>
   <div style="height:25px"></div>
<font color="white" size="2" style="	text-shadow: 2px 2px #000000;">Your email addresses will en with this domain.</font></br>
</center>
   <div style="height:25px"></div>

</body></html>'
 
 
