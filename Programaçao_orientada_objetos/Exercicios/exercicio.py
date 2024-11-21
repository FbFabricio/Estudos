''' Salve sua classe em JSON 
E depois cria novamente sua classe'''

CAMINHO_ARQUVIO = 'json_exercicio.json'
import json

class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome 
        self.idade = idade 

p1 = Pessoa('fabricio',24)

bd = [vars(p1)]

with open(CAMINHO_ARQUVIO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)