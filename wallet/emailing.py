import smtplib
import os

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

emailid = 'manishsaini698@gmail.com'
#emailid = os.environ['email']

def send_email(recipient, message):
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = emailid
    msg['Subject'] = 'Otp from Expay'
    part = MIMEText('text', 'plain')
    part.set_payload(message)
    msg.attach(part)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    #password = os.environ['ekey']
    password = 'manish16199811'

    session.login(emailid, password)
    session.sendmail(emailid, recipient, msg.as_string())
    session.quit()
