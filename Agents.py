from game import Agent
from game import Directions

class DumbAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    "Based on the current options, pick a random action to carry out."
    def getAction(self, state):
         "The agent receives a GameState (defined in pacman.py)."
         print("Location:", state.getPacmanPosition())
         print("Action available:", state.getLegalPacmanActions())
         import random
         return random.choice(state.getLegalPacmanActions())


class BetterRandomAgent(Agent):
    "Based on the current options, pick a random action to carry out."
    def getAction(self, state):
         "The agent receives a GameState (defined in pacman.py)."
         print("Location:", state.getPacmanPosition())
         print("Action available:", state.getLegalPacmanActions())
         actions = state.getLegalPacmanActions()
         actions.remove(Directions.STOP)
         import random
         return random.choice(actions)


class ReflexAgent(Agent):
    "If one of these actions would cause a food pellet to be eaten, it should choose that action. "
    "If none of the immediate actions lead to food, it should choose randomly from the possibilities (excluding 'Stop')."
    def getAction(self, state):

        legalActions = state.getLegalPacmanActions()
        if Directions.STOP in legalActions:
            legalActions.remove(Directions.STOP)

        successors = [(state.generateSuccessor(0, action).data.score, action) for action in legalActions]
        highestScore = max(successors)[0]

        bestActions = []
        for score, action in successors:
            if score == highestScore:
                bestActions.append(action)
                
        import random
        return random.choice(bestActions)

               

