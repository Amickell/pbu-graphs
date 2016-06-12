import networkx as nx
import shortest_path as sp
from random import randint

G = nx.dense_gnm_random_graph(10,40)
for (u,v) in G.edges():
	# G.edge[u][v]['weight'] = 20*random.random() #random weight between -10 and 10
	G.edge[u][v]['weight'] = randint(0,20) #random weight between -10 and 10
G = G.to_directed()	

nx_path = nx.dijkstra_path(G,0,9,'weight')

G2 = sp.make_graph_from_networkx(G)
my_path = sp.Shortest_Path(G2,0,9)




