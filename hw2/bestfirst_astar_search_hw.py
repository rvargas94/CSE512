import random
import time
import pickle
from jug34 import *

# import library for the jugs 



class Node:
  def __init__(self, state = None, path = [], depth = 0, evalue = None):
    self.thestate = state
    self.thepath = path
    self.thedepth = depth
    self.theeval = evalue

  def __eq__(self, other):
    return self.thestate == other.thestate   # equality by state only!


# parameterize the goal, successor and evaluation functions;

def BEST_FIRST_SEARCH_FCT(start,target,GOAL_FCT,SUCCESSOR_FCT,EVAL_FCT,\
                    COMPACT_PRINT = None):

  if COMPACT_PRINT == None:
      def myprint (x): print x
      COMPACT_PRINT = myprint

  open = [Node(start,[start],0,EVAL_FCT(start,target))]
  closed = []
  steps = 0  ######### report these as effort!!!
  while open != []:
    nxt = open[0]
    open = open[1:]
    
    nxtstate = nxt.thestate  
    nxtpath = nxt.thepath     
    nxteval = nxt.theeval     
  
    if GOAL_FCT(nxtstate,target): 
      print "GOAL FOUND:"
      #print "state: %s" % nxtstate
      print "State:   ",
      COMPACT_PRINT(nxtstate)
      print "PathL:  %d" % len(nxtpath)
      print "Steps:  %d\n" % steps
      return (nxtstate, nxtpath)

    if nxt in closed:
      continue
    closed.append(nxt)

    succ = SUCCESSOR_FCT(nxtstate) # successors are states, NOT Nodes (yet)
    random.shuffle(succ)

    for x in succ:
      xcost = EVAL_FCT(x,target)
      newnode = Node(x, addpath(nxtpath,x),0,\
                     EVAL_FCT(x,target)) # 0 depth bec don't care

      #check whether newnode is already on open or closed with
      #shorter path; if so, do not bother to put open;
      keeper = True
      for c in closed:
        if newnode.thestate == c.thestate and\
           len(newnode.thepath) >= len(c.thepath):
          keeper = False
          break

        if not keeper:
          continue
      
      for op in open:
        if newnode.thestate == op.thestate and\
           len(newnode.thepath) >= len(op.thepath):
          keeper = False
          break

      if keeper:
          open.append(newnode)

      open.sort(lambda x,y: CostCmp(x,y))  # NOTICE SORTING
      steps += 1
  return None

def ASTAR_SEARCH_FCT(start,target,GOAL_FCT,SUCCESSOR_FCT,EVAL_FCT,\
                    COMPACT_PRINT = None):

  if COMPACT_PRINT == None:
      def myprint (x): print x
      COMPACT_PRINT = myprint

  open = [Node(start,[start],0,EVAL_FCT(start,target))]
  closed = []
  steps = 0
  while open != []:
    nxt = open[0]
    open = open[1:]
    
    nxtstate = nxt.thestate  
    nxtpath = nxt.thepath
    nxteval = nxt.theeval
    nxtdpth = nxt.thedepth
    
    if GOAL_FCT(nxtstate,target): 
      print "GOAL FOUND:"
      #print "state: %s" % nxtstate
      print "State:    ",
      COMPACT_PRINT(nxtstate)
      print "PathL:  %d" % len(nxtpath)
      print "Steps:  %d\n" % steps
      return (nxtstate, nxtpath)
    

    
    if nxt in closed:
      continue
    closed.append(nxt)  
    
    succ = SUCCESSOR_FCT(nxtstate) 
    random.shuffle(succ)
    
    for x in succ:
        xcost = EVAL_FCT(x,target)  
        newnode = Node(x,addpath(nxtpath,x),nxtdpth+1,xcost+nxtdpth+1)

        #check whether newstate[0] (or, x) is already on open or closed with
        #shorter path; if so, do not bother to put open;
        keeper = True
        for c in closed:
          if newnode.thestate == c.thestate and\
             len(newnode.thepath) >= len(c.thepath):
            keeper = False
            break
        if not keeper:
          continue
        
        for op in open:
          if newnode.thestate == op.thestate and\
             len(newnode.thepath) >= len(op.thepath):
            keeper = False
            break

        if keeper:
            open.append(newnode)

    open.sort(lambda x,y: CostCmp(x,y))  # NOTICE SORTING
    steps += 1
  return None


# utility function 
def addpath(path,x):
  newpath = path[:]  # NOTICE: a copy is made!
  newpath.append(x)
  return newpath

 # x,y are lists that are compared by
# magnitude of their third elements;
# x of type Node 
# CostCmp compare costs, to allow sortig of triples by cost
def CostCmp (x,y):
  if x.theeval < y.theeval:
    return -1
  elif x.theeval == y.theeval:
    return 0
  else:
    return 1

# map puzz8 representation of puzzle state to
# Tiles1to8_Frame object; allows graphics simulation
# of path

def make_1to8_init_list(jugs):
  initlst = []
  for x in range(1,4):
    for y in range(1,4):
      if jugs[(x,y)] == 'B':
        initlst.append(0)
      else:
        initlst.append(jugs[(x,y)])
  return initlst


if __name__ == '__main__':

  random.seed()

  print "\nBest-first search in jug domains:"
 # show_jug(start)
  for i in range(5):
    BESTFIRST_SOLN =\
                   BEST_FIRST_SEARCH_FCT(start, GOAL, jug_goal_fct,\
                                         jug_successor_fct,\
                                         jug_eval_fct, )

  print "\nA* search in jug domains:"
 # show_jug(start)
  for i in range(5):
    ASTAR_SOLN =\
               ASTAR_SEARCH_FCT(start, GOAL, jug_goal_fct,\
                                jug_successor_fct,\
                                jug_eval_fct,)

  path1 = BESTFIRST_SOLN[1]
  path2 = ASTAR_SOLN[1]

  topickle = open("bestfirst_path.pickle", "wb")
  pickle.dump(path1, topickle)
  topickle.close()
  
  topickle = open("astar_path.pickle", "wb")
  pickle.dump(path2,topickle)
  topickle.close()
  
  print "\nA path from BEST-FIRST SEARCH:\n"
  for x in path1:
    jugs34_compact(x)

  print "\nA path from ASTAR SEARCH:\n"
  for x in path2:
    jugs34_compact(x)

    

 


  

