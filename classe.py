import os

def limpar():
    os.system("cls")

def pausar():
    os.system("pause")
    
class Cliente:

    def sacar(self, valor,saldo):
        if valor > saldo:
            print("Não é possivel sacar esse valor")
        else:
            self.saldo -= valor
            print("Valor sacado. O seu saldo agora é de R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print("Valor depositado. O seu saldo agora é de R$", self.saldo)

    def transferencia():
        pass

class Banco:

    def adicionar_conta(self):
        self.nome = ""
        self.cpf = 0
        self.saldo = 0
        conta = {'nome': self.nome, 'cpf': self.cpf, 'saldo' : self.saldo}
        clientes.append(conta)
    
    def getConta(self):
        return self.num_conta
   
    def getNome(self):
        return self.nome
    
    def setNome(self,x):
        self.nome = x

    def getCpf(self):
        return self.cpf
    
    def setCpf(self,x):
        self.cpf = x
        
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self,x):
        self.saldo = x

clientes = []