def cadastrar_produto(estoque, codigo, nome, quantidade, preco): 
    if any(produto['codigo'] == codigo for produto in estoque):
        print("Produto já cadastrado.")
    else:
        estoque.append({'codigo': codigo, 'nome': nome, 'quantidade': quantidade, 'preco': preco})
        print(f"Produto {nome} cadastrado com sucesso.")

def consultar_produto(estoque, codigo):  
    for produto in estoque:
        if produto['codigo'] == codigo: 
            return produto
    return None

def registrar_entrada(estoque, historico, codigo, quantidade):
    produto = consultar_produto(estoque, codigo)
    if produto:
        produto['quantidade'] += quantidade
        historico.append({'tipo': 'entrada', 'codigo': codigo, 'quantidade': quantidade})
        print(f"Entrada de {quantidade} unidades do produto {codigo} registrada com sucesso.")
    else:
        print("Produto não encontrado.")

def gerar_relatorio_estoque(estoque):
    print("Relatório de Estoque:")
    for produto in estoque:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

def consultar_historico_movimentacoes(historico, codigo):
    print(f"Histórico de Movimentações do Produto {codigo}:")
    for movimentacao in historico:
        if movimentacao['codigo'] == codigo:
            print(f"Tipo: {movimentacao['tipo']}, Quantidade: {movimentacao['quantidade']}")

estoque = [
    {'codigo': '12345', 'nome': 'Notebook', 'quantidade': 10, 'preco': 3500.00},
    {'codigo': '67890', 'nome': 'Mouse', 'quantidade': 50, 'preco': 50.00},
    {'codigo': '54321', 'nome': 'Teclado', 'quantidade': 30, 'preco': 100.00},
    {'codigo': '09876', 'nome': 'Monitor', 'quantidade': 15, 'preco': 800.00},
    {'codigo': '9001', 'nome': 'fone de ouvido', 'quantidade': 16, 'preco': 5.00},


]

historico_movimentacoes = []

while True:
    entrada = int(input('\n x---- Gerenciamento de estoque ----x'
                        '\n (1) Cadastrar Produto'
                        '\n (2) Consultar Produto'
                        '\n (3) Atualizar Produto'
                        '\n (4) Relatório de Produtos'
                        '\n (5) Histórico de Movimentações'
                        '\n (6) SAIR'
                        '\n = = = = = = = = = = = = = = = = = ='
                        '\n Digite uma opção: '
                        ))

    if entrada == 1:
        codigo = input('Digite o código do produto: ')
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o preço do produto: '))
        cadastrar_produto(estoque, codigo, nome, quantidade, preco)
    
    elif entrada == 2:
        codigo = input('Informe o código do produto: ')
        produto = consultar_produto(estoque, codigo)
        if produto:
            print(f"Produto encontrado: {produto}")
        else:
            print("Produto não encontrado.")
    
    elif entrada == 3:
        codigo = input('Digite o código do produto: ')
        quantidade = int(input('Digite a quantidade a adicionar: '))
        registrar_entrada(estoque, historico_movimentacoes, codigo, quantidade)
    
    elif entrada == 4:
        gerar_relatorio_estoque(estoque)
    
    elif entrada == 5:
        codigo = input('Informe o código do produto: ')
        consultar_historico_movimentacoes(historico_movimentacoes, codigo)
    
    elif entrada == 6:
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
