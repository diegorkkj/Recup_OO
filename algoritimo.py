import os
from classe import *

def main():
    while True:
        try:
            limpar()
            print("Bem vindo a Loja do Cacique")
            print("[1] - Cadastrar Usuario")
            print("[2] - Sacar")
            print("[3] - Depositar")
            print("[4] - Realizar Transferência")
            print("[5] - Ver o Saldo")
            print("[6] - Sair")
            print("Digite o numero equivalente a opção que deseja")
            menu = int(input(">> "))

            match menu:
                case 1:
                    limpar()
                    pausar() 

                case 2:
                    limpar()
                    pausar()

                case 3:
                    limpar()
                    pausar()
                    
                case 4:
                    limpar()
                    pausar()


                case 5:
                    limpar()
                    pausar()

                case 6:
                    limpar()
                    print("Saindo...")
                    pausar
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
    
