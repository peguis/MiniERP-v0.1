import os
from produtos import cadastrar_produto, listar_produtos, alterar_preco, alterar_estoque, remover_produto


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

            print("\nCadastro de produto")

            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))

            produto = cadastrar_produto(
                nome,
                preco,
                estoque
            )

            print("\nProduto cadastrado:")
            print(produto)


        elif opcao == "2":

            print("\nProdutos cadastrados:")

            lista = listar_produtos()

            if not lista:
                print("Nenhum produto cadastrado.")
            else:
                for produto in lista:
                    print("-" * 30)
                    print(f"Nome: {produto['nome']}")
                    print(f"Preço: R$ {produto['preco']:.2f}")
                    print(f"Estoque: {produto['estoque']}")


        elif opcao == "3":
            print("\nAlterar preço")

            nome = input("Nome do produto: ")

            novo_preco = float(
            input("Novo preço: ")
            )

            resultado = alterar_preco(
                nome,
                novo_preco
            )

            if resultado:
                print("Preço alterado com sucesso!")
            else:
                print("Produto não encontrado.")


        elif opcao == "4":

            print("\nAlterar estoque")

            nome = input("Nome do produto: ")

            novo_estoque = int(
                input("Novo estoque: ")
            )


            resultado = alterar_estoque(
                nome,
                novo_estoque
            )


            if resultado:

                print("Estoque alterado com sucesso!")

            else:

                print("Produto não encontrado ou estoque inválido.")


        
        elif opcao == "5":

            print("\nRemover produto")

            nome = input("Nome do produto: ")


            removido = remover_produto(nome)


            if removido:

                print("Produto removido com sucesso!")

            else:

                print("Produto não encontrado.")


        elif opcao == "6":
            print("\nObrigado por utilizar o MiniERP!")
            break


        else:
            print("\nOpção inválida!")


        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()