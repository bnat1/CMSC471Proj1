#Nat Baylon
#CMSC 471, Max
#Project 1: BFS, DFS, UCS

#parse input
#read from file, build tree
#execute search
#print path, or empty list

import sys
from collections import deque
from operator import itemgetter

#graph deinition
class Graph:
	#constructor
	def __init__(self, start_node, end_node):
		self.start_node = start_node
		self.end_node = end_node

		#store nodes and edges
		self.nodes = {}
		##structure of graph##
		# nodes:{
		# 	parntnode#: [
		# 		{child_name: 0,
		#		 edge_weight: 0},
		# 		...
		# 	],
		# 	...
		# }

	#add nodes and verticies to graph
	def add_node(self, from_node, to_node, weight):
		from_node = int(from_node)
		temp_dict = {}
		temp_dict['child_node'] = int(to_node)
		temp_dict['edge_weight'] = float(weight)
		if from_node in self.nodes:
			self.nodes[from_node].append(temp_dict)
		else:
			self.nodes[from_node] = []
			self.nodes[from_node].append(temp_dict)
	
	#bfs search
	def bfs(self):
		print('bfs skeleton call')
		visited = {}
		parents = {}
		queue = 

	def dfs(self):
		print('dfs skeleton call')
	def ucs(self):
		print('ucs skeleton call')

	def print_path(self):
		print('print_path skeleton call')
	
	#for testing add
	def print_nodes(self):
		print(self.nodes)

	# sort children of each parent
	def sort_children(self):
		# https://wiki.python.org/moin/SortingListsOfDictionaries
		sort_on = "child_node"
		for k, v in self.nodes.items():
			self.nodes[k] = sorted(v, key=itemgetter('child_node'))

#check if input args is correct length
def validateInput(len):
	if len != 5:
		print('Usage: python Search.py input_file start_node end_node search')
		sys.exit(2)

#main
def main(argc, argv):

	#validate command line args
	validateInput(argc)

	#read command line args
	input_file = argv[1]
	start_node = int(argv[2])
	end_node = int(argv[3])
	search = argv[4]

	#initialize graph with start and end nodes
	graph = Graph(start_node, end_node)

	#add nodes to graph
	with open(input_file, 'r') as f:
		for line in f:
			graph.add_node(*line.split())
	#sort children nodes in graph
	graph.sort_children()

	#do the search
	if search == 'BFS':
		graph.bfs()
	elif search == 'DFS':
		graph.dfs()
	elif search == 'UCS':
		graph.ucs()

	#print path
	graph.print_path()



#call main if script
if __name__ == '__main__':
	main(len(sys.argv), sys.argv)