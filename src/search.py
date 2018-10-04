# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 74].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from game import Directions

    "get initial state"
    initialState = problem.getStartState()

    exploredList = []
    finalPath = []
    frontier = util.Stack()

    "node = cur_state, path, cost = 0 since we dont count now"
    node = (initialState, [], 0)
    frontier.push(node)

    while not frontier.isEmpty():
        curNode = frontier.pop()
        "check whether it is goal state"
        if problem.isGoalState(curNode[0]): return curNode[1]

        if curNode[0] not in exploredList:
            exploredList.append(curNode[0])
            for successor in problem.getSuccessors(curNode[0]):
                path = curNode[1]
                path = path + [successor[1]]
                finalPath = finalPath + [successor[1]]
                frontier.push((successor[0], path, 0))


    return finalPath


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    "*** YOUR CODE HERE ***"

    from game import Directions

    "get initial state"
    initialState = problem.getStartState()

    exploredList = []
    finalPath = []
    frontier = util.Queue()

    "node = cur_state, path, cost = 0 since we dont count now"
    node = (initialState, [], 0)
    frontier.push(node)

    while not frontier.isEmpty():
        curNode = frontier.pop()
        "check whether it is goal state"
        if problem.isGoalState(curNode[0]): return curNode[1]

        if curNode[0] not in exploredList:
            exploredList.append(curNode[0])
            for successor in problem.getSuccessors(curNode[0]):
                path = curNode[1]
                path = path + [successor[1]]
                finalPath = finalPath + [successor[1]]
                frontier.push((successor[0], path, 0))


    return finalPath

import heapq
def uniformCostSearch(problem):


    initialState = problem.getStartState()

    exploredList = []
    finalPath = []
    frontier = util.PriorityQueue()

    "node = cur_state, path, cost = 0 since we dont count now"
    node = (initialState, [], 0)
    frontier.push(node,0)

    while not frontier.isEmpty():
        NodeInfo = heapq.heappop(frontier.heap)
        curNode = NodeInfo[1]
        cost = NodeInfo[0]
        "check whether it is goal state"
        if problem.isGoalState(curNode[0]): return curNode[1]

        if curNode[0] not in exploredList:
            exploredList.append(curNode[0])
            for successor in problem.getSuccessors(curNode[0]):
                path = curNode[1]
                path = path + [successor[1]]
                finalPath = finalPath + [successor[1]]
                frontier.push((successor[0], path, cost+1),cost+1)


    return finalPath



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return util.manhattanDistance(state,problem.goal)


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    initialState = problem.getStartState()

    exploredList = []
    finalPath = []
    frontier = util.PriorityQueue()

    "node = cur_state, path, cost = 0 since we dont count now"
    node = (initialState, [], 0)
    frontier.push(node,0)

    while not frontier.isEmpty():
        NodeInfo = heapq.heappop(frontier.heap)
        curNode = NodeInfo[1]
        priority = NodeInfo[0]
        "check whether it is goal state"
        if problem.isGoalState(curNode[0]): return curNode[1]

        if curNode[0] not in exploredList:
            exploredList.append(curNode[0])
            for successor in problem.getSuccessors(curNode[0]):
                path = curNode[1]
                path = path + [successor[1]]
                finalPath = finalPath + [successor[1]]
                frontier.push((successor[0], path, curNode[2]+1),curNode[2]+1+nullHeuristic(curNode[0],problem))


    return finalPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
