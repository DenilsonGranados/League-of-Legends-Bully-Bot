import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, content):
    user= ''### Add your email here Example> 'bobsmith1234@gmail.com'
    pswrd= '' ### Add your email's pswrd here
    msg=MIMEMultipart()
    msg['From']=user
    msg['To']= to
    msg['Subject']=subject
    
    msg.attach(MIMEText(content, 'plain'))
    
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user, pswrd) ### Note if this line gives issue try allow less secure apps from google at this link https://www.google.com/settings/security/lesssecureapps
    text= msg.as_string()
    server.sendmail(user,to, text)
    return
# send_email('denilsongranados4@gmail.com', 'You suck at League', "Hello World") ### Testing line