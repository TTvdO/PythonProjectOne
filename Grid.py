import pygame
from blocktypes import *

WHITE = 255, 255, 255

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns

        self.create_in_memory_grid()
    
    def create_in_memory_grid(self):
        # TOBECOME: instead of storing 0's in this grid, will be filled with classes.
        # generate random integers, and based on these random integers produce:
        # - 1 Start block on a random position
        # - Ground blocks
        # - Forest blocks
        # - Mountain blocks
        # Make sure that:
        # - Blocks are not overridden (if position [x][y] is taken, then )
        # - The start block is only made once (so e.g. if integer outcome 1 creates a start block, check if boolean startBlockMade is already true or not. if it is: don't make a start
        # block)
        self.grid = [[0 for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]
        pass

    # also will need to update this grid after every change later on. can do this by calling draw_grid at the end of the while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid)
    def draw_grid(self, screen):
        for column in range(self.rowsAndColumns):
            for row in range(self.rowsAndColumns):
                # here the grid contents will be different, and you'll be looping through the in memory grid
                # you'll be able to do stuff here based on the type of class stored within the grid. (if type X, paint color blue. if type Y, paint color green)
                # and remember that this is just for visualization purposes, the actual logic will be done by using the in memory grid
                if type(self.grid[row][column]) is int:
                    rect = pygame.Rect(column * self.roomPerBlock, row * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                    pygame.draw.rect(screen, WHITE, rect, 1)
                elif type(self.grid[row][column]) is Start:
                    # make start block
                    pass
                elif type(self.grid[row][column]) is Forest:
                    # make forest block
                    pass
                elif type(self.grid[row][column]) is Mountain:
                    # make mountain block
                    pass
                else:
                    # ground
                    pass