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
        # 1. mark all positions of the Grid as unvisited, except for the current node

        # 2. be able to set_cost of terrain for the Grid that the Dijkstra algorithm uses
        # make the cost of any terrain other than the starting position infinite (a.k.a. very high)
        # --> see element.set_cost(9999)

        # 3. for the current node, look at all of its unvisited neighbors and consider them (move to all of the adjacent neighbours)
        # if current position A is marked with a distance of 6 and the edge connecting it with a neighbour B has a value of 2, then
        # distance to B is 6+2=8. IF B was previously marked higher than 8 (through traversing with a different route), then change the cost to 8


        while not self.nodesToIterateThrough.empty():
            # ADD extra loop here to loop through a Queue of nodes where node has been visited, but its adjacent nodes have not, then for every node in this queue
            # you loop through the elements in the unvisitedlist to see if they're adjacent to the current node's position
            #for currentNode in self.nodesToIterateThrough:
            currentNode = self.nodesToIterateThrough.get()
            # CHANGE: don't loop through every element in the unvisitedList anymore, because you won't be able to override a route that has a higher value at a certain
            # node, due to not checking nodes that have already been visited.
            # instead, just make a list of all nodes and for every single node position check all adjacent nodes, whether they've been visited or not does not matter.
            for otherNode in self.allNodesBesidesStart:
                # if self.element_adjacent_to_current_node:
                if (((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() + 1) == otherNode.get_y()))
                or ((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() - 1) == otherNode.get_y()))
                or (((currentNode.get_x() + 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))
                or (((currentNode.get_x() - 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))):
                    adjacentNode = otherNode
                    if type(adjacentNode) is not End:
                            # set positional cost of current element: positional cost of current node + block cost of current element 
                            #element.set_positional_cost(NODE.get_positional_cost() + element.get_block_cost())

                            # cost would be the node's current positional cost + the element's block cost
                            costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()

                            # if this cost is smaller than the element's positional cost (9999 if element hadn't been reached before yet, or if previous path was a higher cost
                            # than this one)
                            if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                                adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                                self.nodesToIterateThrough.put(adjacentNode)
                                # self.draw.draw_green_image((adjacentNode.get_x(), adjacentNode.get_y()), adjacentNode.get_current_positional_cost())
                                self.draw.draw_green_image((adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()),
                                    adjacentNode.get_current_positional_cost())
                                pygame.display.flip()
                    else: # if adjacentNode is of type End
                        costFromStartToAdjacentNode = currentNode.get_current_positional_cost() + adjacentNode.get_block_cost()

                        # if this cost is smaller than the element's positional cost (9999 if element hadn't been reached before yet, or if previous path was a higher cost
                        # than this one)
                        if costFromStartToAdjacentNode < adjacentNode.get_current_positional_cost():
                            adjacentNode.set_current_positional_cost(costFromStartToAdjacentNode)
                            self.nodesToIterateThrough.put(adjacentNode)
                            # adjacentNode.set_current_positional_cost(currentNode.get_current_positional_cost() + adjacentNode.get_block_cost())
                            self.draw.draw_red_image((adjacentNode.get_x() * self.gridClass.get_room_per_block(), adjacentNode.get_y() * self.gridClass.get_room_per_block()), adjacentNode.get_current_positional_cost())
                            pygame.display.flip()
                        # time.sleep(10)
                        # self.endpointReached = True
                        # TODO:
                            # - show total eventual cost clearly, not only on the end block itself. also stop the program clearly, e.g.: pop-up screen

        # 4. when done with considering unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set
        # a visited node will never be checked again (because you will loop through the unvisited set)
        # [DONE]

        # 5. if the destination node has been marked visited at this point within the loop, then stop
        # [DONE]

        # 6. otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node" and repeat the loop from step 3
        # 

    def element_adjacent_to_current_node(self, currentNode, element):
        if (((currentNode.get_x() == element.get_x()) and ((currentNode.get_y() + 1) == element.get_y()))
            or ((currentNode.get_x() == element.get_x()) and ((currentNode.get_y() - 1) == element.get_y()))
            or (((currentNode.get_x() + 1) == element.get_x()) and (currentNode.get_y() == element.get_y()))
            or (((currentNode.get_x() - 1) == element.get_x()) and (currentNode.get_y() == element.get_y()))):
            return True
        else:
            return False