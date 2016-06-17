# Own-Mailbox_first-time-setup-ihm
Web interface in order to easilly setup an Own-mailbox.

Dependencies
-----
* Tor
* Tor-socks
* sudo
* postfix
* gnupg
* Apache with cgi-bin
* Mailpile (Own-Mailbox version) installed in /home/mailpile/Mailpile directory.
* Own-Mailbox_Client-Server_Commnucation (client side).

install
-----
Make will install files in /var/www/first/ and /usr/lib/cgi-bin/ for cgi scripts, AND modify your SUDOERS FILE so that www-data is permitted to do required operations.