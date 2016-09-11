#Nat Baylon
#CMSC 471, Max
#Project 1: BFS, DFS, UCS

#parse input
#read from file, build tree
#execute search
#print path, or empty list

import sys
from collections import deque

#graph deinition
class Graph:
	def __init__(self, start_node, end_node):
		self.start_node = start_node
		self.end_node = end_node

		#store nodes and edges
		self.nodes = {}
		
		#keep track of parent in path?
		self.parent_dict = {}

		#notes on deques
		#https://docs.python.org/2/tutorial/datastructures.html
		#use popleft() for queues and popright() for stacks
		self.bfs_queue = deque() 
		self.dfs_stack = deque()

	#add nodes and verticies to graph
	def add_node(self, from_node, to_node, weight):
		#check if key exists in data
		temp_dict = {}
		temp_dict[to_node] = weight
		if from_node in self.nodes:
			self.nodes[from_node].append(temp_dict)
		else:
			self.nodes[from_node] = []
			self.nodes[from_node].append(temp_dict)
	
	def bfs():
		print('bfs skeleton call')
	def dfs():
		print('dfs skeleton call')
	def ucs():
		print('ucs skeleton call')

	def print_path(self):
		print('print_path skeleton call')
	
	#for testing add
	def print_nodes(self):
		print(self.nodes)

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
	# graph.add_node(1,2,3)
	# graph.add_node(2,3,4)
	# graph.add_node(1,3,4)
	graph.print_nodes()

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