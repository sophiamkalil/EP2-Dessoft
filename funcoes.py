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

def calcula_pontos_regra_simples(lista_numeros): #numeros: faces do dado
    dict_pontos = {}
    dict_pontos[1] = 0
    dict_pontos[2] = 0
    dict_pontos[3] = 0
    dict_pontos[4] = 0
    dict_pontos[5] = 0
    dict_pontos[6] = 0

    for numero in lista_numeros:
        if numero in dict_pontos:
            dict_pontos[numero] += numero
        else:
            dict_pontos[numero] = numero 

    return dict_pontos


def calcula_pontos_soma(dados):
    soma = 0
    i = 0
    while i < len(dados):
        soma += dados[i]
        i += 1
    return soma


def calcula_pontos_sequencia_baixa(dados):
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for seq in sequencias:
        todos_presentes = True
        for num in seq:
            if num not in dados:
                todos_presentes = False
                break
        if todos_presentes:
            return 15
            
    return 0


def calcula_pontos_sequencia_alta(dados):
    sequencias = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]
    for seq in sequencias:
        todos_presentes = True
        for num in seq:
            if num not in dados:
                todos_presentes = False
                break
        if todos_presentes:
            return 30
            
    return 0

def calcula_pontos_full_house(lista_faces):
    soma_faces = 0
    
    for face in lista_faces:
        soma_faces += face

    count1 = 0
    for i in range(len(lista_faces)):
        face = lista_faces[0]
        if lista_faces[i] == face:
            count1 += 1
        else:
            face_diferente = lista_faces[i]
    if count1 == 3:
        count = 0
        for i in range(len(lista_faces)):
            if lista_faces[i] == face_diferente:
                count += 1
    
        if count == 2:
            return soma_faces
    elif count1 == 2:
        count = 0
        for i in range(len(lista_faces)):
            if lista_faces[i] == face_diferente:
                count += 1
        if count == 3:
            return soma_faces
    
    return 0
    
        