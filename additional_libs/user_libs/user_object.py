import json
import hashlib
import os

class user:
    def __init__(self, email:str, password:str, name=None, cpf=None) -> object:
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.name = None
        self.cpf = None
    def register(self, name, cpf) -> 'object_database_create':
        from user_create import create_user_database
        self.name = name
        self.cpf = cpf
        create_user_database(name, email, password, cpf)
    def login(self, login:'cpf/email:str', password:str) -> 'object_menu':
        scan_users = os.run('ls database/').split('\n')
        for k in scan_users:
            if login in k:
                data_dict = json.load('database/'+k)
                self = user(data_dict['name'], data_dict['email'], data_dict['password'], data_dict['cpf'])
            else:
                return print('Sua conta não foi encotrada')

    