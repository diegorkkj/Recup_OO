from classe import *

banco = Banco()

cliente = Cliente()

def main():
    while True:
        try:
            print("Bem Vindo")
            print("[1] - Cadastrar cliente")
            print("[2] - Saque")
            print("[3] - Depositar")
            print("[4] - Transferir")
            print("[5] - Saldo")
            print("[6] - Sair")

            menu = int(input("Digite o número equivalente à opção que deseja\n>> "))
            match menu:
                case 1:
                    limpar()
                    banco.adicionar_conta()
                    banco.setNome(input("Digite o nome do cliente.\n>> "))
                    banco.setCpf(input("Digite o CPF do cliente.\n>> "))
                    banco.setSaldo(input("Digite o saldo do cliente.\n>> "))
                    pausar()
                case 2:
                    limpar()
                    print("Saque")
                    cliente.sacar()
                    pausar()
                case 3:
                    limpar()
                    print("Deposito")
                    pausar()
                case 4:
                    limpar()
                    print("Transferir")
                    pausar()
                case 5:
                    limpar()
                    print("Saldo")
                    banco.getSaldo()
                    pausar()
                case 6:
                    limpar()
                    print("Saindo...")
                    pausar()
                    break
                case _:
                    print("Essa opção não consta na lista.")
        except Exception:
            limpar()
            print("Algo deu errado.")
            pausar()