class Aniversario:
    def to_try(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
dia=Aniversario()
dia.dia=30
dia.mes=8
dia.ano=2004
print(dia.to_try())

class meunome:
    def montagem(self):
        return f"{self.primeiro} {self.segundo} {self.terceiro} {self.quarto}"
nome=meunome()
nome.primeiro=str(input("Quall seu primeiro nome?"))
nome.segundo=str(input("Qual seu segundo nome?"))
nome.terceiro=str(input("Qual seu terceiro nome?"))
nome.quarto=str(input("Qual seu quarto nome?"))
print(nome.montagem())

class pedido:
    def anotacao(self):
        return f"{self.bebida},{self.lanche},{self.maisalgo}"
bloco=pedido()
bloco.bebida=str(input("Digite sua bebida?  "))
bloco.lanche=str(input("Digite um lanche?   "))
bloco.maisalgo=str(input("Quer algo mais?   "))
print(bloco.anotacao())

class carro:
    def monteseucarro(self):
        return f"{self.cor},{self.cavalos}"
motando=carro()
motando.cor=str(input("Qual a cor do carro? "))
motando.cavalos=str(input("Quantos cavalos? "))
print(motando.monteseucarro())

class sanduichi:
    def recheio(self):
        return f"{self.recheio1},{self.recheio2},{self.recheio3},{self.recheio4}"
pao=sanduichi()
pao.recheio1=str(input("Qual o seu primeiro recheio? "))
pao.recheio2=str(input("Qual o seu segundo recheio? "))
pao.recheio3=str(input("Qual o seu terceiro recheio? "))
pao.recheio4=str(input("Qual  o seu quarto recheio? "))
print(pao.recheio())

class redesocial:
    def seguir(self):
        return f"{self.seguidor1}\n{self.seguidor2}"
follow=redesocial()
follow.seguidor1=str(input("Deseja seguir gabriel?"))
follow.seguidor2=str(input("Deseja seguir tamires"))
print(follow.seguir())