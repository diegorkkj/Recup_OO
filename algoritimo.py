import os
from classe import *

def main():
    while True:
        try:
            limpar()
            print("Bem vindo a Loja do Cacique")
            print("[1] - ")
            print("[2] - ")
            print("[3] - ")
            print("[4] - ")
            print("[5] - Sair")
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
                    print("Saindo...")
                    pausar()
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
    
