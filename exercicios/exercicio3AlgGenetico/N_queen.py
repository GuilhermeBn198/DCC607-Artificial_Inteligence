import random

# Tamanho do tabuleiro
n = 8

# Função de avaliação
def fitness(queens):
    attacking = 0
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                attacking += 1
    return 1/(attacking+1)

# Cria uma população inicial
def create_population(size):
    population = []
    for i in range(size):
        population.append([random.randint(0, n-1) for _ in range(n)])
    return population

# Seleciona os indivíduos mais aptos
def selection(population):
    population_fitness = [(individual, fitness(individual)) for individual in population]
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    selected = [individual for individual, _ in population_fitness[:int(len(population)/2)]]
    return selected

# Cruzamento (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, n-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutação
def mutate(individual, mutation_rate):
    for i in range(n):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, n-1)
    return individual

# Algoritmo genético principal
def genetic_algorithm(population_size, mutation_rate, generations):
    population = create_population(population_size)
    for generation in range(generations):
        selected = selection(population)
        new_population = selected[:]
        while len(new_population) < population_size:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.append(child1)
            if len(new_population) < population_size:
                new_population.append(child2)
        population = new_population
    return max([(individual, fitness(individual)) for individual in population], key=lambda x: x[1])[0]

# Executa o algoritmo genético
solution = genetic_algorithm(population_size=100, mutation_rate=0.1, generations=100)

print(solution)
