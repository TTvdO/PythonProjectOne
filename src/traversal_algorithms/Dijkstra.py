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
        self.nodesToIterateBackThrough = queue.Queue()

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
        while not self.traversedBackToStart:
            if not self.nodesToIterateThrough.empty():
                currentNodeTuple = self.nodesToIterateThrough.get()
                # uncomment to clearly show that dijkstra is selecting the node with lowest positional cost to evaluate adjacent nodes
                # time.sleep(1.5)
                currentNodeTuple[1].set_visited(True)
                for otherNode in self.allNodesBesidesStart:
                    if otherNode.get_visited() == False:
                        if self.other_node_adjacent_to_current_node(currentNodeTuple[1], otherNode):
                            adjacentNode = otherNode
                            if type(adjacentNode) is not End:
                                    costFromStartToAdjacentNode = currentNodeTuple[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                                    if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                        # if you're overriding a previous lowest cost that was not the initial value of that position, show that a better value has been found
                                        if adjacentNode.get_current_positional_cost() != 9999:
                                            adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                            adjacentNode.set_predecessor_node(currentNodeTuple[1])
                                            self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                            

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
                                            adjacentNode.set_predecessor_node(currentNodeTuple[1])
                                            self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                            

                                            self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                                adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                            pygame.display.flip()
                                            
                            else: # if adjacentNode is of type End
                                # self.endNode = adjacentNode
                                # self.nodesToIterateBackThrough.put(self.endNode)
                                costFromStartToAdjacentNode = currentNodeTuple[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                                if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                    self.endNode = adjacentNode
                                    self.endNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                    self.endNode.set_predecessor_node(currentNodeTuple[1])
                                    self.nodesToIterateBackThrough.put(self.endNode)
                                    # self.endNode.set_predecessor_node(currentNodeTuple[1])
                                    # self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                    # self.nodesToIterateBackThrough.put(adjacentNode)

                                    self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                        adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
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

    def show_value_being_overridden(self, adjacentNode):
        self.draw.draw_colored_image(Constants.RED_IMAGE, Constants.GREEN, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                        adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
        pygame.display.flip()
        # can uncomment to make it more obvious when a value is being overridden.
        # time.sleep(0.25)
        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
            adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
        pygame.display.flip()

    def backtrack(self):
        self.allNodesBesidesStart.append(self.startNode)
        self.allNodes = self.allNodesBesidesStart

        while not self.nodesToIterateBackThrough.empty():
            currentNode = self.nodesToIterateBackThrough.get()
            if type(currentNode) is not Start:
                self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_node(), currentNode.get_y() * self.gridClass.get_room_per_node()),
                                            currentNode.get_edge_cost(), currentNode.get_current_positional_cost())
                pygame.display.flip()
                self.nodesToIterateBackThrough.put(currentNode.get_predecessor_node())
            else:
                self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_node(), currentNode.get_y() * self.gridClass.get_room_per_node()),
                                            currentNode.get_edge_cost(), currentNode.get_current_positional_cost())
                pygame.display.flip()
                self.traversedBackToStart = True
        
        # for otherNode in self.allNodes:
        #     if not self.traversedBackToStart:
        #         if self.other_node_adjacent_to_current_node(currentNode, otherNode):
        #             self.adjacentNodesToVisit -= 1

        #             adjacentNode = otherNode
        #             if type(adjacentNode) is Start:
        #                 self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), adjacentNode.get_y() * self.gridClass.get_room_per_node()),
        #                         adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
        #                 pygame.display.flip()
        #                 self.traversedBackToStart = True
        #             else:
        #                 if self.adjacentNodesToVisit > 0:
        #                     if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
        #                         self.nextCurrentNode = adjacentNode
        #                         self.lowestAdjacentNodeCost = adjacentNode.get_current_positional_cost()
        #                 else: # self.adjacentNodesToVisit == 0, 
        #                     # put the node with the lowest cost out of the evaluated adjacent nodes as the next node in the queue to evaluate adjacent nodes for
        #                     # and draw a black image over this position after calling .get() before this for loop is activated
        #                     if adjacentNode.get_current_positional_cost() < self.lowestAdjacentNodeCost:
        #                         self.nextCurrentNode = adjacentNode

        #                     self.nodesToIterateBackThrough.put(self.nextCurrentNode)

        #                     self.update_adjacent_nodes_booleans()
        #                     self.lowestAdjacentNodeCost = 9999

    def get_lowest_cost(self):
        return self.lowestCost