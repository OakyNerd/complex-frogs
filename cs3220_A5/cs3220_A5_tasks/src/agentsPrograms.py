#How do we decide which node from the frontier to expand next?
from nodeClass import Node
from queue import PriorityQueue
from collections import deque

def BestFirstSearchAgentProgram(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):

      node = Node(problem.initial)
      #print(node)
      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))
      reached = {problem.initial:node}
      nodes_expanded = 0

      while frontier:
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))
        nodes_expanded +=1
        
        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                frontier.put((1,child))
                reached.update({child.state:child})
            
      return None

    return program

def A_StarSearchAgentProgram(f=None):
    
    def program(problem):
      print("problem: {}".format(problem))

      node = Node(problem.initial)
 
      frontier = PriorityQueue()
      h=node.path_cost+round(f(node.state, problem.goal),3)
      frontier.put((h,node))
      reached = {problem.initial:node}
      nodes_expanded = 0

      while frontier:
        print(frontier.queue)
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))
        nodes_expanded += 1

        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          print("Total nodes expanded: {}".format(nodes_expanded))
          print("Total cost: {}".format(problem.path_cost))
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                print("Child node path cost: {}".format(child.path_cost))
                h=child.path_cost+round(f(child.state, problem.goal),3)
                frontier.put((h,child))
                reached.update({child.state:child})
        print("Nodes expanded: {}".format(nodes_expanded))
      return None

    return program

def BestFirstSearchAgentProgramForShow(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
  def program(problem):
      #print(111)
      steps = 0
      allNodeColors = []
      nodeColors = {k : 'white' for k in problem.graph.nodes()}

      node = Node(problem.initial)
      nodeColors[node.state] = "yellow"
      steps += 1
      allNodeColors.append(dict(nodeColors))

      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))

      nodeColors[node.state] = "orange"
      steps += 1
      allNodeColors.append(dict(nodeColors))



      reached = {problem.initial:node}

      while not frontier.empty():
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))
        nodeColors[node.state] = "red"
        steps += 1
        allNodeColors.append(dict(nodeColors))
        #print(node)

        if problem.goal_test(node.state):
          nodeColors[node.state] = "green"
          steps += 1
          allNodeColors.append(dict(nodeColors))
          return (node,steps,allNodeColors)
          

        #reached.add(node.state)
        #print(node.expand(problem))
        for child in node.expand(problem):
            #print(child)
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                print("The child node {}.".format(child))
                frontier.put((1,child))
                nodeColors[child.state] = "orange"
                steps += 1
                allNodeColors.append(dict(nodeColors))

                reached.update({child.state:child})

        # modify the color of explored nodes to blue
        nodeColors[node.state] = "blue"
        steps += 1
        allNodeColors.append(dict(nodeColors))
      print("No solution...")
            
      return None,steps,allNodeColors

  return program


def BreadthFirstSearchGraph():
  def program(problem):
    node = Node(problem.initial)
    #early goal test
    if problem.goal_test(node.state):
      print("We have found our goal: {}".format (node.state))
      return node
    
    frontier = deque()#FIFO
    frontier.append(node)
    reached = set()
    reached.add(node.state)
    
    while frontier:
      print("Reached: {} ".format(reached))
      print("Frontier: {} ".format(frontier))
      node = frontier.popleft()#FIFO
      print("The node {} is extracted from frontier:".format(node.state))
      
      for child in node.expand(problem):
        print("The child node {}.".format(child))
        if problem.goal_test(child.state):
          print("We have found our goal: {}".format (child.state))
          return child

        if child.state not in reached:
          reached.add(child.state)
          frontier.append(child)
    return None

  return program


