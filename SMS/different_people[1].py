import smtplib
from email.message import EmailMessage

# change this one with your address
username = "ebisinteidennis@gmail.com"
# and this with the password as I showed you in the video
password = "vvbtrorgrgczcshh"
 
message = [
    """From: From Person <ebisinteidennis@gmail.com>
To: To Person <howto5349@gmail.com>
Subject: Lets play tech
 
First email
    """,
 
    """From: From Person <ebisinteidennis@gmail.com>
To: To Person <fu109306@gmail.com>
Subject: Email 2 from gg
 
Second email again
    """]
 
mail = username
receivers = [mail, "fu109306@gmail.com"]
 
 
def same_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(
        mail,
        receivers,
        message)
 
    server.quit()
 
 
def different_email():
    for n, msg in enumerate(message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(
            mail,
            receivers[n],
            message[n])
 
        server.quit()
 
 
different_email()
