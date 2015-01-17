import networkx as nx
import matplotlib.pylab as plt

def plot_multigraph(graphs, n_rows, n_cols, node_size=100, fig_no=1):
  fig = plt.figure(fig_no)
  fig.clear()
  for k, (name, G) in enumerate(graphs):
    plt.subplot(n_rows, n_cols, k + 1)
    plt.title(name)
    nx.draw(G, node_size=node_size)

  plt.show()
