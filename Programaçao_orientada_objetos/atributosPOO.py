# atributos de classe  
# atributos como '_idade' ou '__idade' não dever ser usados
# fora da classe 

class Pessoa: 
    ano_atual = 2022 # atributo da classe 

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
        self._idade = idade 
        self.__idade = idade 


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('fabricio', 24)
p2 = Pessoa('helena', 27)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


