all: 	/var/www/first/
	cp sudoers /etc/sudoers
	cp -r *.html /var/www/first/
	cp -r files /var/www/first/	
	cp *.cgi /usr/lib/cgi-bin/
	cp index-root-init.html /var/www/index.html
	chown www-data /var/www/index.html
	chmod 755 /usr/lib/cgi-bin/*.cgi
	cp setupTor.sh /usr/lib/cgi-bin/
	cp setupGnupg.sh /usr/lib/cgi-bin/
	cp gpgscript /usr/lib/cgi-bin/
	cp sudoers-final /usr/lib/cgi-bin/	
	chmod +x /usr/lib/cgi-bin/setupTor.sh
	chmod +x /usr/lib/cgi-bin/setupGnupg.sh
	chmod 755 /usr/lib/cgi-bin/gpgscript
	chown www-data /var/www/first/index.html
	chown www-data /var/www/first/index-final.html	
	chmod 755 /var/www/first/index.html
	chmod 755 /var/www/first/index-final.html	
	chown www-data  /usr/lib/cgi-bin/02-recupPassnSetupTor.cgi
	chown www-data  /usr/lib/cgi-bin/04-recupIdentificationLink.cgi
	chown www-data  /usr/lib/cgi-bin/05b-choose-domain-error.cgi
	chown www-data  /usr/lib/cgi-bin/06-recupdomain.cgi
	chown www-data  /usr/lib/cgi-bin/07-sumup.cgi
	chown www-data  /usr/lib/cgi-bin/08b-setup-email-acount-nomatch.cgi
	chown www-data  /usr/lib/cgi-bin/08-setup-email-acount.cgi
	chown www-data  /usr/lib/cgi-bin/09-setupMailpile.cgi
	chown www-data  /usr/lib/cgi-bin/10-final.cgi
	
/var/www/first/:
	mkdir /var/www/first/
