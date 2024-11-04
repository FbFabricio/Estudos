def pesquisa_binaria(lista, item):
    global contador # variavel global 

    baixo = 0 
    alto = len (lista) - 1 
    contador = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2 
        chute = lista[meio]
        contador += 1 

        if chute == item:
            return meio 
        if chute > item:
            alto = meio - 1 
        else:
            baixo = meio - 1 
    
    return None

def mostrar_contador():
    print(f'o script rodou {contador} vezes')

minha_lista = list(range(1,129))
minha_lista_salva = minha_lista

print(pesquisa_binaria(minha_lista_salva,128))
mostrar_contador()

print(pesquisa_binaria(minha_lista_salva,12))
mostrar_contador()

