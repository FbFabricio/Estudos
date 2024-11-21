# @staticmethod 
# são métodos que estão dentro da classe, não tem acesso 
# ao self nem ao cls.
# São literalmentes funções dentro da classe 

class Exemplo:
    def __init__(self, valor):
        self.valor = valor

    def metodo_instancia(self):
        return self.valor

    @staticmethod
    def metodo_estatico(a, b):
        return a * b

# Criando uma instância
obj = Exemplo(10)

# Método de instância, acessando 'valor' da instância
print(obj.metodo_instancia())  # Saída: 10

# Método estático, não precisa de instância
print(Exemplo.metodo_estatico(3, 4))  # Saída: 12