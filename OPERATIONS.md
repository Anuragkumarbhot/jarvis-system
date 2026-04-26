Operations Guide

Start System

~/assistant/start.sh

Stop System

pkill -9 python

Restart System

pkill -9 python
~/assistant/start.sh

Check Logs

cat logs/dashboard.log

Backup System

tar -czf backup.tar.gz assistant/

Update System

pkg update
pkg upgrade

Security

Change default password
Enable HTTPS
Monitor logs regularly
