import random

def rolar_dados(numero_dados):
    lista_valores_dados = []

    for i in range(numero_dados):
        valor_dado = random.randint(1,6)
        lista_valores_dados.append(valor_dado)
    
    return lista_valores_dados

def guardar_dado(lista_dados_rolados, lista_dados_estoque, indice):
    dados_rolados = []
    lista_rolados_estoque = []
    dado_armazenado = lista_dados_rolados[indice]
    lista_dados_estoque.append(dado_armazenado)

    for i in range(len(lista_dados_rolados)):
        if i != indice:
            dados_rolados.append(lista_dados_rolados[i])

    lista_rolados_estoque.append(dados_rolados)
    lista_rolados_estoque.append(lista_dados_estoque)

    return lista_rolados_estoque

