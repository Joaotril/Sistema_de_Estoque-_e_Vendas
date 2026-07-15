produtos = []
def cadastrar():
    print("\033c", end="")
    print("=======Cadastre um novo produto=======")
    nome_produto = input('Nome do produto: ')
    cod_produto = int(input('Código do produto: '))
    preco_produto = float(input('Preço(R$): '))
    quant_produto = int(input('Digite a quantidade em estoque: '))
    produto = {'nome': nome_produto,
               'Codigo': cod_produto,
               'Preco': preco_produto,
               'quant':quant_produto}
    produtos.append(produto)
    print('Produto cadastrado com sucesso!')
def listar():
    print("\033c", end="")
    print("=======Lista de todos os produtos disponíveis=======")
    for produto in produtos:
        print(f'''
Nome: {produto['nome']}
Código: {produto['Codigo']}
Preço: R${produto['Preco']}
Estoque: {produto['quant']} ''')


def pesquisar():
    print("\033c", end="")
    pesquisa = input("Pesquise um produto:")
    for produto in produtos:
        if (pesquisa == produto['nome'] or pesquisa == str(produto['Codigo'])) and produto['quant'] > 0:
            print(f'''
=======Este produto está a venda=======
Nome: {produto['nome']}
Código: {produto['Codigo']}
Preço: {produto['Preco']}
Estoque: {produto['quant']} ''')
            return
    print('O produto está em falta ou não existe')
def alterar():
    print('=======Alterar produto=======')
    alteracao = input('Digite o item que você deseja alterar: ')
    for produto in produtos:
        if alteracao == produto['nome'] or alteracao == str(produto['Codigo']):
            print("\033c", end="")
            print('''=======Alterar produto=======
1.Alterar nome
2.Alterar código
3.Alterar preço
4.Alterar quantidade''')
            escolha_alteracao = int(input())
            if escolha_alteracao == 1:
                nome_produto = input('Nome do produto: ')
                produto['nome'] = nome_produto
                return print('Nome alterado com sucesso!')
            elif escolha_alteracao == 2:
                cod_produto = int(input('Código do produto: '))
                produto['Codigo'] = cod_produto
                return print('Código do produto alterado com sucesso!')
            elif escolha_alteracao == 3:
                preco_produto = float(input('Preço(R$): '))
                produto['Preco']= preco_produto
                return print('Preço do produto alterado com sucesso!')
            elif escolha_alteracao == 4:
                 quant_produto = int(input('Digite a quantidade em estoque: '))
                 produto['quant'] = quant_produto
                 return print('Quantidade em estoque alterado com sucesso!')
    print('Produto não encontrado')    
def deletar():
    produto_remover = input('Digite qual produto você deseja deletar')
    for produto in produtos:
        if produto_remover == produto['nome'] or produto_remover == str(produto['Codigo']):
            produtos.remove(produto)
            print('Produto excluído com sucesso')
            return
    print('Produto não encontrado')
def vendas():
    carrinho = []
    venda = ''
    while True:
        venda = input('Digite o nome/código do produto(S para prosseguir para o total): ')
        if venda.upper() == 'S':
            break
        encontrado = False
        for produto in produtos:
            if venda == produto['nome'] or venda == str(produto['Codigo']):
                encontrado = True
                quant_venda = int(input('Quantidade: '))
                if quant_venda <= produto['quant']:
                    produto['quant'] = produto['quant'] - quant_venda
                    itens = {'nome': produto['nome'],
                'preco': produto['Preco'],
                'quantidade':quant_venda}
                    carrinho.append(itens)
                else:
                    print("Estoque insuficiente")
        if encontrado == False:
            print('Produto não encontrado')
    print("\033c", end="")
    print('''-------Carrinho------''')
    total = 0
    for itens in carrinho:
        total_item = itens['preco'] * itens['quantidade']
        total += total_item
        print(f'''
{itens["nome"]}
{itens["quantidade"]}x R$ {itens["preco"]:.2f}       Subtotal: R$ {total_item:.2f}
''')
    print(f"TOTAL DA COMPRA: R$ {total:.2f}")
    print('TENHA UM ÓTIMO DIA!!!')