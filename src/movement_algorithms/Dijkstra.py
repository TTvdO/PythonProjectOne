import sys
sys.path.append(".")
from src.Grid import Grid

class Dijkstra:
    def __init__(self, grid):
        self.grid = grid
        self.copyOfGrid = self.grid
        # self.unvisitedList
        # self.visitedList

    # def get_copy_of_grid(self):
    #     self.copyOfGrid.get_grid()

    def move(self):
        # have exact copy of the Grid available within this class (the Grid is the same as the Graph within the theory of Dijkstra),
        # all positions have x and y coordinates and you are able to traverse bidirectionally (up/down, left/right by looping through columns and rows)
        #

        # 1. mark all positions of the Grid as unvisited
        #

        # 2. be able to set_cost of terrain for the Grid that the Dijkstra algorithm uses
        # make the cost of any terrain other than the starting position infinite (a.k.a. very high)
        #

        # 3. for the current node, look at all of its unvisited neighbors and consider them (move to all of the adjacent neighbours)
        # if current position A is marked with a distance of 6 and the edge connecting it with a neighbour B has a value of 2, then
        # distance to B is 6+2=8. IF B was previously marked higher than 8 (through traversing with a different route), then change the cost to 8
        #

        # 4. when done with considering unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set
        # a visited node will never be checked again (because you will loop through the unvisited set)
        #

        # 5. if the destination node has been marked visited at this point within the loop, then stop
        #

        # 6. otherwise, select the unvisited node that is marked with the smallest tentatice distance, set it as the new "current node" and repeat the loop from step 3
        #

        pass