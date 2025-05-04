#Implementação do jogo Yacht Dice
from funcoes import *

cartela= {
    'regra_simples':{
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela)
i = 0
list_combinacaoes = []
while i < 12:
    dados_rolados = rolar_dados(5)
    dados_estoque = []

    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_estoque}')
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    escolha = input('>')

    rerrolagem = 0
    while i < 12:
        if int(escolha) in [1, 2, 3, 4, 5, 0]:
            if int(escolha) == 1:
                print('Digite o índice do dado a ser guardado (0 a 4):')
                acao = int(input('>'))
                guardar = guardar_dado(dados_rolados, dados_estoque, acao)
                dados_rolados = guardar[0]
                dados_estoque = guardar[1]
            elif int(escolha) == 2:
                print("Digite o índice do dado a ser removido (0 a 4):")
                acao = int(input('>'))
                remover = remover_dado(dados_rolados,dados_estoque,acao)
                dados_rolados = remover[0]
                dados_estoque = remover[1]
            elif int(escolha) == 3:
                if rerrolagem < 2:
                    dados_rolados = rolar_dados(len(dados_rolados))
                    rerrolagem +=1
                else:
                    print("Você já usou todas as rerrolagens.")
            elif int(escolha) == 4:
                imprime_cartela(cartela)
            elif int(escolha) == 0:
                combinacoes = ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
                print("Digite a combinação desejada:")
                acao = input('>')
                while acao not in combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    acao = input('>')
                if acao not in list_combinacaoes:
                    list_combinacaoes.append(acao)
                else:
                    while acao in list_combinacaoes:
                        print("Essa combinação já foi utilizada.")
                        acao = input('>')
                    list_combinacaoes.append(acao)
                cartela = faz_jogada(dados_estoque, acao, cartela)
                rerrolagem = 0 
                i+=1
                break

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_estoque}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = int(input('>'))

        else:
            print('Opção inválida. Tente novamente.')
            escolha = int(input('>'))

pontuacao = 0
dict_categoria = cartela['regra_simples']
for pontos in dict_categoria.values():
    pontuacao += pontos
    if pontuacao >= 63:
        pontuacao += 35
dict_categoria = cartela['regra_avancada']
for pontos in dict_categoria.values():
    pontuacao += pontos

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")

