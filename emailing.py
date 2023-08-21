import smtplib,ssl
import os
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def send_email(images):
    password = os.getenv("PASSWORD")
    username = os.getenv("EMAIL")
    with open (f'images/{images}.png','rb') as f:
        img_data=f.read()
    msg=MIMEMultipart()
    msg['From']=username
    msg['To']=username
    msg['Subject']='Email From web detection app'
    msg.attach(MIMEText("This object is detected in the area"))
    image=MIMEImage(img_data, name=os.path.basename('imag.png'))
    msg.attach(image)
    host='smtp.gmail.com'

    port=465


    with smtplib.SMTP_SSL(host,port) as server:
        server.login(username,password)
        server.sendmail(username,username,msg.as_string())