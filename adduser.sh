password=$2
pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
echo $pass;
useradd -m -p $pass $1

sudo -u $1 maildirmake /home/$1/Maildir
sudo -u $1 maildirmake -f Sent /home/$1/Maildir
sudo -u $1 maildirmake -f Queue /home/$1/Maildir
sudo -u $1 maildirmake -f junkmail /home/$1/Maildir
sudo -u $1 maildirmake -f virus /home/$1/Maildir
sudo -u $1 maildirmake -f Drafts /home/$1/Maildir
sudo -u $1 maildirmake -f Trash /home/$1/Maildir

chown -R $1 /home/$1/

cp .procmailrc /home/$1/
chown $1 /home/$1/.procmailrc