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
	cp make-tls-key.sh /usr/lib/cgi-bin/	
	cp certbot.sh /usr/lib/cgi-bin/	
	cp gpgscript /usr/lib/cgi-bin/
	cp sudoers-final /usr/lib/cgi-bin/	
	chmod +x /usr/lib/cgi-bin/setupTor.sh
	chmod +x /usr/lib/cgi-bin/setupGnupg.sh
	chmod 755 /usr/lib/cgi-bin/gpgscript
	chown www-data /var/www/first/index.html
	chown www-data /var/www/first/index-final.html	
	chmod 755 /var/www/first/index.html
	chmod 755 /var/www/first/index-final.html	
	chown www-data  /usr/lib/cgi-bin/*
	chown www-data  /var/www/first/*
	chown www-data  /var/www/first
/var/www/first/:
	mkdir /var/www/first/
