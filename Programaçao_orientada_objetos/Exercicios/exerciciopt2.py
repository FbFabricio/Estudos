from Programaçao_orientada_objetos.Exercicios.exercicio import CAMINHO_ARQUVIO, Pessoa
import json

with open(CAMINHO_ARQUVIO,'r') as arquivo:
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    

    print(p1.nome, p1.idade)