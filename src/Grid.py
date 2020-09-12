import pygame
import random
from block_types import *
from block_types.Block import Block
from block_types.Forest import Forest
from block_types.Ground import Ground
from block_types.Mountain import Mountain
from block_types.Start import Start
from block_types.End import End
from Constants import Constants

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns
        self.hasStartingPoint = False
        self.hasEndPoint = False
        self.amountOfBlocksCreated = 0
        self.amountOfTimesCalled = 0

        self.create_in_memory_grid()

    def create_in_memory_grid(self):
        # je kan hier het best de x en y doorgeven. als dat niet kan met deze syntax, moet je hier een dubbele for loop van maken om de x en y door te kunnen geven
        # aan de self.get_random_block() method
        self.grid = [[self.get_random_block(x, y) for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    # within this method, you want to not only create a certain Terrain, but you want to give an X and Y value to the terrain created in the constructor.
    # so keep track of the self.rowsAndColumns attribute and make sure that the X and Y values are correctly updated throughout the method.
    # might need help from create_in_memory_grid
    def get_random_block(self, x, y):
        randomNumber = random.randrange(1, 48, 1)
        # Create starting point at one index before the last if no starting point has been created yet before then
        if (self.amountOfBlocksCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 2)) and self.hasStartingPoint == False:
            block = Start()
            self.hasStartingPoint = True
        # Create end point at the last index if no end point has been created yet before then
        elif (self.amountOfBlocksCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 1)) and self.hasEndPoint == False:
            block = End()
            self.hasEndPoint = True
        elif randomNumber >= 1 and randomNumber <= 15:
            block = Forest()
        elif randomNumber > 15 and randomNumber <= 30:
            block = Ground()
        elif randomNumber > 30 and randomNumber <= 45:
            block = Mountain()
        elif randomNumber == 46:
            if self.hasStartingPoint == False:
                block = Start()
                self.hasStartingPoint = True
            else:
                block = Ground()
        else:
            if self.hasEndPoint == False:
                block = End()
                self.hasEndPoint = True
            else:
                block = Ground()
        self.amountOfBlocksCreated+=1
        self.amountOfTimesCalled+=1
        return block

    def get_room_per_block(self):
        return self.roomPerBlock

    def get_grid(self):
        return self.grid