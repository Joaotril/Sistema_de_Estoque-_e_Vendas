from view.menu import menu
from model.model import  cadastrar, listar, pesquisar,alterar,deletar,vendas
def iniciar():
    while True:
        opcao = menu()

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            listar()

        elif opcao == 3:
            pesquisar()
        elif opcao == 4:
            alterar()
        elif opcao == 5:
            deletar()
        elif opcao == 6:
            vendas()
        elif opcao == 0:
            print("Encerrando...")
            break
        input('Enter para voltar ao inicio ')