import json
import os

# Definindo as cédulas disponíveis no caixa eletrônico
cedulas_disponiveis = {
    100: 10,  # 10 cédulas de R$ 100
    50: 20,   # 20 cédulas de R$ 50
    20: 30,   # 30 cédulas de R$ 20
    10: 50,   # 50 cédulas de R$ 10
    5: 100,   # 100 cédulas de R$ 5
    2: 200,   # 200 cédulas de R$ 2
}


def carregar_dados():
    """Carrega os dados do arquivo JSON. Se não existir, cria um novo vazio."""
    if not os.path.exists("dados.json"):
        dados_iniciais = {"usuarios": {}, "notas_disponiveis": {}}
        with open("dados.json", "w") as arquivo:
            json.dump(dados_iniciais, arquivo, indent=4)
        return dados_iniciais
    else:
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)

def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
