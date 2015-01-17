import networkx as nx
from plot_multigraph import plot_multigraph

graphs = [
  ('karate_club_graph', nx.karate_club_graph()),
  ('davis_southern_women_graph', nx.davis_southern_women_graph()),
  ('florentine_families_graph', nx.florentine_families_graph()),
]

plot_multigraph(graphs, 2, 2, node_size=50)
