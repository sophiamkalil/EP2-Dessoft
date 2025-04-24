import random

def rolar_dados(numero_dados):
    lista_valores_dados = []

    for i in range(numero_dados):
        valor_dado = random.randint(1,6)
        lista_valores_dados.append(valor_dado)
    
    return lista_valores_dados

