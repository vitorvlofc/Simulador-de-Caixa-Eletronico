from storage import carregar_dados, salvar_dados

def ver_saldo(usuario):
    dados = carregar_dados()
    saldo = dados["usuarios"][usuario]["saldo"]
    print(f"Saldo atual de {usuario}: R${saldo:.2f}")

def depositar(usuario, valor):
    dados = carregar_dados()
    if valor > 0:
        dados["usuarios"][usuario]["saldo"] += valor
        salvar_dados(dados)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        ver_saldo(usuario)
    else:
        print("Valor de depósito inválido!")

def sacar(usuario, valor):
    dados = carregar_dados()
    saldo = dados["usuarios"][usuario]["saldo"]
    
    # Definir as cédulas disponíveis no caixa eletrônico
    cedulas_disponiveis = {
        100: 10,  # 10 cédulas de R$ 100
        50: 20,   # 20 cédulas de R$ 50
        20: 30,   # 30 cédulas de R$ 20
        10: 50,   # 50 cédulas de R$ 10
        5: 100,   # 100 cédulas de R$ 5
        2: 200,   # 200 cédulas de R$ 2
    }
    
    if valor > saldo:
        print("Saldo insuficiente!")
        return
    
    valor_sacado = 0  # Quanto o usuário já sacou
    cédulas_sacadas = {}  # Armazenar as cédulas que foram usadas no saque
    
    for cédula, quantidade in sorted(cedulas_disponiveis.items(), reverse=True):  # Tentando sacar com as maiores cédulas primeiro
        if valor_sacado >= valor:
            break
        if quantidade > 0:  # Se houver cédulas desse valor
            maximo_sacar = (valor - valor_sacado) // cédula  # Quantas cédulas desse valor o usuário pode retirar
            if maximo_sacar > quantidade:  # Caso o caixa tenha menos cédulas do que o necessário
                maximo_sacar = quantidade
            
            if maximo_sacar > 0:
                valor_sacado += maximo_sacar * cédula
                cedulas_disponiveis[cédula] -= maximo_sacar
                cédulas_sacadas[cédula] = maximo_sacar
    
    if valor_sacado < valor:
        print(f"Só foi possível sacar R${valor_sacado}. O restante não tem cédulas disponíveis.")
    else:
        print(f"Saque de R${valor_sacado} realizado com sucesso!")
    
    # Atualiza o saldo do usuário após o saque
    dados["usuarios"][usuario]["saldo"] -= valor_sacado
    salvar_dados(dados)

