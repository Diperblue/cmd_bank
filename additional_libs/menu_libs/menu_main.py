from termcolor import colored

def register_user() -> 'str=object':
    from ..user_libs.user_object import user
    name = str(input('Digite seu nome: '))
    email = str(input('Digite seu email: '))
    password = str(input('Digite sua senha: '))
    cpf = str(input('Digite seu cpf: '))
    register = user(name, email, password, cpf)
    register.register()
def login() -> 'login_menu':
    from ..user_libs.user_main import user
   # if str(input('Você quer se logar utilizando cpf ou email?(cpf/email):'))=='cpf':



def menu() -> str:
    logo_text = colored("""
    ▄████▄   ███▄ ▄███▓▓█████▄     ▄▄▄▄    ▄▄▄       ███▄    █  ██ ▄█▀
    ▒██▀ ▀█  ▓██▒▀█▀ ██▒▒██▀ ██▌   ▓█████▄ ▒████▄     ██ ▀█   █  ██▄█▒ 
    ▒▓█    ▄ ▓██    ▓██░░██   █▌   ▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░ 
    ▒▓▓▄ ▄██▒▒██    ▒██ ░▓█▄   ▌   ▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄ 
    ▒ ▓███▀ ░▒██▒   ░██▒░▒████▓    ░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄
    ░ ░▒ ▒  ░░ ▒░   ░  ░ ▒▒▓  ▒    ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
    ░  ▒   ░  ░      ░ ░ ▒  ▒    ▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░
    ░        ░      ░    ░ ░  ░     ░    ░   ░   ▒      ░   ░ ░ ░ ░░ ░ 
    ░ ░             ░      ░        ░            ░  ░         ░ ░  ░   
    ░                    ░               ░                          
    """, 'red')
    welcome_text = colored("Bem-vindo ao CMD BANK.", 'green')
    options_text = colored("""
                1 - Entrar
                2 - Registrar
                3 - Sair
    """, 'green')

    print(logo_text, end="\n\n")
    print(welcome_text)
    print(options_text)

def options_select() -> 'selected-menu':
    options_s_text = colored("Escolha umas das opções acima: ")
    op = int(input(options_s_text))
    try: # Escolhendo opções
        if op==1: # Entrar
            print("Em produção...")
        elif op==2: # Registrar
            register_user()
        elif op==3: # Sair
            print("Volte novamente.\nSaindo...")
            exit(0)
    except Exception as ERRO: # Error
        print(f"Aconteceu o erro:\n{ERRO}")