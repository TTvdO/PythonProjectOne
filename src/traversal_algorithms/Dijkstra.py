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
from Constants import Constants
import queue
import time

class Dijkstra:
    def __init__(self, gridClass, draw):
        self.gridClass = gridClass
        self.grid = gridClass.get_grid()
        self.draw = draw

        self.allNodesBesidesStart = []
        self.allNodes = []
        self.unvisitedList = []
        self.visitedList = []

        self.nodesToIterateThrough = queue.Queue()
        self.nodesToIterateBackThrough = queue.Queue()

        self.lowestCost = 0
        self.currentCost = 0
        self.blocksTraversedFromCurrentNode = 0
        self.adjacentNodesVisited = 0
        self.lowestAdjacentNodeCost = 9999

        self.endpointReached = False
        self.traversedBackToStart = False
        self.twoAdjacentBlocks = False
        self.threeAdjacentBlocks = False
        self.fourAdjacentBlocks = False

        self.currentNode = None
        self.nextCurrentNode = None
        self.startNode = None
        self.endNode = None

        self.initialize_dijkstra()

    def initialize_dijkstra(self):
        for row in self.grid:
            for element in row:
                if type(element) is not Start:
                    element.set_current_positional_cost(9999)
                    self.allNodesBesidesStart.append(element)
                else: #type is Start
                    self.startNode = element
                    self.nodesToIterateThrough.put(element)

    def move(self):
        while not self.traversedBackToStart:
            if not self.nodesToIterateThrough.empty():
                currentNode = self.nodesToIterateThrough.get()
                for otherNode in self.allNodesBesidesStart:
                    if self.other_node_adjacent_to_current_node(currentNode, otherNode):
                        adjacentNode = otherNode
                        if type(adjacentNode) is not End:
                                costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()
                                if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                    # if you're overriding a previous lowest cost that was not the initial value of that position, show that a better value has been found
                                    if adjacentNode.get_current_positional_cost() != 9999:
                                        adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                        self.nodesToIterateThrough.put(adjacentNode)
                                        self.draw.draw_colored_image(Constants.RED_IMAGE, Constants.GREEN, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                            adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                        pygame.display.flip()
                                        # can uncomment to make it more obvious when a value is being overridden.
                                        # time.sleep(0.3)
                                        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                            adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                        pygame.display.flip()
                                    # if this is the first time you've reached this point (positional cost of node is still the initial value), go through standard procedure
                                    else: 
                                        adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                        self.nodesToIterateThrough.put(adjacentNode)
                                        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                            adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                        pygame.display.flip()
                                        
                        else: # if adjacentNode is of type End
                            self.endNode = adjacentNode
                            self.nodesToIterateBackThrough.put(self.endNode)
                            costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()
                            if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                    adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                pygame.display.flip()
                                self.lowestCost = costFromStartToAdjacentNode
            else:
                if not self.traversedBackToStart:
                    self.allNodesBesidesStart.append(self.startNode)
                    self.allNodes = self.allNodesBesidesStart

                    currentNode = self.nodesToIterateBackThrough.get()
                    self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_block(), currentNode.get_y() * self.gridClass.get_room_per_block()),
                                                currentNode.get_block_cost(), currentNode.get_current_positional_cost())

                    self.check_amount_of_adjacent_blocks(currentNode)

                    if self.twoAdjacentBlocks:
                        # start at 3 out of 4 adjacent nodes visited (visit nodes 3, and 4)
                        self.adjacentNodesVisited = 3
                    elif self.threeAdjacentBlocks:
                        # start at 2 out of 4 adjacent nodes visited (visit nodes 2, 3, and 4)
                        self.adjacentNodesVisited = 2
                    else:
                        # start at 1 out of 4 adjacent nodes visited (visit nodes 1, 2, 3, and 4)
                        self.adjacentNodesVisited = 1

                    for otherNode in self.allNodes:
                        if not self.traversedBackToStart:
                            if self.other_node_adjacent_to_current_node(currentNode, otherNode):
                                adjacentNode = otherNode

                                if type(adjacentNode) is Start:
                                    self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                            adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                    pygame.display.flip()
                                    self.traversedBackToStart = True
                                else:
                                    if self.adjacentNodesVisited < 4:
                                        if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
                                            self.nextCurrentNode = adjacentNode
                                            self.lowestAdjacentNodeCost = adjacentNode.get_current_positional_cost()
                                    else: # self.adjacentNodesVisited == 4
                                        if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
                                            self.nextCurrentNode = adjacentNode
                                        self.nodesToIterateBackThrough.put(self.nextCurrentNode)
                                        pygame.display.flip()
                                        
                                        if self.twoAdjacentBlocks:
                                            self.adjacentNodesVisited = 2
                                        elif self.threeAdjacentBlocks:
                                            self.adjacentNodesVisited = 1
                                        else:
                                            self.adjacentNodesVisited = 0

                                        self.lowestAdjacentNodeCost = 9999
                                        # time.sleep(0.25)
                                self.adjacentNodesVisited += 1

    def other_node_adjacent_to_current_node(self, currentNode, otherNode):
        if (((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() + 1) == otherNode.get_y()))
        or ((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() - 1) == otherNode.get_y()))
        or (((currentNode.get_x() + 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))
        or (((currentNode.get_x() - 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))):
            return True
        else:
            return False

    def check_amount_of_adjacent_blocks(self, currentNode):
        # if currentNode resides in one of four corners: (0,0), (0, rowsAndColumns), (rowsAndColumns, 0), (rowsAndColumns, rowsAndColumns)
        # with only 2 adjacent blocks
        if ((currentNode.get_x() == 0 and currentNode.get_y() == 0)
        or (currentNode.get_x() == 0 and (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))
        or (currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1) and currentNode.get_y() == 0)
        or ((currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1)) and (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))):
            self.twoAdjacentBlocks = True
            self.threeAdjacentBlocks = False
            self.fourAdjacentBlocks = False
        elif ((currentNode.get_x() == 0 or currentNode.get_y() == 0)
            or (currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1 ) or (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))):
            self.twoAdjacentBlocks = False
            self.threeAdjacentBlocks = True
            self.fourAdjacentBlocks = False
        else:
            self.twoAdjacentBlocks = False
            self.threeAdjacentBlocks = False
            self.fourAdjacentBlocks = True
                        

    def get_lowest_cost(self):
        return self.lowestCost