# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
# 

# # class Caneta: 
# #     def __init__(self, cor):
# #         self.cor_tinta = cor 

# #     @property # faz um metodo se comportar como atributo
# #     def cor(self):
# #         return self.cor_tinta

# #     @property
# #     def cor_tampa(self):
# #         return 'qualquer coisa'
    

# # caneta = Caneta('Azul')


# # print(caneta.cor)
# # print(caneta.cor)
# # print(caneta.cor)
# # print(caneta.cor_tampa)
# # print(caneta.cor_tampa)


###################################################################################

''' Property + setter '''

# property -> faz um metodo se comportar como um atributo 
# setter -> defini o comportamento ao modificar o atributo 
# para ter um setter eu preciso ter uma property

class Caneta: 
     def __init__(self, cor):
         self._cor = cor 

     @property # faz um metodo se comportar como atributo
     def cor(self):
        print('property')
        return self._cor
     
     @cor.setter # settet tem que receber um valor 
     def cor(self, valor):
         print(valor)
         self._cor = valor 


caneta = Caneta('Azul')
caneta.cor = 'rosa'
print(caneta.cor)

