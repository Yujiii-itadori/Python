from email.message import EmailMessage
from password import passwords, emailid
import ssl
import smtplib

email_sender = 'leonbarretto52@gmail.com'
email_password = passwords

email_reciever = 'barretto_l@yahoo.in'

subject = "Python generated email"
body = """Hi, this message is sent by Python"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body) 


content = ssl.create_default_context() #creates in default settings 

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=content) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())