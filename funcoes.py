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
    
def calcula_pontos_quadra(lista_faces):
    soma_faces = 0

    for face in lista_faces:
        soma_faces += face

    frequencias = {}
    for face in lista_faces:
        if face not in frequencias:
            frequencias[face] = 1
        else:
            frequencias[face] += 1
    
    for count in frequencias.values():
        if count >= 4:
            return soma_faces
    
    return 0


def calcula_pontos_quina(dados):
    if len(dados) < 5:
        return 0
    for num in dados:
        if dados.count(num) >= 5:
            return 50
    return 0


def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(list_dados, categoria, dict_cartelas_pontos):
    regra_avancada = calcula_pontos_regra_avancada(list_dados)
    regra_simples = calcula_pontos_regra_simples(list_dados)

    if categoria in regra_avancada:
        dict_categorias = dict_cartelas_pontos['regra_avancada']
        for cat_pontos in dict_categorias:
            dict_categorias[categoria] = regra_avancada[categoria]

    elif int(categoria) in regra_simples:
        categoria = int(categoria)
        dict_categorias = dict_cartelas_pontos['regra_simples']
        for cat_pontos in dict_categorias:
            dict_categorias[categoria] = regra_simples[categoria]

    return dict_cartelas_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)