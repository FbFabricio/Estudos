'''PROGRAMAÇÃO ORIENTADA A OBJETOS'''


class Pessoa:
    
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade



p1 = Pessoa('fabricio', 23)

p2 = Pessoa('Vithória', 28)

print(p1.nome)
print(p2.nome)
