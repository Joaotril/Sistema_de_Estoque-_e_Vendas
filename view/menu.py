def menu():
    print('''-------Sistema de estoque-------
1. Cadastrar produto
2. Lista todos os produtos
3. Pesquisar um produto
4. Alterar um produto
5. Excluir um produto
0. Sair
''')

    opcao = int(input("Digite a opção desejada: "))
    return opcao


