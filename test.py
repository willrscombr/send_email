# -*- coding: utf-8 -*-#
from service import send_email
from entity import Mail
from interface import read_files_receivers, get_user_auth 
from factory import mail_factory

def test():
    #email_sender, password = get_user_auth()
    email_sender = 'wilton.silva@ifgoiano.edu.br'
    title = "Sistema de Envio de E-mail Automático - IFGOIANO - Campus Iporá"
    msg = "Olá essse é um e-mail teste. "
    list_emails = list()
    list_receivers = read_files_receivers('dados.csv') or []
    #rint(list_receivers[0][1])
    for receiver in list_receivers:
        
        if len(receiver) == 2:
            list_emails.append(
                mail_factory(
                    receiver[0],receiver[1]+'.pdf',
                    title,
                    msg,
                    email_sender
                    )
                )
    password = input('Digite sua sua senha de email:   ')
    for email in list_emails:
        send_email(email, password)
        #print(email.attachments)
        


if __name__== "__main__":
    test()


