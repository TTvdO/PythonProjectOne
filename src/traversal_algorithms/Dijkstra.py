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
                else:
                    self.visitedList.append(element)
                    self.currentNode = element

        # 2. be able to set_cost of terrain for the Grid that the Dijkstra algorithm uses
        # make the cost of any terrain other than the starting position infinite (a.k.a. very high)
        # --> see element.set_cost(9999)

        # 3. for the current node, look at all of its unvisited neighbors and consider them (move to all of the adjacent neighbours)
        # if current position A is marked with a distance of 6 and the edge connecting it with a neighbour B has a value of 2, then
        # distance to B is 6+2=8. IF B was previously marked higher than 8 (through traversing with a different route), then change the cost to 8
        while not self.endPointReached:
            counter = 0
            # for element in unvisitedList with the lowest total cost
            for element in self.unvisitedList:
                # check if element in unvisitedList is adjacten to currentNode
                if self.element_adjacent_to_current_node:
                    if type(element) is not End:
                        # ergens in de method, weet niet of het hier is of niet, moet je nog hiervoor zorgen:
                        # je wilt een lowestCost onthouden in deze klasse naast de currentCost. telkens nadat je element.cost hebt geupdate met currentCost + de cost van het element
                        # in de echte grid, wil je kijken of currentCost < lowestCost. wel moet je dan telkens, de eerste keer als je naar 1 van de adjactent elements kijkt, niet eens
                        # checken of currentCost < lowestCost, maar direct zeggen lowestCost = currentCost, anders krijg je natuurlijk altijd false

                        if counter == 0:
                            element.set_cost(self.currentCost + self.grid[element.get_x()][element.get_y()].get_cost())
                            self.lowestCost = element.get_cost()
                            self.nextCurrentNode = element
                            self.visitedList.append(element)
                            self.unvisitedList.remove(element)

                        # je wilt ook nog ergens hierin kijken welke van de 4 adjacent elements de laagste cost had en deze selecteer je als volgende currentNode,
                        # noem dit variabel nextCurrentNode en nadat de counter 4 is zeg je currentNode = nextCurrentNode

                        # je wilt ook de currentCost updaten telkens als je weer voor een nieuwe currentNode de costs van de adjacent elements wil comparen 
                        elif counter > 0 and counter < 4:
                            element.set_cost(self.currentCost + self.grid[element.get_x()][element.get_y()].get_cost())
                            if element.get_cost() < self.lowestCost:
                                self.lowestCost = element.get_cost()
                                self.nextCurrentNode = element
                            self.visitedList.append(element)
                            self.unvisitedList.remove(element)
                        else: #if counter = 4 (mss moet dit 3 zijn, nog even kijken naar de logica zometeen)
                            self.currentNode = self.nextCurrentNode

                    else # if element is of type End:
                        element.cost = self.currentCost + element.get_cost()
                        self.endpointReached = True
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