from math import ceil
#import networkx as nx
import shortest_path as sp

import graph

def path_weight(Graph,path):
	weight = 0
	for i in range(0,len(path)-1):
		#print('path_weight edges ',Graph.edges(data=True))
		#print('path weight indeces ',path[i],path[i+1])
		#weight += Graph.get_edge_data(path[i],path[i+1])['weight']
		# ind = Graph.nodes[path[i]].children.index(path[i+1])
		# weight += Graph.nodes[path[i]].children[ind]['weight']
		weight += Graph.get_edge(path[i],path[i+1])[2]
	return weight



def Shortest_Path(Graph,k,start,end):

	#paths = [nx.dijkstra_path(Graph,start,end,'weight')]
	paths = [sp.Shortest_Path(Graph,start,end)]
	if not paths[0]:
		print('no path to end')
		return
	B = []
	for i in range(1,k):
		#print('i ',i)
		for spurNode in paths[i-1][0:-1]: #don't include end node
			#print('spurNode ',spurNode)
			#print('spurNode ',spurNode, 'last path ',paths[i-1])
			spurNodeInd = paths[i-1].index(spurNode)
			rootPath = paths[i-1][0:spurNodeInd+1]

			edges_removed = []
			nodes_removed = []
			for p in paths:
				#print('p ',p)
				#print('spind ',spurNodeInd,' p ',p)
				if(len(p) >= len(rootPath)):
					if(rootPath == p[0:spurNodeInd+1]):
						#print('root path ',rootPath,' otherpath ',p[0:spurNodeInd+1])
						#edges = [(p(x),p(x+1)) for x in range(0,len(p)-1)]
						#Graph.remove_edges_from(edges)
						if(Graph.has_edge(p[spurNodeInd],p[spurNodeInd+1])): #if edge wasn't already removed
							edge_to_remove = Graph.get_edge(p[spurNodeInd],p[spurNodeInd+1])
							#print('edge to remove ',edge_to_remove)
							if(edges_removed.count(edge_to_remove) == 0):
								edges_removed.append(edge_to_remove)
							#print('edges removed temp1 ',edges_removed)

							#Graph.remove_edge(p[spurNodeInd],p[spurNodeInd+1]) #remove edge from spur that was on previous path
			#print(Graph.nodes())
			for n in rootPath[0:-1]: #all nodes in root path except spur node
				#print('n ',n)
				edges = Graph.edges()
				edges_to_remove = [x for x in edges if (x[0] == n or x[1] == n)]
				#print('edges ',edges_to_remove)
				if(edges_removed.count(edge_to_remove) == 0):
					edges_removed = edges_removed +  edges_to_remove
				#print('edges removed temp2 ',edges_removed)
				nodes_removed.append(n)
				#Graph.remove_node(n) #remove node, so that it isn't visited again, which would create a loop
			Graph.remove_edges_from(edges_removed)
			#Graph.remove_nodes_from(nodes_removed)

			#spurPath = nx.dijkstra_path(Graph,spurNode,end,'weight')
			spurPath = sp.Shortest_Path(Graph,spurNode,end)
			if not spurPath:
				continue #no path found
			#print('edges removed ',edges_removed,' nodes removed ',nodes_removed)
			#Graph.add_nodes_from(nodes_removed)
			Graph.add_edges_from(edges_removed)
			totalPath = rootPath[0:-1] + spurPath
			#print('totalPath, ',totalPath)
			#print('Edges: ',Graph.edges(data=True),' nodes ',Graph.nodes())

			totalPath_weight = (path_weight(Graph,totalPath),totalPath)
			if(B.count(totalPath_weight) == 0):
				B.append(totalPath_weight)


		if(not B):
			break;
		B.sort() #sort at the end because we do many additions for 1 min remove, so heap is not as useful
		#print('B ',B)
		paths.append(B.pop(0)[1])
	return paths







def make_graph(num_nodes,edges):
	G = graph.Graph()
	G.num_nodes = num_nodes
	G.num_edges = len(edges)
	for i in range(0,G.num_nodes):
		G.nodes.append(Node())
	for i in range(0,len(edges)):
		G.nodes[edges[i][0]].children.append({'end'    :edges[i][1],
		                                      'weight' :edges[i][2]})
	G.nodes[0].parent = -2 #node 1 is the only node that shouldn't have it's weight updated if it hasn't been visited, so mark it differently	
		
	return G

# def make_graph_from_networkx(nx_graph):
# 	G = Graph()
# 	G.num_nodes = len(nx_graph.nodes())
# 	edges = nx_graph.edges(data=True)
# 	G.num_edges = len(edges)
# 	for i in range(0,G.num_nodes):
# 		G.nodes.append(Node())
# 	for i in range(0,len(edges)):
# 		G.nodes[edges[i][0]].children.append({'end'    :edges[i][1],
# 		                                      'weight' :edges[i][2]['weight']})
# 	G.nodes[0].parent = -2 #node 1 is the only node that shouldn't have it's weight updated if it hasn't been visited, so mark it differently	
# 	return G







