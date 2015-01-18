import networkx as nx
import plot_multigraph
from matplotlib import pylab as plt

n = 80
p = 10. / n
G = nx.fast_gnp_random_graph(n, p, seed=42)

def to_list(dict_):
  return [dict_[k] for k in G.nodes()]

graph_colors = [
  ("eccentricity", to_list(nx.eccentricity(G))),
  ("clustering", to_list(nx.clustering(G))),
  ("square_clustering", to_list(nx.square_clustering(G))),
]

fig = plot_multigraph.plot_color_multigraph(G, graph_colors, 2, 2, node_size=50)
plt.savefig('graphs/distance.png', facecolor=fig.get_facecolor())
