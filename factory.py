from entity import Mail



def mail_factory(email,attachments_name,title,msg,sender_email):
    mail = Mail(sender_email,
    email,
    title,
    msg,
    [attachments_name]
    )

    return mail

