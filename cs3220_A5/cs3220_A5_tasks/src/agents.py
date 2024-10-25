import math
from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
#from mazeProblemSolvingAgentProDrawClass import MazeProblemSolvingAgentProDraw
from manhattanFunction import manhattan

def ProblemSolvingMazeAgentAStar(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,A_StarSearchAgentProgram(math.dist))

def ProblemSolvingMazeAgentAStar2(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,A_StarSearchAgentProgram(manhattan))


def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

# def ProblemSolvingMazeAgentBFSShow(initState,WorldGraph,goalState):
#     return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BestFirstSearchAgentProgramForShow())


def ProblemSolvingMazeAgentBREADTH_FS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BreadthFirstSearchGraph())
