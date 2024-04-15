import random
import math
import time

# Coordenadas das cidades
cidades = [(0, 0), (1, 2), (3, 1), (5, 3), (2, 4), (4, 0), (2, 1), (1, 3), (4, 2), (3, 0)]

# Função para calcular a distância entre duas cidades
def calcular_distancia(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

# Função para calcular a aptidão de um indivíduo
def calcular_aptidao(individuo):
    distancia_total = 0
    for i in range(len(individuo)):
        cidade_atual = cidades[individuo[i]]
        cidade_proxima = cidades[individuo[(i+1) % len(individuo)]]
        distancia_total += calcular_distancia(cidade_atual, cidade_proxima)
    return 1 / (distancia_total + 1) # +1 para evitar divisão por zero

# Função para gerar uma população inicial
def gerar_populacao_inicial(tamanho_populacao):
    return [random.sample(range(len(cidades)), len(cidades)) for _ in range(tamanho_populacao)]

# Função para selecionar indivíduos para reprodução
def selecao(populacao):
    aptidoes = [calcular_aptidao(individuo) for individuo in populacao]
    return random.choices(populacao, weights=aptidoes, k=len(populacao))

# Função para realizar o crossover
def crossover(individuo1, individuo2):
    ponto = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto] + [gene for gene in individuo2 if gene not in individuo1[:ponto]]
    filho2 = individuo2[:ponto] + [gene for gene in individuo1 if gene not in individuo2[:ponto]]
    return filho1, filho2

# Função para realizar a mutação
def mutacao(individuo):
    if random.random() < 0.01: # Taxa de mutação de 1%
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# Algoritmo genético
def algoritmo_genetico(tamanho_populacao, num_geracooes):
    populacao = gerar_populacao_inicial(tamanho_populacao)
    for _ in range(num_geracooes):
        populacao = selecao(populacao)
        nova_populacao = []
        for i in range(0, len(populacao), 2):
            filho1, filho2 = crossover(populacao[i], populacao[i+1])
            nova_populacao.append(mutacao(filho1))
            nova_populacao.append(mutacao(filho2))
        populacao = nova_populacao
    return max(populacao, key=calcular_aptidao)

# Executando o algoritmo genético
tamanho_populacao = 100
num_geracoes = 1000
inicio = time.time()
melhor_solucao = algoritmo_genetico(tamanho_populacao, num_geracoes)
fim = time.time()

# Imprimindo a melhor solução encontrada e o tempo de execução
print("Melhor solução encontrada:", melhor_solucao)
print("Tempo de execução:", fim - inicio, "segundos")
