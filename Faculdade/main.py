
while True :

    entrada = int(input('\n x---- Gerenciamento de estoque ----x'
                           '\n (1) Cadastrar Produto'
                           '\n (2) Consultar Produto'
                           '\n (3) Atualizar Produto'
                           '\n (4) Relatorio de Produtos'
                           '\n (5) Historico de Movimentações'
                           '\n (6) SAIR'
                           '\n = = = = = = = = = = = = = = = = = ='
                           '\n Digite uma opção: '
                        ))
        
    estoque = {}
    
    if entrada == 1:
        # Cadastrar produto 
        def cadastrar_produto(codigo, nome, quantidade, preco):
                if codigo in estoque:
                    print("Produto já cadastrado.")
                else:
                    estoque[codigo] = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
                    print(f"Produto {nome} cadastrado com sucesso.")

    if entrada == 2:
        # Consultar o produto
        def consultar_produto(codigo):
                if codigo in estoque:
                    return estoque[codigo]
                else:
                    print("Produto não encontrado.")
                    return None
                
            # Historico 
    historico_movimentacoes = []

    if entrada == 3:
            # Registro de entrada
        def registrar_entrada(codigo, quantidade):
                    if codigo in estoque:
                        estoque[codigo]['quantidade'] += quantidade
                        historico_movimentacoes.append({'tipo': 'entrada', 'codigo': codigo, 'quantidade': quantidade})
                        print(f"Entrada de {quantidade} unidades do produto {codigo} registrada com sucesso.")
                    else:
                        print("Produto não encontrado.")

            
    if entrada == 4:
            # Relatório de movimentações
        def gerar_relatorio_estoque():
                print("Relatório de Estoque:")
                for codigo, detalhes in estoque.items():
                    print(f"Código: {codigo}, Nome: {detalhes['nome']}, Quantidade: {detalhes['quantidade']}, Preço: {detalhes['preco']}")

            # Historico de movimentação de produto especifico
        def consultar_historico_movimentacoes(codigo):
            print(f"Histórico de Movimentações do Produto {codigo}:")
            for movimentacao in historico_movimentacoes:
                    if movimentacao['codigo'] == codigo:
                        print(f"Tipo: {movimentacao['tipo']}, Quantidade: {movimentacao['quantidade']}")

