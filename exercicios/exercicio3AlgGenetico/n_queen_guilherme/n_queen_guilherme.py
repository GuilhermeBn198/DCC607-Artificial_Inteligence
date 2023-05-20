from itertools import permutations
import random
import operacoes


pressao_seletiva = 5
num_rainhas = 7
tam_populacao = 1000
geracoes = tam_populacao

valores_permutacao = []
populacao = []
individuos = []

for x in range(1, num_rainhas + 1):
    valores_permutacao.append(x)

espaco_busca = permutations(valores_permutacao)

contador = 0
for _ in range(tam_populacao):
    for elem in espaco_busca:
        contador += 1
        genes = []
        for gene in elem:
            genes.append(gene)
        individuos.append(genes)

    populacao.append(individuos[random.randint(0, contador)])

try:
    for i in range(geracoes):
        if operacoes.fitness(populacao[i]) == 0:
            solucao = populacao[i]
            print("A solução das posições no tabuleiro:\n")
            print(solucao)
            break

        pais = operacoes.selecionaPais(populacao, pressao_seletiva)

        filhos = operacoes.cruzamento(pais[0], pais[1])

        filhos[0] = operacoes.mutacao(filhos[0])
        filhos[1] = operacoes.mutacao(filhos[1])

        operacoes.nova_geracao(populacao, filhos)
except Exception as e:
    print(e)

print("\nAlgoritmo Genético Finalizado\n")
