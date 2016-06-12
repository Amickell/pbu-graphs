
import pbu_graph as pbug
import shortest_path_yen as ksp
from random import randint
work_loc = pbug.location(0,0)

g = pbug.work_graph(work_loc)

g.add_node(pbug.location(10,10))

g.add_node(pbug.location(1,1))

g.add_node(pbug.location(1,2))

g.add_node(pbug.location(2,1))

g.add_node(pbug.location(2,2))


# for i in range(1,10):
# 	g.add_node(pbug.location(randint(0,20),randint(0,20)))


p = ksp.Shortest_Path(g.G,5,1,0)



