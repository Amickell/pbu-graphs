

class Node:
	def __init__(self):
		self.location = 0
		self.children = {'end':[],
		                 'weight':[]}
		self.distance = 0
		self.parent = -1 #-1 means not visited


class Graph:
	def __init__(self):
		self.nodes = []
		self.num_nodes = 0
		self.num_edges = 0
	def add_node(self,location):
		self.nodes.append(Node())
		self.num_nodes += 1
		self.nodes[-1].location = location
		return (self.num_nodes - 1) #returns node id that was added
	def add_edge(self,node,end,weight):
		self.num_edges += 1
		# self.nodes[node].children.append({'end'      : end,
		# 	                              'weight'   : weight})
		self.nodes[node].children['end'].append(end)
		self.nodes[node].children['weight'].append(weight)
	def has_edge(self,start,end):
		if self.nodes[start].children['end'].count(end) != 0:
			return True
		else:
			return False
	def get_edge(self,start,end):
		if(self.nodes[start].children['end'].count(end) == 0):
			print('edge not found')
			return []
		else:
			ind = self.nodes[start].children['end'].index(end)
			return [start,end,self.nodes[start].children['weight'][ind]]
	def edges(self):
		edges = []
		for i in range(0,self.num_nodes):
			for j in range(0,len(self.nodes[i].children['end'])):
				edges.append([i,self.nodes[i].children['end'][j],self.nodes[i].children['weight'][j]])				
		return edges
	def remove_edges_from(self,edges_to_remove):
		for i in edges_to_remove:
			self.nodes[i[0]].children['end'].remove(i[1])
			self.nodes[i[0]].children['weight'].remove(i[2])

	def add_edges_from(self,edges_to_add):
		for i in edges_to_add:
			self.nodes[i[0]].children['end'].append(i[1])
			self.nodes[i[0]].children['weight'].append(i[2])