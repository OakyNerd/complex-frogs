from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from visualizations import drawSearchTree


class MazeProblemSolvingAgentProDraw(MazeProblemSolvingAgentPro):
  def search(self, problem):
      seq, steps, allNodeColors= self.program(problem)
      solution=None
      #print(len(allNodeColors))
      #print(allNodeColors)
      if seq!= None:
        solution=self.actions_path(seq.path())
        print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
      return (solution,steps, allNodeColors)

  def work(self, percept):
        #allNodeColors=[]
        #nSteps=0
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            seq, steps, allNodeColors = self.search(problem)
            self.seq=seq if seq!= None else []
            #print(allNodeColors[steps-1])
            if len(self.seq)==0:
                return allNodeColors[steps-1]#None
             #drawSearchTree(self.dataGraph, allNodeColors[steps-1], steps)
        return allNodeColors[steps-1]




