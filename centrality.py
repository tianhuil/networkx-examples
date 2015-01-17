import networkx as nx
import plot_multigraph
from matplotlib import pylab as plt

n = 80
p = 10. / n
G = nx.fast_gnp_random_graph(n, p, seed=42)

def to_list(dict_):
  return [dict_[k] for k in G.nodes()]

graph_colors = [
  ("degree", to_list(nx.degree_centrality(G))),
  ("betweenness", to_list(nx.betweenness_centrality(G))),
  ("load", to_list(nx.load_centrality(G))),
  ("eigenvector", to_list(nx.eigenvector_centrality_numpy(G))),
  ("closeness_centrality", to_list(nx.closeness_centrality(G))),
  ("current_flow_closeness", to_list(nx.current_flow_closeness_centrality(G))),
  ("current_flow_betweenness", to_list(nx.current_flow_betweenness_centrality(G))),
  ("katz", to_list(nx.katz_centrality_numpy(G))),
  ("communicability", to_list(nx.communicability_centrality(G))),
]

plot_multigraph.plot_color_multigraph(G, graph_colors, 3, 3, node_size=50)
plt.show()
