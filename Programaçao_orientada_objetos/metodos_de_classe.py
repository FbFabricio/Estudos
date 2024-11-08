''' Métods de clase + factories (factorie method)
São metodos onde 'self' será 'cls'(a classe em si), ou seja ao 
invés de receber a instância no primeiro parâmetro,
recebos a própria classe.'''
# factory method -> usado para criar objetos em vez de 
# usar uma chamada direta da classe.

# class Pessoa:
#     ano = 2024 # atributo de classe

#     def __init__(self, nome, idade):
#         self.nome = nome 
#         self.idade = idade

#     @classmethod
#     def metodo_de_classe(cls): # o parametro é a classe
#         print('hey')

#     @classmethod
#     def criar_com_50anos(cls,nome): # o parametro é a classe
#         return cls(nome, 50)


# p1 = Pessoa('joão', 34)
# p2 = Pessoa.criar_com_50anos('fabricio')

# print(Pessoa.ano)
# print(p2.nome, p2.idade)
# print(p1.nome, p1.idade)

# Pessoa.metodo_de_classe()

# methos vs @classmethod vs @staticmethod 


class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        self.user = user 
    

    def set_password(self, password):
        self.password = password 

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user 
        connection.password = password
        return connection 

    @staticmethod
    def soma(x, y):
        return x + y        

c1 = Connection()
c1.set_user('fabricio')
c1.set_password('2020395')

print(c1.password, c1.user)



