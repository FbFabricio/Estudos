# Gerenciamento de estoque 
estoque = {}

# Cadastro de produto
def cadastrar_produto(codigo, nome, quantidade, preco):
    if codigo in estoque:
        print("Produto já cadastrado.")
    else:
        estoque[codigo] = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
        print(f"Produto {nome} cadastrado com sucesso.")

# Função para consultar um produto
def consultar_produto(codigo):
    if codigo in estoque:
        return estoque[codigo]
    else:
        print("Produto não encontrado.")
        return None

# Lista para armazenar o histórico de movimentações
historico_movimentacoes = []

# Função para registrar entrada de produtos
def registrar_entrada(codigo, quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
        historico_movimentacoes.append({'tipo': 'entrada', 'codigo': codigo, 'quantidade': quantidade})
        print(f"Entrada de {quantidade} unidades do produto {codigo} registrada com sucesso.")
    else:
        print("Produto não encontrado.")

# Função para registrar saída de produtos
def registrar_saida(codigo, quantidade):
    if codigo in estoque:
        if estoque[codigo]['quantidade'] >= quantidade:
            estoque[codigo]['quantidade'] -= quantidade
            historico_movimentacoes.append({'tipo': 'saida', 'codigo': codigo, 'quantidade': quantidade})
            print(f"Saída de {quantidade} unidades do produto {codigo} registrada com sucesso.")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

# Função para gerar relatório do estoque
def gerar_relatorio_estoque():
    print("Relatório de Estoque:")
    for codigo, detalhes in estoque.items():
        print(f"Código: {codigo}, Nome: {detalhes['nome']}, Quantidade: {detalhes['quantidade']}, Preço: {detalhes['preco']}")

# Função para gerar relatório de movimentações
def gerar_relatorio_movimentacoes():
    print("Relatório de Movimentações:")
    for movimentacao in historico_movimentacoes:
        print(f"Tipo: {movimentacao['tipo']}, Código: {movimentacao['codigo']}, Quantidade: {movimentacao['quantidade']}")

# Função para consultar histórico de movimentações de um produto
def consultar_historico_movimentacoes(codigo):
    print(f"Histórico de Movimentações do Produto {codigo}:")
    for movimentacao in historico_movimentacoes:
        if movimentacao['codigo'] == codigo:
            print(f"Tipo: {movimentacao['tipo']}, Quantidade: {movimentacao['quantidade']}")

cadastrar_produto('codigo','maça',1, 20)
print(consultar_produto('codigo'))
