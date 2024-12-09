from mazeProblemSolvingAgentClass import MazeProblemSolvingAgent
import collections


class MazeProblemSolvingAgentPro(MazeProblemSolvingAgent):
  def __init__(self, initial_state=None, dataGraph=None, goal=None, program=None):
    super().__init__(initial_state,dataGraph,goal)

    if program is None or not isinstance(program, collections.abc.Callable):
      print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

      def program(percept):
        return eval(input('Percept={}; action? '.format(percept)))

    self.program = program

  def search(self, problem):
    seq = self.program(problem)
    print(seq)
    solution=self.actions_path(seq.path()) if seq else None
    print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
    if seq is None:
      return solution
    else:
      return solution, seq.path()

  
  def actions_path(self, p):
    acts=[]
    for n in p:
      acts.append(n.action)
    return acts[1:]

  def run(self):
    print("goal list:", self.goal)
    path_to_goal=[]
    if isinstance(self.goal, list) and len(self.goal)>1:
      percept=self.state
      while len(self.goal)>0:
        current_goal=self.goal[0]
        print("current percept:", percept)
        print("current goal:", current_goal)
        """Formulate a goal and problem, then search for a sequence of actions to solve it."""
        #4-phase problem-solving process
        self.state = self.update_state(self.state, percept)
        goal = current_goal
        problem = self.formulate_problem(self.state, goal)
        self.seq.append (self.search(problem)[0])
        path_to_goal.append(self.search(problem)[1])
        percept=current_goal
        self.goal.remove(goal)
        print("goal list:", self.goal)
      if not self.seq:
                return None
      return self.seq, path_to_goal
    else:
      return super().__call__(self.state)