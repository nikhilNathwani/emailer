# emailer
Sending automated emails via python

NOTE: need to run the following to start up a simple SMTP server: 
python -m smtpd -n -c DebuggingServer localhost:1025

And then modify the mail-sending code to use the non-standard port number:
s= smtplib.SMTP('localhost',1025)
