import hashlib
import os
from storage import carregar_dados, salvar_dados

# Função para gerar o hash da senha com salt
def gerar_hash_senha(senha):
    """Gera o hash SHA-256 da senha com salt para maior segurança."""
    salt = os.urandom(16)  # Gerar um salt aleatório de 16 bytes
    senha_saltada = salt + senha.encode()  # Combina o salt com a senha
    senha_hash = hashlib.sha256(senha_saltada).hexdigest()  # Gera o hash
    return salt.hex(), senha_hash  # Retorna o salt e o hash (salt é armazenado para verificações futuras)

# Função para verificar a senha
def verificar_senha(senha_informada, salt_armazenado, senha_armazenada):
    """Verifica se a senha informada corresponde ao hash armazenado."""
    senha_informada_saltada = salt_armazenado + senha_informada.encode()
    senha_informada_hash = hashlib.sha256(senha_informada_saltada).hexdigest()
    
    return senha_informada_hash == senha_armazenada

# Função para adicionar um novo usuário
def adicionar_usuario():
    """Permite criar um novo usuário a qualquer momento."""
    dados = carregar_dados()
    
    while True:
        nome = input("Digite seu nome de usuário: ")
        
        # Garante que não vamos criar um usuário que já existe
        if nome in dados["usuarios"]:
            print("Este nome de usuário já está cadastrado! Tente fazer login.")
            return None  # Evita erro
        
        senha = input("Digite uma senha: ")
        
        # Gerar o hash da senha com salt
        salt, senha_hash = gerar_hash_senha(senha)
        
        dados["usuarios"][nome] = {
            "salt": salt,
            "senha": senha_hash,
            "saldo": 0  # Novo usuário começa com saldo 0
        }
        
        salvar_dados(dados)
        print(f"Usuário {nome} criado com sucesso!")
        return nome  # Retorna o nome do usuário criado

# Função de login
def login():
    """Solicita nome e senha e verifica se estão corretos."""
    dados = carregar_dados()
    
    while True:
        nome_usuario = input("Digite seu nome de usuário: ")
        
        if nome_usuario in dados["usuarios"]:
            senha_usuario = input("Digite sua senha: ")
            salt_armazenado = bytes.fromhex(dados["usuarios"][nome_usuario]["salt"])  # Recuperar o salt do usuário
            senha_armazenada = dados["usuarios"][nome_usuario]["senha"]
            
            if verificar_senha(senha_usuario, salt_armazenado, senha_armazenada):
                print("Login bem-sucedido!")
                return nome_usuario  # Retorna o nome do usuário logado
            else:
                print("Senha incorreta! Tente novamente.")
        else:
            print("Usuário não encontrado.")
            opcao = input("Deseja criar um novo usuário? (s/n): ").strip().lower()
            
            if opcao == "s":
                novo_usuario = adicionar_usuario()  # Tentamos criar um novo usuário
                
                if novo_usuario:  # Só retorna se o usuário foi criado com sucesso
                    return novo_usuario  
            else:
                print("Tente novamente ou saia do programa.")