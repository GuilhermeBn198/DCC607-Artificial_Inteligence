from genetica import *  # Import all functions from the genetica module.

# Define the list of items with their weights and values.
pesos_e_valores = [[4, 30], [8, 10], [8, 30], [25, 75],
                   [2, 10], [50, 100], [6, 300], [12, 50],
                   [100, 400], [8, 300]]
peso_maximo = 100  # Define the maximum weight the backpack can carry.
n_de_cromossomos = 150  # Define the number of chromosomes in the population.
geracoes = 80  # Define the number of generations for the genetic algorithm.
n_de_itens = len(pesos_e_valores)  # Calculate the number of items available.
  
# Execute the genetic algorithm.
populacao = population(n_de_cromossomos, n_de_itens)  # Create the initial population.
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]  # Calculate the average fitness of the initial population.
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)  # Evolve the population for each generation.
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))  # Calculate and store the average fitness for each generation.

# Print the results.
for indice, dados in enumerate(historico_de_fitness):
    print("Geracao: ", indice, " | Media de valor na mochila: ", dados)

print("\nPeso máximo:", peso_maximo, "g\n\nItens disponíveis:")
for indice, i in enumerate(pesos_e_valores):
    print("Item ", indice + 1, ": ", i[0], "g | R$", i[1])

print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])

# Generate and display the plot of the average fitness over generations.
from matplotlib import pyplot as plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()
