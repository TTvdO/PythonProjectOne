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

class AStar(TraversalAlgorithm):
    def __init__(self, gridClass, draw):
        super().__init__(gridClass, draw)

        self.allNodesBesidesStart = []
        self.allNodes = []

        self.nodesToIterateThrough = queue.PriorityQueue()
        self.nodesToIterateBackThrough = queue.Queue()

        self.lowestCost = 0
        self.totalCost = 0

        self.traversedBackToStart = False
        self.endPointReached = False

        self.startNode = None
        self.endNode = None

        self.initialize()

    def initialize(self):
        for row in self.grid:
            for element in row:
                if type(element) is Start:
                    self.startNode = element
                    self.nodesToIterateThrough.put((0, element))
                elif type(element) is End:
                    element.set_current_positional_cost(9999)
                    self.endNode = element
                    self.allNodesBesidesStart.append(element)
                else: # if type is not Start or End
                    element.set_current_positional_cost(9999)
                    self.allNodesBesidesStart.append(element)

    def move(self):
        while not self.traversedBackToStart:
            if not self.nodesToIterateThrough.empty():
                if self.endPointReached == False:
                    currentNodeTuple = self.nodesToIterateThrough.get()
                    # gCost = self.get_manhattan_distance(adjacentNode, self.startNode)
                    # hCost = self.get_manhattan_distance(adjacentNode, self.endNode)
                    # fCost = gCost + hCost
                    if type(currentNodeTuple[1]) is not Start:
                        # TODO: change this to display the g, h, & f costs in the drawing
                        self.draw.draw_colored_image(Constants.GREEN_IMAGE, Constants.RED, (currentNodeTuple[1].get_x() * self.gridClass.get_room_per_node(),
                                                    currentNodeTuple[1].get_y() * self.gridClass.get_room_per_node()),
                                                    currentNodeTuple[1].get_edge_cost(), currentNodeTuple[1].get_current_positional_cost())
                        pygame.display.flip()
                    # uncomment line below to clearly show that AStar is selecting the node or one of the nodes 
                    # with the lowest positional cost to evaluate adjacent nodes for
                    time.sleep(.75)
                    currentNodeTuple[1].set_visited(True)
                    for otherNode in self.allNodesBesidesStart:
                        if otherNode.get_visited() == False:
                            if self.other_node_adjacent_to_current_node(currentNodeTuple[1], otherNode):
                                adjacentNode = otherNode
                                if type(adjacentNode) is not End:
                                        # change the way the costFromStartToAdjacentNode is calculated. For A* you no longer want to prioritize nodes based
                                        # on weighted costs (sum of edge costs), instead, you want to prioritize based on the AStar heuristic in which the g, h, & f costs are used
                                        # the g, h, & f costs represent:
                                        # -G COST: the manhattan distance from a specific node to the start node
                                        # -H COST: the manhattan distance from a specific node to the end node
                                        # -F COST: total manhattan distance (sum of g and h cost)
                                        # TODO#1: if multiple f costs are the same, prioritize nodes based on lower H costs (nodes closer to end goal)
                                        # TODO#2: if multiple h costs are the same, prioritize nodes based on lower edge costs
                                        # or perhaps a combination of both TODO's at the same time
                                        gCost = self.get_manhattan_distance(adjacentNode, self.startNode)
                                        hCost = self.get_manhattan_distance(adjacentNode, self.endNode)
                                        fCost = gCost + hCost
                                        if fCost < adjacentNode.get_current_positional_cost():
                                            adjacentNode.set_current_positional_cost(fCost)
                                            adjacentNode.set_predecessor_node(currentNodeTuple[1])
                                            self.nodesToIterateThrough.put((fCost, adjacentNode))
                                else: # if adjacentNode is of type End
                                    gCost = self.get_manhattan_distance(adjacentNode, self.startNode)
                                    hCost = self.get_manhattan_distance(adjacentNode, self.endNode)
                                    fCost = gCost + hCost
                                    # unnecessary line if you immediately end the loop when reaching the end for the first time
                                    # if fCost < adjacentNode.get_current_positional_cost():
                                    self.endNode.set_current_positional_cost(fCost)
                                    self.endNode.set_predecessor_node(currentNodeTuple[1])
                                    self.nodesToIterateBackThrough.put(self.endNode)
                                    self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (adjacentNode.get_x() * self.gridClass.get_room_per_node(), 
                                        adjacentNode.get_y() * self.gridClass.get_room_per_node()),
                                        adjacentNode.get_edge_cost(), adjacentNode.get_current_positional_cost())
                                    pygame.display.flip()
                                    self.endPointReached = True
                else: # if self.endPointReached == True, show path from endpoint to startpoint
                    if not self.traversedBackToStart:
                        self.backtrack()

    def backtrack(self):
        self.allNodesBesidesStart.append(self.startNode)
        self.allNodes = self.allNodesBesidesStart
        while not self.nodesToIterateBackThrough.empty():
            currentNode = self.nodesToIterateBackThrough.get()
            # for AStar, count the total cost at the end while backtracking, since the actual weighted costs aren't used for the algorithm itself
            self.totalCost += currentNode.get_edge_cost()
            self.draw.draw_colored_image(Constants.BLACK_IMAGE, Constants.WHITE, (currentNode.get_x() * self.gridClass.get_room_per_node(), currentNode.get_y() * self.gridClass.get_room_per_node()),
                                            currentNode.get_edge_cost(), currentNode.get_current_positional_cost())
            pygame.display.flip()
            if type(currentNode) is not Start:
                self.nodesToIterateBackThrough.put(currentNode.get_predecessor_node())
            else:
                self.lowestCost = self.totalCost
                self.traversedBackToStart = True

    # start is current node, goal is end or start node. use abs() so that result is always a positive number representing the distance
    def get_manhattan_distance(self, specificNode, endOrStartNode):
        rowDistance = abs(specificNode.get_x() - endOrStartNode.get_x())
        columnDistance = abs(specificNode.get_y() - endOrStartNode.get_y())
        return rowDistance + columnDistance