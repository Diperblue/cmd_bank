def create_user_database(name:str, email:str, password:str, cpf:str):
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    dados = {
        'nome': name,
        'email': email,
        'password': password_md5,
        'cpf': cpf
    }
    cpf_md5 = hashlib.md5(cpf.encode('utf-8')).hexdigest()
    with open(f'database/{cpf_md5}.json', 'a') as json_file:
        json.dump(dados, json_file, indent=4)