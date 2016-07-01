import smtplib 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#sender and recipient
me= "collabxchat@microsoft.com"
you= "njn27@cornell.edu"

#message container
msg= MIMEMultipart('alternative')
msg['Subject']= "Python email test"
msg['From']= me
msg['To']= you


#message body (plaintext version and html version)
text= "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html= """\
<html>
	<head></head>
	<body>
		<p>Hi!<br>
			<em>How are you?</em><br>
			Here is the <a href="https://www.python.org">link</a> you wanted.
		</p>
	</body>
</html>
"""

print "Completed writing email!"

#Record MIME types of both parts
part1= MIMEText(text,'plain')
part2= MIMEText(html,'html')

#Attach parts into message container
msg.attach(part1)
msg.attach(part2)

print "Attached to container!"

#send message via local SMTP server
mail = smtplib.SMTP('smtp.office365.com', 587)

#mail.ehlo()

mail.starttls()

#mail.login('nikhilna@microsoft.com', 'xxxxxxx')
mail.sendmail(me, you, msg.as_string())
mail.quit()

print "Done!"

