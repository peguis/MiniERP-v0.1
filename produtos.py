produtos = []


def cadastrar_produto(nome, preco, estoque):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    return produto

def listar_produtos():
    return produtos

def alterar_preco(nome, novo_preco):
    for produto in produtos:

        if produto["nome"].lower() == nome.lower():

            produto["preco"] = novo_preco

            return True

    return False