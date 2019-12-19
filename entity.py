# -*- coding: utf-8 -*-
class Mail:
    def __init__(self, sender,recipient,subject, message, attachments =[]):
        self.sender = str(sender)
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.attachments = attachments

    def add_attachment_path(filename:'Path'):
        
        self.attachments.add(attachment)

  