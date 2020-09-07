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
        self.grid = [[self.get_random_block() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]
        pass

    def get_random_block(self):
        # TOBECOME: instead of storing 0's in this grid, will be filled with classes.
        # generate random integers, and based on these random integers produce:
        # - 1 Start block on a random position
        # - Ground blocks
        # - Forest blocks
        # - Mountain blocks
        # Make sure that:
        # - The start block is only made once (so e.g. if integer outcome 1 creates a start block, check if boolean startBlockMade is already true or not. if it is: don't make a start
        # block)

        # (Zorg dus nog dat je maar 1 start blok hebt)

        # algemene blok type definen
        # block = Block()

        # nummer genereren van 1 tot 4

        # if nummer == 1: block = Forest()

        # elif nummer == 2: block = Ground()

        # elif ...

        # else ...

        # return block i.p.v. 0
        return 0

    # also will need to update this grid after every change later on. can do this by calling draw_grid at the end of the while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid)
    def draw_grid(self, screen):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                # here the grid contents will be different, and you'll be looping through the in memory grid
                # you'll be able to do stuff here based on the type of class stored within the grid. (if type X, paint color blue. if type Y, paint color green)
                # and remember that this is just for visualization purposes, the actual logic will be done by using the in memory grid
                if type(element) is int:
                    rect = pygame.Rect(elementNumber * self.roomPerBlock, rowNumber * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                    pygame.draw.rect(screen, WHITE, rect, 1)
                elif type(element) is Ground:
                    # draw ground block (simply use a different color at first, then move on to using images)
                    pass
                elif type(element) is Forest:
                    # draw forest block (simply use a different color at first, then move on to using images)
                    pass
                elif type(element) is Mountain:
                    # draw mountain block (simply use a different color at first, then move on to using images)
                    pass
                else: # type is Start (best to use Start as last else, because it only occurs once, so a small amount of time is saved not having to skip it over and over):
                    # draw start block (simply use a different color at first, then move on to using images)
                    pass
                elementNumber+=1
            rowNumber+=1