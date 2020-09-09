import pygame
import random
from blocktypes import *
from blocktypes.Block import Block
from blocktypes.Forest import Forest
from blocktypes.Ground import Ground
from blocktypes.Mountain import Mountain
from blocktypes.Start import Start

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
        self.grid = [[self.get_random_block() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    # def create_in_memory_grid(self):
    #     self.grid = [[Mountain() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]
    #     # self.create_in_memory_grid_two()

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
    # or perhaps this will already be handled within main.py by just refreshing with pygame.display.flip()
    def draw_grid(self, screen):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                left = elementNumber * self.roomPerBlock
                top = rowNumber * self.roomPerBlock
                # rect = pygame.Rect(elementNumber * self.roomPerBlock, rowNumber * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)

                if type(element) is int:
                    pygame.draw.rect(screen, BLACK, rect, 1)
                elif type(element) is Ground:
                    image = pygame.image.load(element.get_image())
                    screen.blit(image, (left, top))
                elif type(element) is Forest:
                    image = pygame.image.load(element.get_image())
                    screen.blit(image, (left, top))
                elif type(element) is Mountain:
                    image = pygame.image.load(element.get_image())
                    screen.blit(image, (left, top))
                else: # type is Start
                    image = pygame.image.load(element.get_image())
                    screen.blit(image, (left, top))
                elementNumber+=1
            rowNumber+=1