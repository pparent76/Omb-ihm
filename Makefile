all:
	cp sudoers /etc/sudoers
	rm -r /var/www/first/
	mkdir /var/www/first/
	cp -r *.html /var/www/first/
	cp -r files /var/www/first/	
	cp *.cgi /usr/lib/cgi-bin/
	chmod 755 /usr/lib/cgi-bin/*.cgi
	cp setupTor.sh /usr/lib/cgi-bin/
	chmod +x /usr/lib/cgi-bin/setupTor.sh
