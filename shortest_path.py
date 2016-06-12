
from heap import heap
from math import ceil
import graph
def get_path(Graph,start,end):
	path = []
	current_node = end
	path.append(end)
	while current_node != start:
		current_node = Graph.nodes[current_node].parent
		if(current_node < 0):
			print("Node without parent in get_path ",current_node)
			return []
		path.append(current_node)
	path.reverse()
	return path


def Shortest_Path(Graph,start,end):

 	for i in Graph.nodes:
 		i.distance = 0
 		i.parent = -1;
 	
 	tovisit = heap(ceil(2+Graph.num_nodes/Graph.num_edges)) #create d-heap where d is ceil(2+m/n)
 	tovisit.push((0,start)) #push a tuple with node label and node number (node label first to sort heap by this)
 	while(tovisit.h): 
 		visit_node = tovisit.pop() #get the minimum cost neighbor
 		visit_node_id = visit_node[1] 
 		#print('visiting: ',visit_node_id)
 		visit_node_label = visit_node[0]

 		for i in range(0,len(Graph.nodes[visit_node_id].children['end'])):  #check all children even if they have already been visited
 			neighbors = Graph.nodes[visit_node_id].children
 			if(Graph.nodes[neighbors['end'][i]].distance > visit_node_label + neighbors['weight'][i] or Graph.nodes[neighbors['end'][i]].parent == -1): # update if the label from this node is less or if the node hasn't been visited
 				#print('count of ',i['end'],'is ',[x[1] for x in tovisit.h].count(i['end']))

 				if([x[1] for x in tovisit.h].count(neighbors['end'][i]) != 0):	#if node is already in heap, remove it
 					index = [x[1] for x in tovisit.h].index(neighbors['end'][i])
 					tovisit.delete(index)

 				Graph.nodes[neighbors['end'][i]].parent = visit_node_id  #update neighbor
 				Graph.nodes[neighbors['end'][i]].distance = visit_node_label + neighbors['weight'][i]
 				#print('adding',i['end'],'with distance',Graph.nodes[i['end']].distance)
 				tovisit.push((Graph.nodes[neighbors['end'][i]].distance,neighbors['end'][i])) #put node on heap
 	return get_path(Graph,start,end)



# def make_graph(num_nodes,edges):
# 	G = graph.Graph()
# 	G.num_nodes = num_nodes
# 	G.num_edges = len(edges)
# 	for i in range(0,G.num_nodes):
# 		G.nodes.append(graph.Node())
# 	for i in range(0,len(edges)):
# 		G.nodes[edges[i][0]].children.append({'end'    :edges[i][1],
# 		                                      'weight' :edges[i][2]})
# 	G.nodes[0].parent = -2 #node 1 is the only node that shouldn't have it's weight updated if it hasn't been visited, so mark it differently	
		
# 	return G

def make_graph_from_networkx(nx_graph):
	G = graph.Graph()
	G.num_nodes = len(nx_graph.nodes())
	edges = nx_graph.edges(data=True)
	G.num_edges = len(edges)
	for i in range(0,G.num_nodes):
		G.nodes.append(graph.Node())
	for i in range(0,len(edges)):
		G.nodes[edges[i][0]].children['end'].append(edges[i][1])
		G.nodes[edges[i][0]].children['weight'].append(edges[i][2]['weight'])
	G.nodes[0].parent = -2 #node 1 is the only node that shouldn't have it's weight updated if it hasn't been visited, so mark it differently	
	return G







