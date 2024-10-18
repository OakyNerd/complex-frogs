from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from mazeProblemSolvingAgentProDrawClass import MazeProblemSolvingAgentProDraw


def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

def ProblemSolvingMazeAgentBFSShow(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BestFirstSearchAgentProgramForShow())


def ProblemSolvingMazeAgentBREADTH_FS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BreadthFirstSearchGraph())
