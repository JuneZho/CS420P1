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
            return Directions.STO

class RandomAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
         "The agent receives a GameState (defined in pacman.py)."
         print("Location:", state.getPacmanPosition())
         print("Action available:", state.getLegalPacmanActions())
         import random
         return random.choice(state.getLegalPacmanActions())


class BetterRandomAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
         "The agent receives a GameState (defined in pacman.py)."
         print("Location:", state.getPacmanPosition())
         print("Action available:", state.getLegalPacmanActions())
         actions = state.getLegalPacmanActions()
         actions.remove(Directions.STOP)
         import random
         return random.choice(actions)


class ReflexAgent(Agent):
    def getAction(self, state):
        foods = state.getFood().asList()
        walls = state.getWalls()
        position = state.getPacmanPosition()
        print(walls.width)
        print(position)
        self.walk(foods[0],position[0],position[1],walls)
        return Directions.STOP

    def outofrange(self,x,y,walls):
        return x<0 and x>=walls.width and y<0 and y>=walls.height and walls[x][y]

    def walk(self,food,x,y,walls):
        if (x,y)==food:
            print('get food')
        if not self.outofrange(x,y,walls):
            walls[x,y]=True
            if not self.walk(x-1,y,walls):
                walls[x, y] = False
            elif not self.walk(x, y-1, walls):
                walls[x, y] = False
            elif not self.walk(x + 1, y, walls):
                walls[x, y] = False
            elif not self.walk(x, y+1, walls):
                walls[x, y] = False
            else:
                return False

        return True