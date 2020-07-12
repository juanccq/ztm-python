import smtplib
from email.mime.text import MIMEText
from string import Template
from pathlib import Path

html = Template( Path( 'smtp-message.html' ).read_text() )
msg = MIMEText( html.substitute( {'name':'Juan Carlos'} ), 'html' )

msg[ 'from' ] = 'ZTM test email message'
msg[ 'to' ] = 'juan.c.c.q@gmail.com'
msg[ 'subject' ] = 'Great news for you'

with smtplib.SMTP( host='smtp.gmail.com', port=587 ) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('jresearch2dd@gmail.com', 'downaccount.1')
	smtp.send_message( msg )
	print( 'Email was sent' )