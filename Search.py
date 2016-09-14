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

debug = False
#graph deinition
class Graph:
	#constructor
	def __init__(self, start_node, end_node):
		self.start_node = start_node
		self.end_node = end_node

		#store nodes and edges
		self.nodes = {}
		self.path = []
		##structure of graph##
		# nodes:{
		# 	parntnode#: [
		# 		{to_node: 0,
		#		 edge_weight: 0},
		# 		...
		# 	],
		# 	...
		# }

	#add nodes and verticies to graph
	def add_node(self, from_node, to_node, weight):
		from_node = int(from_node)
		temp_dict = {}
		temp_dict['to_node'] = int(to_node)
		temp_dict['edge_weight'] = float(weight)
		if from_node in self.nodes:
			self.nodes[from_node].append(temp_dict)
		else:
			self.nodes[from_node] = []
			self.nodes[from_node].append(temp_dict)
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
	def sort_neighbors(self):
		# https://wiki.python.org/moin/SortingListsOfDictionaries
		sort_on = "to_node"
		for k, v in self.nodes.items():
			self.nodes[k] = sorted(v, key=itemgetter('to_node'))

#bfs search
class Search:
	def __init__(self, graph):
		self.graph = graph
		self.found = False		
		self.visited = {}
		self.parents = {}
		self.open_list = deque()
		self.path = []
		#initialize visited and parent dictionary
		for key, value in self.graph.nodes.items():
			if key not in self.visited.items():
				self.visited[key] = False
				self.parents[key] = None
			for item in value:
				if item['to_node'] not in self.visited:
					self.visited[item['to_node']] = False
					self.parents[item['to_node']] = None
		#add start node to queue
		self.open_list.appendleft(self.graph.start_node)
		
	def bfs(self):
		self.visited[self.graph.start_node] = True
		keep_going = True
		while keep_going:
			if len(self.open_list) != 0:
				#look at beginning of queue
				current_node = self.open_list[0]
				if debug:
					print ("current_node: ", current_node)
				#make sure node has children before referencing its children
				if current_node in self.graph.nodes:
					for neighbor in self.graph.nodes[current_node]:
						if debug:
							print("neighbor: ", neighbor)
						#only visit unvisited neighbors
						if not self.visited[neighbor['to_node']]:
							self.open_list.append(neighbor['to_node'])
							if debug:
								print("open: ", self.open_list)
							self.visited[neighbor['to_node']] = True
							self.parents[neighbor['to_node']] = current_node
							if debug:
								print("visited: ", self.visited)
								print("parents: ", self.parents)
							if neighbor['to_node'] == self.graph.end_node:
								#found the end node
								keep_going = False
								self.found = True
				self.open_list.popleft()
			else:
				#ran out of nodes to visit
				keep_going = False
	def dfs(self):
		print("dfs skeleton")
	#print path
	def ucs(self):
		print("ucs skeleton")
	def print_path(self):
		current_node = self.graph.end_node
		if self.found:
			while(current_node != self.graph.start_node):
				self.path.append(current_node)
				current_node = self.parents[current_node]
			self.path.append(self.graph.start_node)
			self.path.reverse()
		print(self.path)
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
	search_method = argv[4]

	#initialize graph with start and end nodes
	graph = Graph(start_node, end_node)
	#add nodes to graph
	with open(input_file, 'r') as f:
		for line in f:
			graph.add_node(*line.split())
	
	#sort children nodes in graph
	graph.sort_neighbors()

	#create search object
	search = Search(graph)

	#do the search
	if search_method == 'BFS':
		search.bfs()
	elif search_method == 'DFS':
		search.dfs()
	else:
		search.ucs()

	#print path to node
	search.print_path()
#call main if script
if __name__ == '__main__':
	main(len(sys.argv), sys.argv)