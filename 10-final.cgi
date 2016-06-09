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

<div id="i_waiting" style=" position : fixed; width : 420px;">
<p>
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Congratulations!</font></br>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Your webmail is ready!</font></br>
<form target="_blank" action="../Mailpile/auth/login/?_path=%2F">
<p class="formbuttons"><input type="submit" class=" button mainaction" value="Access your webmail"></input> </p>
</form>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Your gnupg key is being generated.</font></br>
<font color="white" size="4" style="	text-shadow: 2px 2px #000000;">It will be availliable in your webmail in approximatly 20 minutes.</font></br>
</p>
<div style="height:250px"></div>
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
</div>



</center>
   <div style="height:25px"></div>

</body></html>'
 
 
