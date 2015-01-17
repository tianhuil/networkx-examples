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


def plot_color_multigraph(G, graph_colors, n_rows, n_cols, node_size=100, fig_no=1):
  fig = plt.figure(fig_no)
  fig.clear()
  for k, (name, colors) in enumerate(graph_colors):
    plt.subplot(n_rows, n_cols, k + 1)
    plt.title(name, color='white')
    nx.draw_graphviz(G,  # this is expensive but at least it's consistent.
      node_color=colors,
      vmin=min(colors),
      vmax=max(colors),
      cmap=plt.get_cmap('cool'),
      alpha=.5,
      width=.3,
      edge_color="#FFFFFF",
      node_size=node_size
    )

  fig.set_facecolor("#000000")
  return fig

