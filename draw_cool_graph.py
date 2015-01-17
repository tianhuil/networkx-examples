import networkx as nx
import matplotlib.pylab as plt

def draw_cool_graph(G, fig_no=1, node_size=100):
  colors = [deg for _, deg in G.degree_iter()]
  fig = plt.figure(fig_no)
  fig.clear()
  nx.draw(G,
    node_color=colors,
    vmin=min(colors),
    vmax=max(colors),
    cmap=plt.get_cmap('cool'),
    node_size=node_size,
    alpha=.5,
    edge_color="#FFFFFF"
  )
  fig.set_facecolor("#000000")
  return fig

if __name__ == '__main__':
  n = 100
  p = 10. / n
  G = nx.fast_gnp_random_graph(n, p)
  fig = draw_cool_graph(G, node_size=20)
  plt.savefig('graphs/cool_graph.png', facecolor=fig.get_facecolor())
