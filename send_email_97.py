"""
____________  _______
|            |       |
|            |       |
|__________  |_______|
|            |\
|            | \
|___________ |  \
"""


import smtplib #simple mail transfer protocol library

sender = "sender@gmail.com"
receiver = "reciever@gmail.com"
password = "password" #use the 16 character code either from -> https://myaccount.google.com/u/4/apppasswords
subject = "test"
body = "How are you my friend."

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Logged in... ")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Cant sign in")




"""server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()


server_ssl.login(sender,password)
print("Logged in... ")
server_ssl.sendmail(sender, receiver, message)
server_ssl.close()
print("Email has been sent!")"""






"""from email.mime.multipart import MIMEMultipart #=> mime = multipurpose internet mail extension, defines the format of email, MIMEMultipart => supports both HTML context and plain text
from email.mime.text import MIMEText
import smtplib #simple mail transfer protocol library


message = MIMEMultipart()
message["from"] = "Rawgosh"
message["to"] = "inej.rawgosh@gmail.com"
message["subject"] = "test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo() #requesting the smtp server
    smtp.starttls() #tls => transfer layer security
    smtp.login("rawgoshshrestha129@gmail.com","password") #we can directly pass the user-email and password
    smtp.send_message(message)
    print("Sent")


import smtplib

# create an SMTP object
server = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS encryption
server.starttls()

# login to the server
server.login("inej.rawgosh@gmail.com", "password")

# send the email
msg = "Hello, this is a test email from Python."
server.sendmail("inej.rawgosh@gmail.com", "rawgoshshrestha129@gmail.com", msg)

# quit the server
server.quit()
"""