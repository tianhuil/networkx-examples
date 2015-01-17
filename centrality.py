import networkx as nx
from networkx import algorithms
import plot_multigraph
from matplotlib import pylab as plt

n = 80
p = 10. / n
G = nx.fast_gnp_random_graph(n, p, seed=42)

def to_list(dict_):
  return [dict_[k] for k in G.nodes()]

graph_colors = [
  ("degree", to_list(algorithms.degree_centrality(G))),
  ("betweenness", to_list(algorithms.betweenness_centrality(G))),
  ("load", to_list(algorithms.load_centrality(G))),
  ("eigenvector", to_list(algorithms.eigenvector_centrality(G))),
]

plot_multigraph.plot_color_multigraph(G, graph_colors, 2, 2, node_size=50)
plt.show()
