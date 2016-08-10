all:
	cp sudoers-temporary /etc/sudoers
	mkdir -p /var/www/first/
	cp -r files /var/www/first/
	cp *.html /var/www/first/
	cp index-root-init.html /var/www/index.html
	chown www-data /var/www/index.html
	chown -R www-data /var/www/first
	cp *.cgi /usr/lib/cgi-bin/
	cp sudoers-final /usr/lib/cgi-bin/
	cp gpgscript /usr/lib/cgi-bin/
	cp setup-gnupg.sh /usr/lib/cgi-bin/
	cp setup-tor.sh /usr/lib/cgi-bin/
	cp make-tls-key.sh /usr/lib/cgi-bin/
	cp changeRootPasswordOnce.sh /usr/lib/cgi-bin/
	cp configPostfixMailpileGPG.sh /usr/lib/cgi-bin/	
	cp getTorHostname.sh /usr/lib/cgi-bin/	
	cp revokeSudoers.sh /usr/lib/cgi-bin/		
	cp certbot.sh /usr/lib/cgi-bin/
	chown www-data /usr/lib/cgi-bin/*.cgi
	chmod +x /usr/lib/cgi-bin/*
