import sys
# necessary to be able to open import Grid from this file's location
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

        self.lowestCost = 0
        self.currentCost = 0

        self.endPointReached = false

        self.currentNode = None
        self.nextCurrentNode = None

    def move(self):
        # 1. mark all positions of the Grid as unvisited, except for the current node
        for row in self.copyOfGrid:
            for element in row:
                if type(element) is not Start:
                    element.set_cost(9999)
                    self.unvisitedList.append(element)
                else: #type is Start
                    self.visitedList.append(element)
                    self.currentNode = element

        # 2. be able to set_cost of terrain for the Grid that the Dijkstra algorithm uses
        # make the cost of any terrain other than the starting position infinite (a.k.a. very high)
        # --> see element.set_cost(9999)

        # 3. for the current node, look at all of its unvisited neighbors and consider them (move to all of the adjacent neighbours)
        # if current position A is marked with a distance of 6 and the edge connecting it with a neighbour B has a value of 2, then
        # distance to B is 6+2=8. IF B was previously marked higher than 8 (through traversing with a different route), then change the cost to 8

        # TODO STILL IN THIS WHILE LOOP:
        #   - call the method to draw a green block whenever you have added an element to the visitedList. use the element's x and y coordinates as arguments
        #   - also the cost of that element on top of the method to draw a green block, this can be done by calling element.get_cost() from the element within the list after you have
        #       added it to the visitedList

        # TODO STILL WITHIN THE APPLICATION:
        #   - initialize the Dijkstra class within 'main' 
        #   - use this Dijkstra move method within the while loop of 'main'
        while not self.endPointReached:
            counter = 0
            for element in self.unvisitedList:
                if self.element_adjacent_to_current_node:
                    if type(element) is not End:
                        if counter == 0:
                            element.set_cost(self.currentCost + self.grid[element.get_x()][element.get_y()].get_cost())
                            self.lowestCost = element.get_cost()
                            self.nextCurrentNode = element
                            self.visitedList.append(element)
                            self.unvisitedList.remove(element)

                        else:
                            element.set_cost(self.currentCost + self.grid[element.get_x()][element.get_y()].get_cost())
                            if element.get_cost() < self.lowestCost:
                                self.lowestCost = element.get_cost()
                                self.nextCurrentNode = element
                            self.visitedList.append(element)
                            self.unvisitedList.remove(element)
                            # if 3 previous adjacent elements have been evaluated before this element, then this element is the 4th and final element to be evaluated
                            # for the currentNode's position
                            if counter == 3:
                                self.currentNode = self.nextCurrentNode
                    else # if element is of type End:
                        element.cost = self.currentCost + element.get_cost()
                        self.endpointReached = True
                        # TODO:
                            # - show total cost somewhere
                    counter+=1

        # 4. when done with considering unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set
        # a visited node will never be checked again (because you will loop through the unvisited set)
        # [DONE]

        # 5. if the destination node has been marked visited at this point within the loop, then stop
        # [DONE]

        # 6. otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node" and repeat the loop from step 3
        # 

    def element_adjacent_to_current_node(self, element):
        if currentNode.get_x() == element.get_x() and currentElement.get_y() + 1 == element.get_y()
        or currentNode.get_x() == element.get_x() and currentElement.get_y() - 1 == element.get_y()
        or currentNode.get_x() + 1 == element.get_x() and currentElement.get_y() == element.get_y()
        or currentNode.get_x() - 1== element.get_x() and currentElement.get_y() == element.get_y():
            return True
        else:
            return False