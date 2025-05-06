class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dormir=False
        self.falando=False
        self.comendo=False

    def falar(self):
        print(f"{self.nome} começou a falar")
        if self.dormir:
            print(f"não pode falar por que esta dormindo")
        else:
            print(f" {self.nome} esta falando")


    def comer(self, comida):
        print(f"{self.nome} começou a comer {comida}")
    def dormir(self ):
        print(f"{self.nome} começou a dormir")
