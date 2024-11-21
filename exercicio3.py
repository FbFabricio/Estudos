class Carro:
    def __init__(self,nome):
        self.nome = nome


class Motor:
    def __init__(self, nome, modelo):
        self._nome = nome
        self.modelo = modelo
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome 


class Fabricante:
    def __init__(self, nome, modelo, fabricante):
        self._nome = nome
        self._modelo = modelo
        self.fabricante = fabricante


c1 = Carro('kwid') 
c2 = Motor(c1.nome, 'k4m')
c3 = Fabricante(c2._nome, c2.modelo, 'renault')

print(c2.nome, c2.modelo)
print(c3._nome, c3._modelo, c3.fabricante)