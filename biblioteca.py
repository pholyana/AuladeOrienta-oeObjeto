class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dormindo=False
        self.falando=False
        self.comendo=False

    def falar(self):
        if self.falando==True:
            print(f" {self.nome} esta falando")
        elif self.dormir==True:
            print(f"não pode falar por que esta dormindo")
        else:
            print(f"{self.nome} começou a falar")
            self.falando=True

    def comer(self):
        if self.comendo==True:
            print(f"não pode comer pq já está comendo")
        elif self.dormindo==True:
            print(f"{self.nome} não pode  está dormindo pq está comendo")
        elif self.falando==True:
            print("nao pode dormir pq já  esta falando")
        else:
            print(f"{self.nome} começou a comer")
            self.comendo=True

    def dormir(self ):
        if self.dormindo==True:
            print(f"{self.nome} já está dormindo")
        elif self.comendo ==True:
            print(f"{self.nome} não pode comer pq está dormindo")
        elif self.dormindo==True:
            print("não pode dormir pq já esta dormindo")
        else:
            print(f"{self.nome} começou a dormir")
            self.dormindo=True

class conta_bancaria():
    def __init__(self, conta ,nomecliente,tipodaconta):
        self.conta=conta
        self.saldo=0
        self.statusdaConta = False
        self.nomedoCliente=nomecliente
        self.tipodaConta=tipodaconta

    def ativsarconta(self):
        if self.statusdaconta==False:
            self.statusdaConta=True
            print(f"{self.nomeCliente} conta ativada")
        else:
            print(f"conta ja está ativada")
