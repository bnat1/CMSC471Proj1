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
		self.costs = {}
		self.open_list = deque()
		self.path = []
		#initialize visited and parent, and cost dictionary
		for key, value in self.graph.nodes.items():
			if key not in self.visited.items():
				self.visited[key] = False
				self.parents[key] = None
				self.costs[key] = float("inf")
			for item in value:
				if item['to_node'] not in self.visited:
					self.visited[item['to_node']] = False
					self.parents[item['to_node']] = None
					self.costs[item['to_node']] = float("inf")
		#start_node is visited 
		self.visited[self.graph.start_node] = True
		#no weight for start node
		self.costs[self.graph.start_node] = 0
		#add start node to queue
		self.open_list.appendleft(self.graph.start_node)
		
	def bfs(self):
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
		keep_going = True
		has_unvisited_child = False;
		while keep_going:
			#set current to last item on stack
			if len(self.open_list) != 0:
				current_node = self.open_list[-1]
				if debug:
					print ("current_node: ", current_node)
				#make sure node has neighbors before continuing
				#goal: check if neighbor
				if current_node in self.graph.nodes:
					#visit lowest unvisited child
					for neighbor in self.graph.nodes[current_node]:
						if debug:
							print("neighbor: ", neighbor)
						#only visit unvisited neighbors
						if not self.visited[neighbor['to_node']]:
							has_unvisited_child = True
							self.open_list.append(neighbor['to_node'])
							if debug:
								print("open: ", self.open_list)
							self.visited[neighbor['to_node']] = True
							self.parents[neighbor['to_node']] = current_node
							current_node = neighbor['to_node']
							if debug:
								print("visited: ", self.visited)
								print("parents: ", self.parents)
							if neighbor['to_node'] == self.graph.end_node:
								#found the end node
								keep_going = False
								self.found = True
							#break when there is at least one unvisited child
							break
						else:
							has_unvisited_child = False;
				else:
					has_unvisited_child = False;
				if not has_unvisited_child:
					self.open_list.pop()
			else:
				#ran out of nodes to visit
				keep_going = False
	#print path
	def ucs(self):
		current_node = self.graph.start_node
		#for current node, look at unvisied neibors, calcuate 
		#distance to this node + distance from this to neighbor
		keep_going = True
		while(keep_going):
			#check every neighbor of current_node
			if debug:
				print ("current node: ", current_node)
			self.visited[current_node] = True
			if debug:
				print ("visited: ", self.visited)
			#make sure current node has children before trying to visit them
			if current_node in self.graph.nodes:
				for neighbor in self.graph.nodes[current_node]:
					#if neighbor not visted yet:
					if not self.visited[neighbor['to_node']]:
						potential_distance = self.costs[current_node] + neighbor['edge_weight']
						if debug:
							print("looking at ", neighbor['to_node'])
							print("potential distance: ", potential_distance)
						#check if potential distance is better than tentative distance
						if potential_distance < self.costs[neighbor['to_node']]:
							#update cost, parent of neighbor
							self.costs[neighbor['to_node']] = potential_distance
							self.parents[neighbor['to_node']] = current_node
							if debug:
								print ("costs: ", self.costs)
								print ("parents: ", self.parents)
			#condition to be done with search
			if current_node == self.graph.end_node:
				if debug:
					print("found")
				self.found = True
				keep_going = False
			#next current node is the one with the smallest weight
			#visited is false and minimal cost, and has a parent
			unvisited_discovered_nodes = []
			candidate_lowest_costs = {}
			for key, value in self.visited.items():
				if not value and self.parents[key] != None:
					unvisited_discovered_nodes.append(key)
			if debug:
				print("unvisted discovered nodes: ", unvisited_discovered_nodes)
			#check if any unvisited left
			if len(unvisited_discovered_nodes) > 0:
				for node in unvisited_discovered_nodes:
					candidate_lowest_costs[node] = self.costs[node]
				#find minimum cost in dictionary
				#http://stackoverflow.com/questions/3282823/get-key-with-the-least-value-from-a-dictionary
				if debug:
					print ("candidate lowest costs: ",candidate_lowest_costs)
				current_node = min(candidate_lowest_costs, key=candidate_lowest_costs.get)
				if debug:
					print("lowest discovered unvisited node: %d, with value %d", current_node, self.costs[current_node])
			else:
				#not found, and no more nodes to visit
				keep_going = False


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
			#line isn't whitespace
			if line.strip() != '':
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