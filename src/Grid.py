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

        self.create_in_memory_grid()

    def create_in_memory_grid(self):
        self.grid = [[self.get_random_block(x, y) for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    def get_random_block(self, x, y):
        randomNumber = random.randrange(1, 48, 1)
        # Create starting point at one index before the last if no starting point has been created yet before then
        if (self.amountOfBlocksCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 2)) and self.hasStartingPoint == False:
            block = Start(x, y)
            self.hasStartingPoint = True
        # Create end point at the last index if no end point has been created yet before then
        elif (self.amountOfBlocksCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 1)) and self.hasEndPoint == False:
            block = End(x, y)
            self.hasEndPoint = True
        elif randomNumber >= 1 and randomNumber <= 15:
            block = Forest(x, y)
        elif randomNumber > 15 and randomNumber <= 30:
            block = Ground(x, y)
        elif randomNumber > 30 and randomNumber <= 45:
            block = Mountain(x, y)
        elif randomNumber == 46:
            if self.hasStartingPoint == False:
                block = Start(x, y)
                self.hasStartingPoint = True
            else:
                block = Ground(x, y)
        else:
            if self.hasEndPoint == False:
                block = End(x, y)
                self.hasEndPoint = True
            else:
                block = Ground(x, y)
        self.amountOfBlocksCreated+=1
        return block

    def get_room_per_block(self):
        return self.roomPerBlock

    def get_amount_of_rows_and_columns(self):
        return self.rowsAndColumns

    def get_grid(self):
        return self.grid