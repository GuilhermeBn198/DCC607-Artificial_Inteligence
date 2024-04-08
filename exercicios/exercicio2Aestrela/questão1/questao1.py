import heapq


# Define a função heurística para estimar a distância restante até o nó de destino
def heuristic(node, heuristic_dict):
    return heuristic_dict.get(node, float("inf"))


# Implementa o algoritmo A*
def a_star(graph, start, end, heuristic_dict):
    # Cria uma fila de prioridade com o nó inicial
    priority_queue = [(0, start)]
    # Armazena os nós já visitados
    visitados = set()
    # Armazena o custo total até o nó atual
    g = {start: 0}
    # Armazena o nó anterior de cada nó visitado para rastrear o caminho mais curto
    pai = {start: None}

    # Continua a busca até que a fila de prioridade esteja vazia
    while priority_queue:
        # Seleciona o nó com o menor custo total
        _, no_atual = heapq.heappop(priority_queue)
        # Se o nó selecionado for o nó de destino, rastreia o caminho mais curto e retorna
        if no_atual == end:
            caminho = []
            while no_atual is not None:
                caminho.append(no_atual)
                no_atual = pai[no_atual]
            # Inverte o caminho para exibir a ordem correta e retorna o caminho e o custo total
            caminho.reverse()
            return caminho, g[end]

        # Adiciona o nó atual à lista de visitados
        visitados.add(no_atual)

        # Explora os vizinhos do nó atual
        for vizinho, custo in graph[no_atual].items():
            # Ignora os vizinhos já visitados
            if vizinho in visitados:
                continue

            # Calcula o custo total até o vizinho e atualiza se for menor que o custo atual
            pontuacao_g = g[no_atual] + custo
            if pontuacao_g < g.get(vizinho, float("inf")):
                pai[vizinho] = no_atual
                g[vizinho] = pontuacao_g
                # Calcula o custo total estimado do caminho e adiciona o vizinho à fila de prioridade
                f = pontuacao_g + heuristic(vizinho, heuristic_dict)
                heapq.heappush(priority_queue, (f, vizinho))
                print(f"Caminho atual: {no_atual}")

    # Retorna nulo se não encontrar um caminho
    return None, None


# Define a função principal
def main():
    # Lê o mapa da Romênia e as heurísticas dos arquivos de texto
    with open("Romenia.txt", "r") as f:
        romenia_mapa = eval(f.read())

    with open("Heuristica.txt", "r") as f:
        heuristic_dict = eval(f.read())

    # Define o nó inicial e o nó de destino
    inicio = "Arad"
    fim = "Bucharest"

    # Executa o algoritmo A*
    caminho, custo = a_star(romenia_mapa, inicio, fim, heuristic_dict)

    # Exibe o caminho mais curto e o custo total
    if caminho is not None:
        print(f"Caminho encontrado: {caminho}")
        print(f"Custo total: {custo}")
    else:
        print("Caminho não encontrado")


# Chama a função principal se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
