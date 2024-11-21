# __dict__ e vars para atributos de instância
''' __dict__ é um dicionário que armazena os atributos de instância de um objeto.'''

class Pessoa: 
    ano_atual = 2022 

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('fabricio', 24)

p1.__dict__['outra'] = 'coisa' # criando nova chave-valor

print(p1.__dict__)
print(vars(p1))
