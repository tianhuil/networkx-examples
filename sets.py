import networkx as nx
import plot_multigraph
from matplotlib import pylab as plt

n = 80
k = int(.2 * n)
p = 10. / n
G = nx.fast_gnp_random_graph(n, p, seed=42)

def set_to_list(set_, G):
  return [1. * (k in set_) for k in G.nodes()]

graph_colors = [
  ("center", set_to_list(nx.center(G), G)),
  ("periphery", set_to_list(nx.periphery(G), G)),
  ("k_core", set_to_list(nx.k_core(G), G)),
  ("k_shell", set_to_list(nx.k_shell(G), G)),
  ("k_crust", set_to_list(nx.k_crust(G), G)),
  ("k_corona", set_to_list(nx.k_corona(G, k), G)),
]

plot_multigraph.plot_color_multigraph(G, graph_colors, 2, 3, node_size=50)
plt.show()
