from abc import ABCMeta, abstractmethod
import os

class TraversalAlgorithm(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, gridClass, draw):
        self.gridClass = gridClass
        self.grid = gridClass.get_grid()
        self.draw = draw
        self.lowestCost = 0
    
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def backtrack(self):
        pass

    def other_node_adjacent_to_current_node(self, currentNode, otherNode):
        if (((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() + 1) == otherNode.get_y()))
        or ((currentNode.get_x() == otherNode.get_x()) and ((currentNode.get_y() - 1) == otherNode.get_y()))
        or (((currentNode.get_x() + 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))
        or (((currentNode.get_x() - 1) == otherNode.get_x()) and (currentNode.get_y() == otherNode.get_y()))):
            return True
        else:
            return False

    def get_lowest_cost(self):
        return self.lowestCost