import networkx as nx
import matplotlib.pylab as plt

G=nx.dodecahedral_graph()
layouts = [
  ("draw_circular", nx.draw_circular),
  ("draw_random", nx.draw_random),
  ("draw_spectral", nx.draw_spectral),
  ("draw_spring", nx.draw_spring),
  ("draw_shell", nx.draw_shell),
  ("draw_graphviz", nx.draw_graphviz),
]

for k, (name, draw) in enumerate(layouts):
  plt.subplot(2, 3, k + 1)
  plt.title(name)
  draw(G, node_size=100)

plt.show()
