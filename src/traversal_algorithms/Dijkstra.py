import sys, pygame
# necessary to be able to open import Grid from this file's location
sys.path.append(".")
from src.Grid import Grid
from src.Draw import Draw
from block_types import *
from block_types.Block import Block
from block_types.Forest import Forest
from block_types.Ground import Ground
from block_types.Mountain import Mountain
from block_types.Start import Start
from block_types.End import End
import queue
import time

class Dijkstra:
    def __init__(self, gridClass, draw):
        # use grid to get the actual costs of nodes within the Graph, 
        # to call the "draw_green_image()" method on nodes you're adding to the visitedList,
        # and to call the "set_cost" method on nodes you're adding to the visitedList 
        self.gridClass = gridClass
        self.grid = gridClass.get_grid()
        self.draw = draw

        # use copyOfGrid to modify the costs of terrain temporarily within the unvisitedList

        # ! original grid was getting updated as well when you were updating the copyOfGrid values, you need a deepcopy of the object
        # or something similar. you can't just say self.copyOfGrid = self.grid, because you are just creating another reference to the grid
        # instead of actually copying it, where modification doesn't impact it  
        # self.copyOfGrid = deepcopy(self.grid)

        self.allNodesBesidesStart = []
        self.unvisitedList = []
        self.visitedList = []

        # self.queueOfNodes = queue.Queue(maxsize=(gridClass.rowsAndColumns*gridClass.rowsAndColumns))
        self.nodesToIterateThrough = queue.Queue()

        self.lowestCost = 0
        self.currentCost = 0
        self.blocksTraversedFromCurrentNode = 0

        self.endpointReached = False

        self.currentNode = None
        self.nextCurrentNode = None

        self.initialize_dijkstra()

    def initialize_dijkstra(self):
        for row in self.grid:
            for element in row:
                if type(element) is not Start:
                    element.set_current_positional_cost(9999)
                    self.allNodesBesidesStart.append(element)
                else: #type is Start
                    self.nodesToIterateThrough.put(element)

    def move(self):
        while not self.nodesToIterateThrough.empty():
            currentNode = self.nodesToIterateThrough.get()
            for otherNode in self.allNodesBesidesStart:
                if (((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() + 1) == otherNode.get_y()))
                or ((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() - 1) == otherNode.get_y()))
                or (((currentNode.get_x() + 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))
                or (((currentNode.get_x() - 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))):
                    adjacentNode = otherNode
                    if type(adjacentNode) is not End:
                            costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()

                            if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                self.nodesToIterateThrough.put(adjacentNode)
                                self.draw.draw_green_image((adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                    adjacentNode.get_current_positional_cost())
                                pygame.display.flip()
                    else: # if adjacentNode is of type End
                        costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()
                        if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                            adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                            self.lowestCost = costFromStartToAdjacentNode
                            self.nodesToIterateThrough.put(adjacentNode)
                            self.draw.draw_red_image((adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()), adjacentNode.get_current_positional_cost())
                            pygame.display.flip()
                            # TODO:
                                # - show total eventual cost clearly, not only on the end block itself. also stop the program clearly, e.g.: pop-up screen

    def element_adjacent_to_current_node(self, currentNode, element):
        if (((currentNode.get_x() == element.get_x()) and ((currentNode.get_y() + 1) == element.get_y()))
            or ((currentNode.get_x() == element.get_x()) and ((currentNode.get_y() - 1) == element.get_y()))
            or (((currentNode.get_x() + 1) == element.get_x()) and (currentNode.get_y() == element.get_y()))
            or (((currentNode.get_x() - 1) == element.get_x()) and (currentNode.get_y() == element.get_y()))):
            return True
        else:
            return False

    def get_lowest_cost(self):
        return self.lowestCost