import sys, pygame
# necessary to be able to open import Grid from this file's location
sys.path.append(".")
from src.Grid import Grid
from src.Draw import Draw
from .TraversalAlgorithm import TraversalAlgorithm
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

class Dijkstra(TraversalAlgorithm):
    def __init__(self, gridClass, draw):
        super().__init__(gridClass, draw)

        self.allNodesBesidesStart = []
        self.allNodes = []

        self.nodesToIterateThrough = queue.PriorityQueue()
        self.nodesToIterateBackThrough = queue.Queue()

        self.lowestCost = 0

        self.traversedBackToStart = False

        self.startNode = None
        self.endNode = None

        self.initialize()

    def initialize(self):
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
                if type(currentNodeTuple[1]) is not Start:
                    self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (currentNodeTuple[1].get_x() * self.gridClass.get_room_per_node(), 
                                                    currentNodeTuple[1].get_y() * self.gridClass.get_room_per_node()),
                                                    currentNodeTuple[1].get_edge_cost(), currentNodeTuple[1].get_current_positional_cost())
                    pygame.display.flip()
                # uncomment line below to clearly show that dijkstra is selecting the node or one of the nodes 
                # with the lowest positional cost to evaluate adjacent nodes for
                # time.sleep(1.5)
                currentNodeTuple[1].set_visited(True)
                for otherNode in self.allNodesBesidesStart:
                    if otherNode.get_visited() == False:
                        if otherNode.get_traversable() == True:
                            if self.other_node_adjacent_to_current_node(currentNodeTuple[1], otherNode):
                                adjacentNode = otherNode
                                if type(adjacentNode) is not End:
                                        costFromStartToAdjacentNode = currentNodeTuple[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                                        if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                                adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                                adjacentNode.set_predecessor_node(currentNodeTuple[1])
                                                self.nodesToIterateThrough.put((costFromStartToAdjacentNode, adjacentNode))
                                else: # if adjacentNode is of type End
                                    costFromStartToAdjacentNode = currentNodeTuple[1].get_current_positional_cost() + adjacentNode.get_edge_cost()
                                    if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                        self.endNode = adjacentNode
                                        self.endNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                        self.endNode.set_predecessor_node(currentNodeTuple[1])
                                        self.nodesToIterateBackThrough.put(self.endNode)
                                        self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), 
                                            adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                            adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                        pygame.display.flip()
                                        self.lowestCost = costFromStartToAdjacentNode
            else: # if nodesToIterateThrough.empty(), show path from endpoint to startpoint
                if not self.traversedBackToStart:
                    self.backtrack()

    def backtrack(self):
        self.allNodesBesidesStart.append(self.startNode)
        self.allNodes = self.allNodesBesidesStart

        while not self.nodesToIterateBackThrough.empty():
            currentNode = self.nodesToIterateBackThrough.get()
            self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_node(), currentNode.get_y() * self.gridClass.get_room_per_node()),
                                            currentNode.get_edge_cost(), currentNode.get_current_positional_cost())
            pygame.display.flip()
            if type(currentNode) is not Start:
                self.nodesToIterateBackThrough.put(currentNode.get_predecessor_node())
            else:
                self.traversedBackToStart = True