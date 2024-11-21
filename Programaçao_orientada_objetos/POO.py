''' Classes -> molde para novos objetos
    Dataclasse -> escreve classes de maneira mais legível e limpa'''

from dataclasses import dataclass

# class Pessoa:
#     # toda função in class é um método

#     def __init__(self,nome,idade): # método init 
#         self.nome = nome 
#         self.idade = idade # self se refere a instância atual da classe 



# p1 = Pessoa('fabricio', 23)

# p2 = Pessoa('Vithória', 28)

# print(p1.nome)
# print(p2.nome)

@dataclass # decorador 
class Cliente: 
    # método init automático 
    nome: str
    email: str       
    idade: int

    def exibir(self): # método 
        print(f'nome {self.nome}, email {self.email}, idade {self.idade}')


fabricio = Cliente(nome='fabricio', email='fb@fb.com', idade=24)


fabricio.exibir()