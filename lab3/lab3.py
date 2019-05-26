import random

#directed, acyclic graph of "nodes"
# example from Poole et.al. "Computational Intelligence",
# Oxford Univ Press,1998,pp. 117, 121
GRAPH = {'o103':['o109','ts','l2d3'],
		 'o109':['o111','o119'],
		 'ts':['mail'],
		 'o111':[],
		 'mail':[],
		 'o119':['store','o123'],
		 'store':[],
		 'o123':['o125','r123'],
		 'o125':[],
		 'r123':[],
		 'l2d3':['l2d1','l2d4'],
		 'l2d1':['l3d2','l2d2'],
		 'l2d4':['o109'],
		 'l2d2':['l2d4'],
		 'l3d2':['l3d3','l3d1'],
 		 'l3d3':[],
 		 'l3d1':['l3d3']}
COST = {('o103','ts'):8, ('o103','o109'):12, ('o103','l2d3'):4,\
		('ts','mail'):6,\
		('o109','o111'):4, ('o109','o119'):16,\
		('o119','store'):7, ('o119','o123'):9,\
		('o123','r123'):4, ('o123','o125'):4,\
		('l2d1','l3d2'):3, ('l2d1','l2d2'):6,\
		('l2d2','l2d4'):3, ('l2d3','l2d1'):4,\
		('l2d3','l2d4'):7, ('l2d4','o109'):7,\
		('l3d2','l3d3'):6, ('l3d2','l3d1'):4,\
		('l3d1','l3d3'):8}
		
#traversing and printing nodes in depth-first order

def dfs_traverse(start):
	open = [start]
	closed = []
	while open != []:
		nxt = open[0]
		open = open[1:]
		
		if nxt in closed:
			continue
		
		closed.append(nxt)
		print "nxt from open: %s" % nxt
		succ = GRAPH[nxt]
		random.shuffle(succ) #WHY DO DIS
		
		for x in succ:
			if not x in closed and not x in open:
				open = [x] + open
			
	return closed
	
#traversing and printing in breadth-first order

def bfs_traverse(start):
	open = [start]
	closed = []
	while open != []:
		nxt = open[0]
		open = open[1:]
		
		if nxt in closed:
			continue
		
		closed.append(nxt)
		print "nxt from open: %s" % nxt
		succ = GRAPH[nxt]
		random.shuffle(succ)
		for x in succ:
			if not x in closed and not x in open:
				open.append
	return closed
	
#SEARCHING connection from start to goal in dfs;
#returns goal when found, None otherwise;
#does NOT computer the "path" between start and goal;

def dfs_search(start,goal):
	open = [start]
	closed = []
	steps = 0
	while open != []:
		nxt = open[0]
		open = open[1:]
		
		#return when GOAL FOUND!
		if nxt == goal:
			return goal,steps
			
		if nxt in closed:
			continue
			
		print "nxt from open: %s" % nxt
		steps += 1
		closed.append(nxt)
		succ = GRAPH[nxt]
		random.shuffle(succ)
		for x in succ:
			if not x in closed and not x in open:
				open = [x] + open
		
	return None,steps
	
#SEARCH from start to goal in bfs;

def bfs_search(start,goal):
	open = [start]
	closed = []
	steps = 0
	while  open != []:
		nxt = open[0]
		open = open[1:]
		
		if nxt == goal:
			return goal,steps
		
		if nxt in closed:
			continue
		
		print "nxt from open: %s" % nxt
		steps += 1
		closed.append(nxt)
		succ=GRAPH[nxt]
		random.shuffle(succ)
		for x in succ:
			if not x in closed and not x in open:
				open.append(x)
	return None, steps
	
# searching with computing of PATH
# from start to goal; dfs;

def dfs_search_path(start,goal):
	open = [[start,[start]]]
	closed = []
	steps = 0
	while open != []:
		nxt = open[0]
		open = open[1:]
		nxtnode = nxt[0]
		nxtpath = nxt[1]
		
		if nxtnode == goal:
			return nxtpath, steps, len(closed)
		
		if nxt in closed:
			continue
		
		closed.append(nxtnode)
		succ = GRAPH[nxtnode]
		random.shuffle(succ)
		for x in succ:
			if not x in closed:
				open = [[x,addpath(nxtpath,x)]] + open
		steps += 1
	return None,steps
	
#searching and computing PATH in bfs;

#utility function
def addpath(path,x):
	newpath = path[:] #notice a copy is made!
	newpath.append(x)
	return newpath

#def bfs_search_path(start,goal):

#finding a path bgy pursing "best" first;

def best_first_search_path(start,goal):
	open = [[start,[start],0]]
	closed = []
	steps = 0
	while open != []:
		nxt = open[0]
		open = open[1:]
		
		nxtnode = nxt[0]
		nxtnode = nxt[1]
		nxtnode = nxt[2]
		
		if nxtnode == goal:
			return nxtpath,steps,len(closed)
			
		if nxt in closed:
			continue
			
		closed.append(nxtnode)
		succ = GRAPH[nxtnode]
		
		for x in succ:
			if not x in closed:
				xcost = COST[(nxtnode,x)]
				open.append([x,addpath(nxtpath,x),nxtcost+xcost])
		open.sort(lambda x,y: CostCmp(x,y)) #notice sorting
		steps += 1
	return None

#x,y are lists that are compared by magnitude of their third #
#elements; x of type [node,path,cost];
#CostCmp compare costs, to allow sorting of triples by cost

def CostCmp(x,y):
	if x[2] < y[2]:
		return -1
	elif x[2] == y[2]:
		return 0
	else:
		return 1
	
#FOR LATER...
#goal, successor and evaluation functions for best-first search
#in robot domain (above)

def rob_goal(node,target):
	return node == target
	
def rob_succ(node):
	return GRAPH[node]
	
def rob_cost(node,prevnode,target = None):
	return COST[(prevnode,node)]

