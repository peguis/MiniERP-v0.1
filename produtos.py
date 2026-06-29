import json
import os


ARQUIVO = "dados/produtos.json"


produtos = []

def cadastrar_produto(nome, preco, estoque):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    salvar_produtos()

    return produto

def listar_produtos():
    return produtos

def alterar_preco(nome, novo_preco):
    for produto in produtos:

        if produto["nome"].lower() == nome.lower():

            produto["preco"] = novo_preco

            salvar_produtos()

            return True

    return False

def alterar_estoque(nome, novo_estoque):

    if novo_estoque < 0:
        return False


    for produto in produtos:

        if produto["nome"].lower() == nome.lower():

            produto["estoque"] = novo_estoque

            salvar_produtos()

            return True


    return False

def remover_produto(nome):

    for produto in produtos:

        if produto["nome"].lower() == nome.lower():

            produtos.remove(produto)

            salvar_produtos()

            return True


    return False

def carregar_produtos():

    global produtos


    if os.path.exists(ARQUIVO):

        with open(
            ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            produtos = json.load(arquivo)

def salvar_produtos():

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            produtos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )