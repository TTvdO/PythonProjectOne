import sys
sys.path.append(".")
from src.Grid import Grid
from block_types import *
from block_types.Block import Block
from block_types.Forest import Forest
from block_types.Ground import Ground
from block_types.Mountain import Mountain
from block_types.Start import Start
from block_types.End import End

class Dijkstra:
    def __init__(self, grid):
        # use grid to get the actual costs of nodes within the Graph, 
        # to call the "draw_green_image()" method on nodes you're adding to the visitedList,
        # and to call the "set_cost" method on nodes you're adding to the visitedList 
        self.grid = grid
        # use copyOfGrid to modify the costs of terrain temporarily within the unvisitedList
        self.copyOfGrid = self.grid
        self.unvisitedList = []
        self.visitedList = []
        self.endPointReached = false

    def move(self):
        # have exact copy of the Grid available within this class (the Grid is the same as the Graph within the theory of Dijkstra),
        # all positions have x and y coordinates and you are able to traverse bidirectionally (up/down, left/right by looping through columns and rows)

        # mark X and Y position of current node, keep this updated
        currentX = 0
        currentY = 0

        # 1. mark all positions of the Grid as unvisited, except for the current node
        for row in self.copyOfGrid:
            for element in row:
                if type(element) is not Start:
                    element.set_cost(9999)
                    self.unvisitedList.append(element)
                else:
                    self.visitedList.append(element)
                    currentX = element  # moet worden: currentX = element.posXandYtuple[0]
                    currentY = row      # moet worden: currentY = element.posXandYtuple[1]

        # 2. be able to set_cost of terrain for the Grid that the Dijkstra algorithm uses
        # make the cost of any terrain other than the starting position infinite (a.k.a. very high)
        # --> see element.set_cost(9999)

        # 3. for the current node, look at all of its unvisited neighbors and consider them (move to all of the adjacent neighbours)
        # if current position A is marked with a distance of 6 and the edge connecting it with a neighbour B has a value of 2, then
        # distance to B is 6+2=8. IF B was previously marked higher than 8 (through traversing with a different route), then change the cost to 8
        while not endPointReached:
            for unvisitedList:
                # je hebt de X en Y coordinaten nodig van elk element in de unvisitedList, zodat je kan zeggen
                # if posXandYtuple = (currentX + 1, currentY) or (currentX - 1, current Y) or (currentX, currentY + 1) or (currentX, currentY - 1):
                    # dan wil je voor deze aanliggende posities:
                    # - de cost updaten in self.copyOfGrid, waar je zegt: self.copyOfGrid[x][y] = currentCost + self.grid[x][y].cost
                    # - de positie aan de visitedList toevoegen 


        # 4. when done with considering unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set
        # a visited node will never be checked again (because you will loop through the unvisited set)
        #

        # 5. if the destination node has been marked visited at this point within the loop, then stop
        #

        # 6. otherwise, select the unvisited node that is marked with the smallest tentatice distance, set it as the new "current node" and repeat the loop from step 3
        #

        pass