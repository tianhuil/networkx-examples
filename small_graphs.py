import networkx as nx
from plot_multigraph import plot_multigraph

graphs = [
  ("bull", nx.bull_graph()),
  ("chvatal", nx.chvatal_graph()),
  ("cubical", nx.cubical_graph()),
  ("desargues", nx.desargues_graph()),
  ("diamond", nx.diamond_graph()),
  ("dodecahedral", nx.dodecahedral_graph()),
  ("frucht", nx.frucht_graph()),
  ("heawood", nx.heawood_graph()),
  ("house", nx.house_graph()),
  ("house_x", nx.house_x_graph()),
  ("icosahedral", nx.icosahedral_graph()),
  ("krackhardt_kite", nx.krackhardt_kite_graph()),
  ("moebius_kantor", nx.moebius_kantor_graph()),
  ("octahedral", nx.octahedral_graph()),
  ("pappus", nx.pappus_graph()),
  ("petersen", nx.petersen_graph()),
  ("sedgewick_maze", nx.sedgewick_maze_graph()),
  ("tetrahedral", nx.tetrahedral_graph()),
  ("truncated_cube", nx.truncated_cube_graph()),
  ("truncated_tetrahedron", nx.truncated_tetrahedron_graph()),
]

plot_multigraph(graphs, 4, 5, node_size=50)
