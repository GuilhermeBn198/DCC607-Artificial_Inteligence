import random

# Tamanho da população
POP_SIZE = 100

# Taxa de mutação
MUTATION_RATE = 0.1

# Número de gerações
GENERATIONS = 100

# Lista de itens com valor e peso
ITEMS = [(266, 3), (442, 13), (671, 10), (526, 9), (388, 7), (245, 1), (210, 8), (145, 8), (126, 2), (322, 9)]

# Capacidade da mochila
CAPACITY = 35

# Função de avaliação
def fitness(chromosome):
    total_value = 0
    total_weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += ITEMS[i][0]
            total_weight += ITEMS[i][1]
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

# Cria uma população inicial
def create_population():
    population = []
    for i in range(POP_SIZE):
        chromosome = [random.randint(0, 1) for _ in range(len(ITEMS))]
        population.append(chromosome)
    return population

# Seleciona os indivíduos mais aptos
def selection(population):
    population_fitness = [(individual, fitness(individual)) for individual in population]
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    selected = [individual for individual, _ in population_fitness[:int(len(population)/2)]]
    return selected

# Cruzamento (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutação
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Algoritmo genético principal
def genetic_algorithm():
    population = create_population()
    for generation in range(GENERATIONS):
        selected = selection(population)
        new_population = selected[:]

        while len(new_population) < POP_SIZE:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    best_individual, best_fitness = max([(individual, fitness(individual)) for individual in population], key=lambda x: x[1])
    return best_individual, best_fitness

# Executa o algoritmo genético e imprime a melhor solução encontrada
best_individual, best_fitness = genetic_algorithm()
print("Melhor solução encontrada: ", best_individual)
print("Valor da mochila: ", best_fitness)

