# -*- coding: utf-8 -*-
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from entity import Mail


def _build_email(mail):
    print(f'Preparando para enviar o email a {mail.recipient}')
    path = './files/'
    msg = MIMEMultipart()
    msg['From'] = mail.sender
    msg['To'] = mail.recipient
    msg['Subject'] = mail.subject
    body = mail.message
    msg.attach(MIMEText(body, 'plain')) 
    for filename in mail.attachments:
        p = MIMEBase('application', 'octet-stream') 
        attachment = open(path+filename,'rb')
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
    
    return msg

  
def send_email(mail, password):
    msg = _build_email(mail)
    #print(msg.as_string())
    s = smtplib.SMTP('smtp.gmail.com', 587)    
    # start TLS for security 
    s.starttls()   
    # Authentication 
    s.login("wilton.silva@ifgoiano.edu.br", password)   
    # Converts the Multipart msg into a string 
    text = msg.as_string()
    # sending the mail 
    s.sendmail("wilton.silva@ifgoiano.edu.br", msg['To'], text) 
    # terminating the session 
    print(f'Email Enviado para {mail.recipient}')
    s.quit() 