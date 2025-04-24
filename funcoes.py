import random

def rolar_dados(numero_dados):
    lista_valores_dados = []

    for i in range(numero_dados):
        valor_dado = random.randint(1,6)
        lista_valores_dados.append(valor_dado)
    
    return lista_valores_dados

def guardar_dado(lista_dados_rolados, lista_dados_estoque, indice): #indice: indice da lista de dados rolados que deve ser passado para os dados estocados
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

def remover_dado(lista_dados_rolados, lista_dados_estoque, indice): #indice: indice da lista de daodos estocados que deve ser removido e ir para a lista de daods rolados
    lista_rolados_estoque = []
    dados_estoque = []
    dado_removido = lista_dados_estoque[indice]
    lista_dados_rolados.append(dado_removido)

    for i in range(len(lista_dados_estoque)):
        if i != indice:
            dados_estoque.append(lista_dados_estoque[i])

    lista_rolados_estoque.append(lista_dados_rolados)
    lista_rolados_estoque.append(dados_estoque)

    return lista_rolados_estoque

