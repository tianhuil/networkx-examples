import networkx as nx
from plot_multigraph import plot_multigraph

n = 6
hypercube_n = 4
m = 6
r = 2
h = 3
dim = [2, 3]

graphs = [
  ("balanced_tree", nx.balanced_tree(r, h)),
  ("barbell_graph", nx.barbell_graph(n, m)),
  ("complete_graph", nx.complete_graph(n)),
  ("complete_bipartite_graph", nx.complete_bipartite_graph(n, m)),
  ("circular_ladder_graph", nx.circular_ladder_graph(n)),
  ("cycle_graph", nx.cycle_graph(n)),
  # ("dorogovtsev_goltsev_mendes_graph", nx.dorogovtsev_goltsev_mendes_graph(n)),
  ("empty_graph", nx.empty_graph(n)),
  ("grid_2d_graph", nx.grid_2d_graph(m, n)),
  ("grid_graph", nx.grid_graph(dim)),
  ("hypercube_graph", nx.hypercube_graph(hypercube_n)),
  ("ladder_graph", nx.ladder_graph(n)),
  ("lollipop_graph", nx.lollipop_graph(m, n)),
  # ("null_graph", nx.null_graph()),
  ("path_graph", nx.path_graph(n)),
  ("star_graph", nx.star_graph(n)),
  ("trivial_graph", nx.trivial_graph()),
  ("wheel_graph", nx.wheel_graph(n)),
]

plot_multigraph(graphs, 4, 4, node_size=50)
