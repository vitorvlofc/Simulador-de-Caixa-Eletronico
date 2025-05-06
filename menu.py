from operações import ver_saldo, sacar, depositar
from storage import carregar_dados, salvar_dados

def menu_interativo(usuario):
    while True:
        print("\n=== Menu do Caixa Eletrônico ===")
        print("1 - Ver saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ver_saldo(usuario)
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para sacar: "))
                sacar(usuario, valor)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "3":
            try:
                valor = float(input("Digite o valor para depositar: "))
                depositar(usuario, valor)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "4":
            print("Saindo... Obrigado por usar o caixa!")
            break
        else:
            print("Opção inválida! Tente novamente.")
