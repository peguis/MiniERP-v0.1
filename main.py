import os


def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("=" * 40)
    print("         MINI ERP v0.1")
    print("=" * 40)
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Alterar preço")
    print("4 - Alterar estoque")
    print("5 - Remover produto")
    print("6 - Sair")
    print("=" * 40)


def main():
    while True:
        limpar_tela()
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n[Cadastro de produto - Em desenvolvimento]")
        elif opcao == "2":
            print("\n[Listagem de produtos - Em desenvolvimento]")
        elif opcao == "3":
            print("\n[Alteração de preço - Em desenvolvimento]")
        elif opcao == "4":
            print("\n[Alteração de estoque - Em desenvolvimento]")
        elif opcao == "5":
            print("\n[Remoção de produto - Em desenvolvimento]")
        elif opcao == "6":
            print("\nObrigado por utilizar o MiniERP!")
            break
        else:
            print("\nOpção inválida!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()