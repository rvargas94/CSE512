# jug34.py
# Heidy Ramirez, Richard Vargas
# Homework2

import random
import copy


start = [0,0]  # 3-liter and 4-liter jugs are empty


GOAL = [0,2]   # 3-liter jug is empty 4-liter jug holds 2 liters



#The three functions: goal, evaluation, and successor
#
#
#
def jug_goal_fct(jugs,goal):
    return jugs == GOAL


def jug_eval_fct(jugs,goal):  
    score = 0
    
    if not goal == jugs:
            score += 1
    return score

def jug_successor_fct(jugs):
    succs =[]
    moves = [stateA(jugs), stateB(jugs), stateC(jugs),stateD(jugs),\
             stateE(jugs), stateF(jugs)]
    
    for x in moves:
        if not x == None:
            succs.append(x)
    return succs
#
#
#



#The next 6 states are the production rules!
#(fill, dump, pour) 

# 3L FILL
def stateA(jugs):
      newjugs = jugs[:]
      newjugs[0] = 3       # [3,y]
      return 
   
# 4L FILL
def stateB(jugs):
    newjugs = jugs[:]
    newjugs[1] = 4         # [x,4]
    return newjugs


# 3L DUMP
def stateC(jugs):
    newjugs = jugs[:]
    newjugs[0] = 0         # [0,y]
    return newjugs


# 4L DUMP
def stateD(jugs):
    newjugs = jugs[:]      # [x,0]
    newjugs[1] = 0
    return newjugs


#POUR TO FILL
def stateE(jugs):
    newjugs = jugs[:]
    x = newjugs[0]         # state description 
    y = newjugs[1]         # using two integers (x , y)

    if (0 < x+y >= 3 and y > 0):       # (3, y-(4-x))
        newjugs[0] = 3
        newjugs[1] = y-(4-x)

    
    
    if (0 < x+y >= 4 and y > 0):       # (x-(3-y),4)
        newjugs[0] = x-(3-y)
        newjugs[1] = 4

    return newjugs

#POUR ALL 
def stateF(jugs):
    newjugs = jugs[:]
    x = newjugs[0]     
    y = newjugs[1]

    if (0 < x+y <= 3 and y >= 0):     # (x+y,0)      
        newjugs[0] = x+y
        newjugs[1] = 0

    
    
    if (0 < x+y <= 4 and x >= 0):     # (0,x+y)
        newjugs[0] = 0
        newjugs[1] = x+y


    return newjugs

#PRINTS THE PATH

def jugs34_compact(jugs):
    print jugs


