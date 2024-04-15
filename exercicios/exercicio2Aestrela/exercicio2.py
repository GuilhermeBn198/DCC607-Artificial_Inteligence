# !pip install osmnx
import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox

#latitude e longitude da cidade/MAPA levando como base/centro o bloco 5.
latitude = 2.831977
longitude = -60.697621
raio = 3500 #(Quanto maior o raio, maior será o Mapa de Tráfego, em contra ponto a visualização fica pior)

#BAIXAR O GRAFO
G = ox.graph_from_point((latitude, longitude),dist=raio, network_type= 'drive')


#Plota o Mapa de Tráfego das ruas
ox.plot_graph(G)


# Origem = Casa / Destino = Bloco 5
origem = (2.8338856071557847, -60.66873152333758)
destino = (2.835027, -60.694897)

origem_node = ox.distance.nearest_nodes(G,origem[1], origem[0])
destino_node = ox.distance.nearest_nodes(G,destino[1], destino[0])

caminho = nx.astar_path(G,origem_node, destino_node, weight= 'length')

fig, ax = ox.plot_graph_route(G, caminho, route_linewidth=6, node_size=0, bgcolor= 'k')

plt.show()