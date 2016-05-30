from math import sqrt
import shortest_path_yen as ksp


class location:
	def __init__(self,x,y):
		self.x = x
		self.y = y



def find_linear_dist(start,end):
	return sqrt((start.x - end.x)**2 + (start.y - end.y)**2)

def find_actual_dist(start,end):
	return sqrt((start.x - end.x)**2 + (start.y - end.y)**2)

class work_graph:
	
	def __init__(self,work_loc):
		self.G = ksp.Graph()
		self.work_loc = work_loc
		self.work_id = self.G.add_node(work_loc)





	def add_node(self,location):
		#do we need to check if location already exists in graph?
		new_id = self.G.add_node(location)
		#always need distance straight to work (do this first so we know the first edge is always edge to work)
		self_dist_direct = find_actual_dist(location,self.work_loc)
		self.G.add_edge(new_id,self.work_id,self_dist_direct) 
		for n in range(1,len(self.G.nodes)-1): #don't include the node we just added or work
			candidate_dist_direct = self.G.nodes[n].children[0]['weight']

			self_to_candidate_dist = find_linear_dist(location,self.G.nodes[n].location)

			#increased distance is the distance to pick up minus distance without pick up
			self_dist_increase = (self_to_candidate_dist + candidate_dist_direct) - self_dist_direct 

			act_dist_found = False
			act_dist = 0
			#don't add if dist increase (price to be payed) is greater than driving direct for the passenger
			if(self_dist_increase < candidate_dist_direct):
				act_dist = find_actual_dist(location,self.G.nodes[n].location)
				self.G.add_edge(new_id,n,act_dist)
				act_dist_found = True

  			#check for adding the other way around
			candidate_dist_increase = (self_to_candidate_dist + self_dist_direct) - candidate_dist_direct
			if(candidate_dist_increase < self_dist_direct):
				if(act_dist_found):
					self.G.add_edge(n,new_id,act_dist)					
				else:
					self.G.add_edge(n,new_id,find_actual_dist(location,self.G.nodes[n].location))


