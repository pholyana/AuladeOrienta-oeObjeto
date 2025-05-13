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
        else:
            print(f"conta ja está ativada")






class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor


    def comer(self):
        print(f"{self.nome} foi comer")


class Gato(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"o {self.nome} está miando ")


class Vaca(Animal):
    def __init__(self, nome ,cor):
        super().__init__(nome,cor)

    def rugir(self):
        print(f"{self.nome} faz muuuuuhhh")


class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"{self.nome} está latindo")


class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def grunindo(self):
        print(f"{self.nome} está grunindo")


class Ingresso():
    def __init__(self,valor):
        self.valor=valor
        print(f"{self.valor} este é o valor do ingresso")

    def imprimeValor(self):
        print(f" o ingresso custa: {self.valor}")


class VIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor2=valor*1.5

    def imprimeValor(self):
        print(f" O seu ingresso vip custa :{self.valor2}")


class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()


    def calculaArea(self,base,altura):
        self.area = base*altura
        print(f"a area do retangulo é {self.area} :")

    def calcularperimetro(self, base,altura):
        self.perimetro=2*(base+altura)
        print(f"o perimetro do retangulo é {self.perimetro}")

class Triangulo(Forma):
    def __init__(self,altura):
        super().__init__()



class Atleta():
    def __init__(self):
        self.aposentado=False
        self.peso=0
       

    def aquecer(self):
        print("ele está aquecendo")
        if self.aposentado==True:
            print("ele está aposentado e não pode aquecer")
            return


    def aposentar(self):
            print("ele esta aquecendo")


class Corredor(Atleta):
    def __init__(self):
        super().__init__()

    def correr(self):
        print(f"ele está corrrendo")



class Nadador(Atleta):
    def __init__(self):
        super().__init__()
        print(f"ele está nadando")



class Ciclista(Atleta):
    def __init__(self):
        super().__init__()