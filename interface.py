# -*- coding: utf-8 -*-#
import csv

def get_user_auth():
    user_email = input('Digite o e-mail que enviará os certificados:   ')
    password = input('Digite sua sua senha de email:   ')
    return user_email, password

def read_files_receivers(file_name):
    list_user = []

    with open('./input/'+file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',quotechar="|",skipinitialspace=True)
        for row in reader:
            list_user.append(row)
    
    
    return list_user


