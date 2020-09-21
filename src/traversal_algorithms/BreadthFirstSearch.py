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

class BreadthFirstSearch:
    def __init__(self, gridClass, draw):
        self.gridClass = gridClass
        self.grid = gridClass.get_grid()
        self.draw = draw

        self.allNodesBesidesStart = []
        self.allNodes = []

        self.nodesToIterateThrough = queue.Queue()
        self.nodesToIterateBackThrough = queue.Queue()

        self.lowestCost = 0
        self.adjacentNodesToVisit = 0
        self.lowestAdjacentNodeCost = 9999

        self.traversedBackToStart = False
        self.twoAdjacentBlocks = False
        self.threeAdjacentBlocks = False
        self.fourAdjacentBlocks = False

        self.nextCurrentNode = None
        self.startNode = None
        self.endNode = None

        self.initialize_bfs()

    def initialize_bfs(self):
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
                                        #time.sleep(0.25)
                                        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                            adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                        pygame.display.flip()

                                    # else if this is the first time you've reached this point (positional cost of node is still the initial value), go through standard procedure
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
                                self.nodesToIterateThrough.put(adjacentNode)
                                self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                    adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                                pygame.display.flip()
                                self.lowestCost = costFromStartToAdjacentNode
            else: # if nodesToIterateThrough.empty(), show path from endpoint to startpoint
                if not self.traversedBackToStart:
                    self.backtrack()

    def other_node_adjacent_to_current_node(self, currentNode, otherNode):
        if (((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() + 1) == otherNode.get_y()))
        or ((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() - 1) == otherNode.get_y()))
        or (((currentNode.get_x() + 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))
        or (((currentNode.get_x() - 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))):
            return True
        else:
            return False

    def backtrack(self):
        self.allNodesBesidesStart.append(self.startNode)
        self.allNodes = self.allNodesBesidesStart

        currentNode = self.nodesToIterateBackThrough.get()
        self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_block(), currentNode.get_y() * self.gridClass.get_room_per_block()),
                                    currentNode.get_block_cost(), currentNode.get_current_positional_cost())
        pygame.display.flip()

        self.check_amount_of_adjacent_blocks(currentNode)
        self.update_adjacent_blocks_booleans()
        
        for otherNode in self.allNodes:
            if not self.traversedBackToStart:
                if self.other_node_adjacent_to_current_node(currentNode, otherNode):
                    self.adjacentNodesToVisit -= 1

                    adjacentNode = otherNode
                    if type(adjacentNode) is Start:
                        self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                adjacentNode.get_block_cost(), adjacentNode.get_current_positional_cost())
                        pygame.display.flip()
                        self.traversedBackToStart = True
                    else:
                        if self.adjacentNodesToVisit > 0:
                            if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
                                self.nextCurrentNode = adjacentNode
                                self.lowestAdjacentNodeCost = adjacentNode.get_current_positional_cost()
                        else: # self.adjacentNodesToVisit == 0, 
                            # put the node with the lowest cost out of the evaluated adjacent blocks as the next node in the queue to evaluate adjacent nodes for
                            # and draw a black image over this position after calling .get() before this for loop is activated
                            if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
                                self.nextCurrentNode = adjacentNode

                            self.nodesToIterateBackThrough.put(self.nextCurrentNode)

                            self.update_adjacent_blocks_booleans()
                            self.lowestAdjacentNodeCost = 9999

    def check_amount_of_adjacent_blocks(self, currentNode):
        # if currentNode resides in one of four corners: 
        #   1-(0,0), 
        #   2-(0, (amountOfRowsAndColumns - 1)), 
        #   3-((amountOfRowsAndColumns - 1), 0), 
        #   4-((amountOfRowsAndColumns - 1), (amountOfRowsAndColumns - 1))
        # then this node only has two adjacent blocks
        if ((currentNode.get_x() == 0 and currentNode.get_y() == 0)
        or (currentNode.get_x() == 0 and (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))
        or (currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1) and currentNode.get_y() == 0)
        or ((currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1)) and (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))):
            self.twoAdjacentBlocks = True
            self.threeAdjacentBlocks = False
            self.fourAdjacentBlocks = False
        # if currentNodes resides at an edge: 
        #   1- x or y = 0
        #   2- x or y = (amountOfRowsAndColumns - 1))
        # then this node only has three adjacent blocks 
        elif ((currentNode.get_x() == 0 or currentNode.get_y() == 0)
            or (currentNode.get_x() == (self.gridClass.get_amount_of_rows_and_columns() - 1 ) or (currentNode.get_y() == (self.gridClass.get_amount_of_rows_and_columns() - 1)))):
            self.twoAdjacentBlocks = False
            self.threeAdjacentBlocks = True
            self.fourAdjacentBlocks = False
        else:
            self.twoAdjacentBlocks = False
            self.threeAdjacentBlocks = False
            self.fourAdjacentBlocks = True

    def update_adjacent_blocks_booleans(self):
        if self.twoAdjacentBlocks:
            self.adjacentNodesToVisit = 2
        elif self.threeAdjacentBlocks:
            self.adjacentNodesToVisit = 3
        else:
            self.adjacentNodesToVisit = 4

    def get_lowest_cost(self):
        return self.lowestCost