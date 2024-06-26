# O objetivo da tarefa é implementar o Algoritmo A_Estrela (Algoritmo A\*). O programa deve ser capaz de solucionar o problema do Mapa da Romênia e problemas da mesma classe. A tarefa é individual e deve ser original. Um documento descrevendo a linguagem usada, a versão e o ambiente de execução, deve ser elaborado para orientar usuários a utilizar o programa

As linguagens empregadas podem ser C, C++, Java, ou Python.

Importante: Envie o código-fonte e não o executável.

## Resposta

- O problema do mapa da Romênia é um exemplo clássico de como encontrar o caminho mais curto entre duas cidades em um mapa que mostra as estradas que conectam as cidades. É um problema de busca em um grafo, onde os vértices representam as cidades e as arestas representam as estradas que as ligam.
- O problema do mapa da Romênia começa com um mapa que mostra as cidades e as estradas que as conectam. Cada estrada tem um comprimento que indica a distância entre as cidades que ela liga. O objetivo do problema é encontrar o caminho mais curto entre duas cidades especificadas no mapa, ou seja, a rota que requer menos tempo ou recursos para ser percorrida. Para resolver esse problema, é necessário percorrer o grafo de maneira eficiente, avaliando as distâncias entre as cidades e escolhendo o caminho mais curto possível.
- O algoritmo A* é uma técnica de busca heurística que pode ser aplicada para encontrar o caminho mais curto entre dois pontos em um grafo. Ele usa uma heurística para estimar a distância restante do nó atual até o nó de destino, juntamente com a distância já percorrida, para determinar qual nó deve ser explorado a seguir. Essa combinação de informações é usada para escolher o caminho mais eficiente, enquanto explora o grafo de forma inteligente. O algoritmo A* é uma mistura da busca de custo uniforme e da busca heurística informada, tornando-o uma técnica poderosa para resolver problemas de caminhos mais curtos.
- O problema do mapa da Romênia é um exemplo popular usado para demonstrar como o algoritmo A* e outros algoritmos de busca operam. É comumente usado como um problema padrão para avaliar a eficiência de diferentes algoritmos de busca. Para resolvê-lo, podemos seguir os passos necessários para encontrar o caminho mais curto entre duas cidades na Romênia, usando o mapa com as estradas que as conectam.

## Dos passos para se resolver o problema

1. Para resolver o problema do mapa da Romênia, é necessário representar as cidades e as estradas que as conectam em forma de um grafo. Nesse grafo, cada cidade é considerada um nó, e cada estrada é considerada uma aresta que conecta dois nós.
2. Em seguida, é preciso estabelecer as distâncias entre cada cidade, o que pode ser feito por meio de uma matriz de adjacência. Cada posição dessa matriz representa a distância entre a cidade i e a cidade j. Além disso, é importante definir uma heurística que estime a distância restante do nó atual até o nó de destino. Uma heurística comum é a distância em linha reta entre as duas cidades, que é considerada admissível, pois nunca superestima a distância real entre elas.
3. Para resolver o problema do mapa da Romênia com o algoritmo A*, é necessário começar pelo nó de origem e utilizar a heurística para estimar a distância restante até o nó de destino. Em seguida, é preciso selecionar o nó que possui o menor custo total, que é a soma da distância já percorrida e da estimativa da distância restante, e expandir seus vizinhos. Esse processo deve ser repetido até que o nó de destino seja alcançado, sempre selecionando e expandindo os nós com menor custo total.
4. Para obter o caminho mais curto do nó de origem ao nó de destino no problema do mapa da Romênia utilizando o algoritmo A*, é preciso armazenar o nó anterior de cada nó visitado durante a busca. Com essa informação, é possível percorrer de volta do nó de destino até o nó de origem e determinar o caminho mais curto. Esse processo é realizado utilizando a sequência de nós visitados e seus respectivos nós anteriores, que permitem traçar o caminho completo a ser percorrido.

O código-fonte para a solução e seus arquivos está em [click here](../exercicio2Aestrela/)

## Acerca do código apresentado acima

- O código é uma implementação do algoritmo A* para encontrar o caminho mais curto em um grafo com pesos.
- A função heuristic é utilizada para estimar a distância restante até o nó de destino, e é passada como parâmetro para a função a_star.
- A função a_star implementa o algoritmo em si, utilizando uma fila de prioridade para selecionar o nó com o menor custo total e explorando seus vizinhos. A cada passo, atualiza o custo total até o nó atual e o nó anterior de cada nó visitado para rastrear o caminho mais curto. Quando o nó de destino é alcançado, rastreia o caminho mais curto e retorna.
- A função main lê o mapa e as heurísticas dos arquivos de texto, define o nó inicial e o nó de destino, executa o algoritmo A* e exibe o caminho mais curto e o custo total.
