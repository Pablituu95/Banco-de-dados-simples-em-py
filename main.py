import sqlite3,secrets

def verificar_resposta(r=float):
    comando = ""
    match r:
        case 2:
            comando = "SELECT nome,email,idade from usuarios ORDER BY nome ASC"
        case 2.1:
            comando = "SELECT nome,email,idade from usuarios WHERE idade <18 "
        case 2.2:
            comando = "SELECT nome,email,idade from usuarios WHERE idade >=18"
    cursor.execute(comando)
    dados = cursor.fetchall()
    for usuario in dados:
        nome = usuario[0]
        email = usuario[1]
        idade = usuario[2]
        print('-'*30)
        print(f"Nome do usuário: {nome}\nEmail: {email}\nIdade: {idade}\n{'-'*30}")
    db.commit()
        
def adicionar_usuarios():
    while True:
            try:
                nome = input("Digite o nome do usuário: ")
                if nome == "":
                    break
                idade = int(input("Digite a idade do usuário: "))
                senha = secrets.token_hex(16)
                email = input("Digite o seu email: ")
                cursor.execute("INSERT INTO usuarios(nome,senha,idade,email) VALUES(?,?,?,?)",(nome,senha,idade,email))
                db.commit()
                print("Usuário adicionado com sucesso!")
            except sqlite3.IntegrityError:
                print("\033[31m","O email ou nome que você digitou já está sendo usado, digite os dados novamente!", "\033[0m")
                continue

db = sqlite3.connect("meu_banco.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL,
               idade INTEGER NOT NULL,
               email TEXT NOT NULL UNIQUE
               )""")

while True:
    try:
        resposta = float(input(f"{"="*30} Formulário de gestão {"="*30}\n1 - Adicionar usuários\n2 - Mostrar todos (A-Z)\n2.1 - Mostrar menores de idade\n2.2 - Mostrar maiores de idade\n3- SAIR\nDigite a sua resposta: "))
        if resposta == 1.0:
            adicionar_usuarios()
        elif resposta == 3:
            break
        else:
            verificar_resposta(resposta)
    except ValueError:
        print("O valor que você inseriu é inválido!")




