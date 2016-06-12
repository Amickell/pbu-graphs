from math import floor
class heap:
	def __init__(self,d):
		self.h = [] #array of nodes
		self.d = d #how many children can a node have

	def push(self,v):
		self.h.append(v) #add new node to the next leaf
		self.sift_up(len(self.h)-1)#get the new node in the right place

	def pop(self):		
		if len(self.h) > 1:   #if there is more than 1 node
			return self.delete(0)  #delete the root
		elif len(self.h) == 1:   #if there is only one node, just return that node
			to_return = self.h[0]
			self.h = []
			return to_return
		else: #this will happen if heap is empty
			return []
			

	def delete(self,index):     
		if(index != len(self.h)-1):   #if the node to delete isn't the last leaf
			temp = self.h[index]  #remove the index to be deleted, and replace it with the last leaf
			last_val = self.h.pop()
			self.h[index] = last_val
			self.sift_down(index)   #get the moved node in the right place
		else:
			temp = self.h.pop()  #if the node to delete is the last node, just remove it
		return temp


	def sift_up(self,index):
		parent_index = floor((index-1)/self.d) #nodes are just in order (i.e. node 0 is at 0, its children are at 1 through d, node 1's children are at d+1 through 2d etc.)
		while(self.h[parent_index] > self.h[index]):  #while the node has a parent greater than itself, switch it with its parent
			self.h[index],self.h[parent_index] = self.h[parent_index],self.h[index]
			index = parent_index
			if(index != 0): #if the node is not at the root
				parent_index = floor((index-1)/self.d)
			else: #if the node is at the root, then set it to its own parent, this will end the while loop
				parent_index = index

	def sift_down(self,index):
		children = self.h[self.d*index + 1:self.d*index + self.d+1] 
		if children: #if children is not empty (node is not a leaf)
			minchild = min(children) 
			while self.h[index] > minchild: #while the node is bigger than one or more children, switch the min child with that node
				min_child_ind = self.d*index + children.index(min(children))+1
				self.h[min_child_ind],self.h[index] = self.h[index],self.h[min_child_ind] 
				index = min_child_ind
				children = self.h[self.d*index + 1:self.d*index + self.d+1]
				if children:
					minchild = min(children)
				else:
					break






#def heappush(h,d):


# h = heap(4)
# h.push(15)
# print(h.h)
# h.push(10)
# print(h.h)
# h.push(9)
# print(h.h)
# h.push(8)
# print(h.h)
# h.push(7)
# print(h.h)
# h.push(4)
# print(h.h)
# h.push(2)
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)
# print(h.pop())
# print(h.h)

