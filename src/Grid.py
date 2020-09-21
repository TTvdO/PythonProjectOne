import pygame
import random
from node_types import *
from node_types.Node import Node
from node_types.Forest import Forest
from node_types.Ground import Ground
from node_types.Mountain import Mountain
from node_types.Start import Start
from node_types.End import End
from node_types.Barricade import Barricade
from Constants import Constants

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerNode = self.screenWidthAndHeight / self.rowsAndColumns
        self.hasStartingPoint = False
        self.hasEndPoint = False
        self.amountOfNodesCreated = 0

        self.create_in_memory_grid()

    def create_in_memory_grid(self):
        self.grid = [[self.get_random_node(x, y) for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    def get_random_node(self, x, y):
        randomNumber = random.randrange(1, 63, 1)
        # Create starting point at one index before the last if no starting point has been created yet before then
        if (self.amountOfNodesCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 2)) and self.hasStartingPoint == False:
            node = Start(x, y)
            self.hasStartingPoint = True
        # Create end point at the last index if no end point has been created yet before then
        elif (self.amountOfNodesCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 1)) and self.hasEndPoint == False:
            node = End(x, y)
            self.hasEndPoint = True
        elif randomNumber >= 1 and randomNumber <= 15:
            node = Forest(x, y)
        elif randomNumber > 15 and randomNumber <= 30:
            node = Ground(x, y)
        elif randomNumber > 30 and randomNumber <= 45:
            node = Mountain(x, y)
        elif randomNumber > 45 and randomNumber <= 58:
            node = Barricade(x,y)
        elif randomNumber == 59 or randomNumber == 60:
            if self.hasStartingPoint == False:
                node = Start(x, y)
                self.hasStartingPoint = True
            else:
                node = Ground(x, y)
        else: # if randomNumber == 61 or randomNumber == 62
            if self.hasEndPoint == False:
                node = End(x, y)
                self.hasEndPoint = True
            else:
                node = Ground(x, y)
        self.amountOfNodesCreated+=1
        return node

    def get_room_per_node(self):
        return self.roomPerNode

    def get_amount_of_rows_and_columns(self):
        return self.rowsAndColumns

    def get_grid(self):
        return self.grid