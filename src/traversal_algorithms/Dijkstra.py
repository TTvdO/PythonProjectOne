import sys, pygame
# necessary to be able to open import Grid from this file's location
sys.path.append(".")
from src.Grid import Grid
from src.Draw import Draw
from node_types import *
from node_types.Node import Node
from node_types.Forest import Forest
from node_types.Ground import Ground
from node_types.Mountain import Mountain
from node_types.Start import Start
from node_types.End import End
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

        self.visitedNodes = []

        self.nodesToIterateThrough = queue.PriorityQueue()
        # self.nodesToIterateBackThrough = queue.Queue()

        self.lowestCost = 0
        self.adjacentNodesToVisit = 0
        self.lowestAdjacentNodeCost = 9999

        self.traversedBackToStart = False

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
                    self.nodesToIterateThrough.put((0, element))

    def move(self):
        while not self.nodesToIterateThrough.empty():
            currentNode = self.nodesToIterateThrough.get()
            # uncomment to clearly show that dijkstra is selecting the node with lowest positional cost to evaluate adjacent nodes
            # time.sleep(1.5)
            for otherNode in self.allNodesBesidesStart:
                # if otherNode.get_visited == False:
                if self.other_node_adjacent_to_current_node(currentNode, otherNode):
                    adjacentNode = otherNode
                    if type(adjacentNode) is not End:
                            costFromStartToAdjacentNode = currentNode[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                            if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                # if you're overriding a previous lowest cost that was not the initial value of that position, show that a better value has been found
                                if adjacentNode.get_current_positional_cost() != 9999:
                                    adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                    self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                    adjacentNode.set_predecessor_node(currentNode[1])

                                    self.show_value_being_overridden(adjacentNode)
                                    # self.draw.draw_colored_image(Constants.RED_IMAGE, Constants.GREEN, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                    #     adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                    # pygame.display.flip()
                                    # # can uncomment to make it more obvious when a value is being overridden.
                                    # #time.sleep(0.25)
                                    # self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                    #     adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                    # pygame.display.flip()

                                # else if this is the first time you've reached this point (positional cost of node is still the initial value), go through standard procedure
                                else: 
                                    adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                    self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                    adjacentNode.set_predecessor_node(currentNode[1])

                                    self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                        adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                    pygame.display.flip()
                                    
                    else: # if adjacentNode is of type End
                        self.endNode = adjacentNode
                        # self.nodesToIterateBackThrough.put(self.endNode)
                        costFromStartToAdjacentNode = currentNode[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                        if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                            adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                            self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                            adjacentNode.set_predecessor_node(currentNode[1])
                            self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                            pygame.display.flip()
                            self.lowestCost = costFromStartToAdjacentNode

    def other_node_adjacent_to_current_node(self, currentNode, otherNode):
        if (((currentNode[1].get_x() == otherNode.get_x()) and ((currentNode[1].get_y() + 1) == otherNode.get_y()))
        or ((currentNode[1].get_x() == otherNode.get_x()) and ((currentNode[1].get_y() - 1) == otherNode.get_y()))
        or (((currentNode[1].get_x() + 1) == otherNode.get_x()) and (currentNode[1].get_y() == otherNode.get_y()))
        or (((currentNode[1].get_x() - 1) == otherNode.get_x()) and (currentNode[1].get_y() == otherNode.get_y()))):
            return True
        else:
            return False

    def show_value_being_overridden(self, adjacentNode):
        self.draw.draw_colored_image(Constants.RED_IMAGE, Constants.GREEN, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                        adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
        pygame.display.flip()
        # can uncomment to make it more obvious when a value is being overridden.
        # time.sleep(0.25)
        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
            adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
        pygame.display.flip()

    def get_lowest_cost(self):
        return self.lowestCost