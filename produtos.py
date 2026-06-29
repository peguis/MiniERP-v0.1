produtos = []


def cadastrar_produto(nome, preco, estoque):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    return produto