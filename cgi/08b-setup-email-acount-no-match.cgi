#!/bin/bash

echo -e "Content-type: text/html\n\n"

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
    <script type="text/javascript">
        function switch_screen() {
            document.getElementById("form").style.display = "none";
            document.getElementById("waiting").style.display = "block";
        }
    </script>
    <script>
    function validateForm() {
      var x = document.forms["myForm"]["pass1"].value;
      if (x.indexOf("$") != -1 || x.indexOf("'
      echo -n "'"
      printf '") != -1 || x.indexOf("\\\"") != -1 ) {
	  alert(\"The following characters are forbidden in passwords: '
	  echo -n "'"
	  printf '\\\" $ \");
	  return false;
      }
      else
      {
      switch_screen();
      }
      return true;
    }
</script>        
</head>
<body>
<img src="../first/files/images/logo.png" alt="Own-Mailbox Logo">
<div class="box">
    <div id="waiting" style="display: none;">
        <p class="title">
            Configuring your webmail
        </p>
        <div class="content">
            <p>Please wait...</p>
            <p class="warn small">This may take up to 3 minutes.</p>
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
    </div>

    <div id="form">
        <p class="title">
            Create email account
        </p>
        <div class="content">
            <form  name="myForm" onsubmit="return validateForm()" action="../cgi-bin/09-setup-mailpile.cgi" method="post">
                <p class="error">Passwords did not match, please try again.</p>
                <table>
                    <tr>
                        <td style="width: 25%%;">Email:</td>
                        <td><input type="text" name="user"></td>
                        <td>@'
cat /home/www-data/domain;
printf '
                        </td>
                    </tr>
                    <tr>
                        <td>Full name:</td>
                        <td colspan="2"><input type="text" name="fn"></td>
                    </tr>
                    <tr>
                        <td>Password:</td>
                        <td colspan="2"><input type="password" name="pass1"></td>
                    </tr>
                    <tr>
                        <td>Confirm:</td>
                        <td colspan="2"><input type="password" name="pass2"></td>
                    </tr>
                </table>

                <p class="buttons">
                    <input type="submit" class="button mainaction" value="Submit">
                </p>
            </form>
        </div>
    </div>
</div>
</body>
</html>'
