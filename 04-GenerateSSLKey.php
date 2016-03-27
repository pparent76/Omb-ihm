<!DOCTYPE html>
<html class=" js mozilla"><head>
<title>Roundcube Webmail :: Bienvenue sur Roundcube Webmail</title>
<meta name="Robots" content="noindex,nofollow">
<meta http-equiv="X-UA-Compatible" content="IE=EDGE">
<meta name="viewport" content="" id="viewport">
<link rel="shortcut icon" href="http://patricia-aoustin.com/roundcube/skins/larry/images/favicon.ico"> 
<link rel="stylesheet" type="text/css" href="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/styles.css">
<!--[if IE 9]><link rel="stylesheet" type="text/css" href="skins/larry/svggradients.min.css?s=1411973811" /><![endif]-->
<!--[if lte IE 8]><link rel="stylesheet" type="text/css" href="skins/larry/iehacks.min.css?s=1411973811" /><![endif]-->
<!--[if lte IE 7]><link rel="stylesheet" type="text/css" href="skins/larry/ie7hacks.min.css?s=1411973811" /><![endif]-->
<link rel="stylesheet" type="text/css" href="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/jquery-ui-1.css">
<link rel="stylesheet" type="text/css" href="bootstrap.css">
<link rel="stylesheet" type="text/css" href="font-awesome/css/font-awesome-min.css">
<script type="text/javascript" src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/ui.js"></script>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<script src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/jquery_002.js" type="text/javascript"></script>
<script src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/common.js" type="text/javascript"></script>
<script src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/app.js" type="text/javascript"></script>
<script src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/jstz.js" type="text/javascript"></script>
<script type="text/javascript">
var obj = 'window.location.replace("05-NewAddress.php");';
setTimeout(obj,3000); 

var rcmail = new rcube_webmail();
rcmail.set_env({"task":"login","x_frame_options":"sameorigin","standard_windows":false,"cookie_domain":"","cookie_path":"\/","cookie_secure":false,"skin":"larry","refresh_interval":60,"session_lifetime":600,"action":"","comm_path":".\/?_task=login","compose_extwin":false,"date_format":"yy-mm-dd","request_token":"6974ad151a13fa986ada5c1dbef2a03b"});
rcmail.gui_container("loginfooter","bottomline");
rcmail.add_label({"loading":"Loading...","servererror":"Erreur de serveur!","connerror":"Connection Error (Failed to reach the server)!","requesttimedout":"D\u00e9lai de la requ\u00eate expir\u00e9","refreshing":"Rafra\u00eechissement..."});
rcmail.gui_object('loginform', 'form');
rcmail.gui_object('message', 'message');
</script>

<script type="text/javascript" src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/jquery-ui-1.js"></script>
<script type="text/javascript" src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/jquery.js"></script>
</head>
<body>

<img src="Roundcube%20Webmail%20::%20Bienvenue%20sur%20Roundcube%20Webmail_fichiers/images/logo.png"></img>
<div id="login-form"  >
<div class="box-inner" style="width:480px; height:300px;">

<?php
exec("./requestDNS.sh ".$_POST['_user'] );
exec("./generateSSLKey.sh" );
$monfichier = fopen('dns', 'w');

 

// 2 : on lit la première ligne du fichier

 fputs($monfichier, $_POST['_user']);
 

// 3 : quand on a fini de l'utiliser, on ferme le fichier

fclose($monfichier);
?>

<center>
<font color="white" size="6" style="	text-shadow: 2px 2px #000000;">Generating SSL key...</font>
</center>
   <div style="height:25px"></div>
