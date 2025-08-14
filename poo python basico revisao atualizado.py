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