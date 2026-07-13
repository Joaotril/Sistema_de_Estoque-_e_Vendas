produtos = []
def cadastrar():
    print("Cadastre um novo produto:")
    nome_produto = input('Nome do produto: ')
    cod_produto = int(input('Código do produto: '))
    preco_produto = float(input('Preço(R$): '))
    produto = {'nome': nome_produto,
               'Codigo': cod_produto,
               'Preco': preco_produto}
    produtos.append(produto)
  
def listar():
    print("Lista de todos os produtos disponíveis")
    for produto in produtos:
        print(f'''
Nome: {produto['nome']}
Código: {produto['Codigo']}
Preço: {produto['Preco']}''')


def pesquisar():
    pesquisa = input("Pesquise um produto:")
    for produto in produtos:
        if pesquisa == produto['nome']:
            print(f'''
-------Este produto está a venda-------
Nome: {produto['nome']}
Código: {produto['Codigo']}
Preço: {produto['Preco']}''')
    print('O produto está em falta')
def alterar():
    alteracao = input('Digite o item que você deseja alterar')
    for produto in produtos:
        if alteracao == produto['nome']:
            print('''
1.Alterar nome
2.Alterar código
3.Alterar preço''')
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
    print('Produto não encontrado')    
def deletar():
    produto_remover = input('Digite qual produto você deseja deletar')
    for produto in produtos:
        if produto_remover == produto['nome']:
            produtos.remove(produto)
        return print('Produto excluído com sucesso')
    print('Produto não encontrado')