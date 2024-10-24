import math
from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from mazeProblemSolvingAgentProDrawClass import MazeProblemSolvingAgentProDraw

def ProblemSolvingMazeAgentAStar(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,A_StarSearchAgentProgram(math.dist))


def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

def ProblemSolvingMazeAgentBFSShow(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BestFirstSearchAgentProgramForShow())


def ProblemSolvingMazeAgentBREADTH_FS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BreadthFirstSearchGraph())
