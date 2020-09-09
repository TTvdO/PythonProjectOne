import pygame
import random
from blocktypes import *
from blocktypes.Block import Block
from blocktypes.Forest import Forest
from blocktypes.Ground import Ground
from blocktypes.Mountain import Mountain
from blocktypes.Start import Start
from PIL import Image

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
RANDOM = 122, 155, 188

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns

        self.create_in_memory_grid()
    
    # def create_in_memory_grid_deprecated(self):
    #     self.grid = [[self.get_random_block() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    def create_in_memory_grid(self):
        self.grid = [[Mountain() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]
        # self.create_in_memory_grid_two()

    def create_in_memory_grid_two(self):
        startAlreadyExists = False
        #self.grid[0][0] = Mountain()
        for row in self.grid:
            for element in row:
                # successful = False
                # while not successful:
                    randomNumber = random.randrange(1, 5, 1)
                    if randomNumber == 1:
                        element = Forest()
                        self.grid.append(element)
                        #successful = True
                    elif randomNumber == 2:
                        element = Ground()
                        self.grid.append(element)
                        #successful = True
                    elif randomNumber == 3:
                        element = Mountain()
                        self.grid.append(element)
                        #successful = True
                    else:
                        if not startAlreadyExists:
                            element = Start()
                            self.grid.append(element)
                            #successful = True

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

        # nummer genereren van 1 tot 4
        randomNumber = random.randrange(1, 5, 1)

        # if nummer == 1: block = Forest()
        if randomNumber == 1:
            block = Forest()

        # elif nummer == 2: block = Ground()
        elif randomNumber == 2:
            block = Ground()

        # elif ...
        elif randomNumber == 3:
            block = Mountain()

        # else ...
        else:
            block = Start()

        # return block i.p.v. 0
        return block

    # also will need to update this grid after every change later on. can do this by calling draw_grid at the end of the while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid)
    def draw_grid(self, screen):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                rect = pygame.Rect(elementNumber * self.roomPerBlock, rowNumber * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                # here the grid contents will be different, and you'll be looping through the in memory grid
                # you'll be able to do stuff here based on the type of class stored within the grid. (if type X, paint color blue. if type Y, paint color green)
                # and remember that this is just for visualization purposes, the actual logic will be done by using the in memory grid
                if type(element) is int:
                    pygame.draw.rect(screen, BLACK, rect, 1)
                elif type(element) is Ground:
                    # draw ground block (simply use a different color at first, then move on to using images)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                    pass
                elif type(element) is Forest:
                    # draw forest block (simply use a different color at first, then move on to using images)
                    pygame.draw.rect(screen, GREEN, rect, 1)
                    pass
                elif type(element) is Mountain:
                    # draw mountain block (simply use a different color at first, then move on to using images)
                    mtnImage = pygame.image.load("images/tile.jpg")
                    # rect = mtnImage.get_rect()
                    screen.blit(mtnImage, (100,100))
                    # pygame.draw.rect(screen, RED, rect, 1)
                    pass
                else: # type is Start (best to use Start as last else, because it only occurs once, so a small amount of time is saved not having to skip it over and over):
                    # draw start block (simply use a different color at first, then move on to using images)
                    pygame.draw.rect(screen, RANDOM, rect, 1)
                    pass
                elementNumber+=1
            rowNumber+=1