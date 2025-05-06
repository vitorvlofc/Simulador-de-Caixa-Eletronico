from auth import login
from menu import menu_interativo

# O programa começa pedindo o login do usuário
usuario = login()

# Depois chama o menu interativo passando o nome do usuário
menu_interativo(usuario)
