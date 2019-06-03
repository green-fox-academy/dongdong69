import networkx as nx
import matplotlib.pyplot as plt 
G = nx.random_graphs.barabasi_albert_graph(100,1)
nx.draw(G)
#plt.savefig("ba.png")
plt.show()