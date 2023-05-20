"""
biblioteca de operações usada para fazer a questão de n-rainhas usando algoritmos genéticos
"""
import random
import copy


# fitnees function
def fitness(cromossomo):
    fitness = 0
    n = len(cromossomo)
    for i in range(n):
        for j in range(n):
            if abs(i - j) == abs(cromossomo[i] - cromossomo[j]) and i != j:
                fitness = fitness + 1
    return fitness // 2


# selecao de pais
def selecionaPais(populacao, k):
    pais = []

    for _ in range(2):
        pai = torneio(populacao, k)
        pais.append(pai)
    return pais


# torneio
def torneio(populacao, k):
    lst_torneio = []
    for _ in range(k):
        individuo = copy.deepcopy(populacao[random.randint(0, len(populacao) - 1)])
        lst_torneio.append(individuo)
    lst_torneio.sort(key=lambda e: fitness(e), reverse=False)

    return copy.deepcopy(lst_torneio[0])


# cruzamento
def cruzamento(pai1, pai2):
    tam_pai1 = len(pai1)
    pos = random.randint(0, (tam_pai1 - 1))

    filho1 = copy.deepcopy(pai1)
    filho2 = copy.deepcopy(pai2)
    for i in range(tam_pai1):
        check1 = 0
        check2 = 0
        for j in range(pos):
            if pai2[i] == pai1[j]:
                check1 = 1
            if pai1[i] == pai2[j]:
                check2 = 1
        if check1 == 0:
            filho1[pos] = pai2[i]
        if check2 == 0:
            filho2[pos] = pai1[i]
    return [filho1, filho2]


# mutacao
def mutacao(cromossomo):
    tam_cromossomo = len(cromossomo)
    mult1 = random.randint(0, tam_cromossomo - 1)
    mult2 = random.randint(0, tam_cromossomo - 1)
    dna = cromossomo[mult1]
    cromossomo[mult1] = cromossomo[mult2]
    cromossomo[mult2] = dna
    return cromossomo


def nova_geracao(pop, novos):
    pop.extend(novos)
