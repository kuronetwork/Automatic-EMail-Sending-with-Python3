import smtplib, ssl

port = 587 
smtp_server = "smtp.gmail.com"
sender_email = "youtmail"
receiver_email = "yourmail"
password = ''
message = """\
Subject: Test

Auto mail"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)