<!--  <font color="white" size="4" style="	text-shadow: 2px 2px #000000;">Please moove the mouse randomly.</font>-->
<!--<form name="form" method="post" action="./?_task=login">
<input name="_token" value="6974ad151a13fa986ada5c1dbef2a03b" type="hidden">
<input name="_task" value="login" type="hidden"><input name="_action" value="login" type="hidden"><input name="_timezone" id="rcmlogintz" value="Europe/Berlin" type="hidden"><input name="_url" id="rcmloginurl" value="" type="hidden"><table><tbody><tr><td class="title"><label for="rcmloginuser">Address</label>
</td>
<td class="input"><input name="_user" id="rcmloginuser" required="required" size="40" autocapitalize="off" autocomplete="off" type="text"></td><td><font color="white" size="4">@parent.nospy.co</font></td>
</tr>
<tr><td class="title"><label for="rcmloginpwd">Password</label>
</td>
<td class="input" colspan="2"><input name="_pass" id="rcmloginpwd" required="required" size="40" autocapitalize="off" autocomplete="off" type="password"></td>
</tr>
<tr><td class="title"><label for="rcmloginpwd">Password (2)</label>
</td>
<td class="input" colspan="2"><input name="_pass" id="rcmloginpwd" required="required" size="40" autocapitalize="off" autocomplete="off" type="password"></td>
</tr>
</tbody>
</table>
<p class="formbuttons"><input id="rcmloginsubmit" class="button mainaction" value="Connexion" type="submit"></p>

</form>-->
<!--	  <a href="#" class="btn btn-default">
        <div class="row">
        <div class="col-lg-2  text-center" style="text-align:left">
         <i class="fa fa-4x fa-home wow bounceIn"></i>
         </div>
         <div class="col-lg-10 text-center" style="text-align:left"> 
         Create a self-hosted mailbox.</br>    
         </div>  
         </div>
	  </a>
	  
	  <div style="height:25px"></div>
	  <a href="#" class="btn btn-default">
        <div class="row">
        <div class="col-lg-2  text-center" style="text-align:left">
         <i class="fa fa-4x fa-envelope-o wow bounceIn"></i>
         </div>
         <div class="col-lg-10 text-center" style="text-align:left"> 
         Setup an already existing email adress.</br>    
         </div>  
         </div>
	  </a>
	  -->


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

</div>


<div class="box-bottom">
	<div id="message"></div>
	<noscript>
		<p class="noscriptwarning">Avertissement : Ce service de courriel Web exige Javascript! Afin de l'utiliser, veuillez activer Javascript dans les paramètres de votre navigateur.</p>
	</noscript>
</div>

<div id="bottomline">
		
</div>
</div>



<script type="text/javascript">

// UI startup
var UI = new rcube_mail_ui();
$(document).ready(function(){
	UI.set('errortitle', 'Une erreur est survenue!');
	UI.init();
});

</script>
<!--[if lte IE 8]>
<script type="text/javascript">

// fix missing :last-child selectors
$(document).ready(function(){
	$('ul.treelist ul').each(function(i,ul){
		$('li:last-child', ul).css('border-bottom', 0);
	});
});

</script>
<![endif]-->





<script type="text/javascript">

jQuery.extend(jQuery.ui.dialog.prototype.options.position, {
                using: function(pos) {
                    var me = jQuery(this),
                        offset = me.css(pos).offset(),
                        topOffset = offset.top - 12;
                    if (topOffset < 0)
                        me.css('top', pos.top - topOffset);
                    if (offset.left + me.outerWidth() + 12 > jQuery(window).width())
                        me.css('left', pos.left - 12);
                }
            });
$(document).ready(function(){ 
rcmail.init();
var images = ["skins\/larry\/images\/ajaxloader.gif","skins\/larry\/images\/ajaxloader_dark.gif","skins\/larry\/images\/buttons.png","skins\/larry\/images\/addcontact.png","skins\/larry\/images\/filetypes.png","skins\/larry\/images\/listicons.png","skins\/larry\/images\/messages.png","skins\/larry\/images\/messages_dark.png","skins\/larry\/images\/quota.png","skins\/larry\/images\/selector.png","skins\/larry\/images\/splitter.png","skins\/larry\/images\/watermark.jpg"];
            for (var i=0; i<images.length; i++) {
                img = new Image();
                img.src = images[i];
            }
});
</script>


</body></html>
