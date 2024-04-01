def n_rainhas(n):
  """
  Encontra todas as soluções para o problema das N-rainhas em um tabuleiro NxN.

  Argumentos:
    n: O número de rainhas.

  Retorna:
    Uma lista de listas, onde cada lista representa uma solução com as posições das rainhas no tabuleiro.
  """

  # Tabuleiro inicial vazio
  tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]

  # Lista para armazenar as soluções
  solucoes = []

  # Função recursiva para colocar as rainhas no tabuleiro
  def colocar_rainhas(linha):
    # Se todas as rainhas foram colocadas, então encontramos uma solução
    if linha == n:
      solucoes.append([coluna for coluna in tabuleiro[0]])
      return

    # Para cada coluna na linha atual
    for coluna in range(n):
      # Se a rainha pode ser colocada na coluna atual
      if pode_colocar_rainha(linha, coluna, tabuleiro):
        # Coloca a rainha na coluna
        tabuleiro[linha][coluna] = coluna

        # Chama a função recursiva para a próxima linha
        colocar_rainhas(linha + 1)

        # Retira a rainha da coluna
        tabuleiro[linha][coluna] = -1

  # Chama a função recursiva para a primeira linha
  colocar_rainhas(0)

  return solucoes

# Função para verificar se uma rainha pode ser colocada em uma posição específica
def pode_colocar_rainha(linha, coluna, tabuleiro):
  # Verifica se a coluna está vazia
  for i in range(linha):
    if tabuleiro[i][coluna] != -1:
      return False

  # Verifica se a diagonal principal está vazia
  i, j = linha - 1, coluna - 1
  while i >= 0 and j >= 0:
    if tabuleiro[i][j] != -1:
      return False
    i -= 1
    j -= 1

  # Verifica se a diagonal secundária está vazia
  i, j = linha - 1, coluna + 1
  while i >= 0 and j < n:
    if tabuleiro[i][j] != -1:
      return False
    i -= 1
    j += 1

  return True

# Exemplo de uso
n = 8
solucoes = n_rainhas(n)

print(f"Número de soluções para {n} rainhas: {len(solucoes)}")
for solucao in solucoes:
  print(solucao)
