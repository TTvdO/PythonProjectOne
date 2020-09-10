import pygame
import random
from blocktypes import *
from blocktypes.Block import Block
from blocktypes.Forest import Forest
from blocktypes.Ground import Ground
from blocktypes.Mountain import Mountain
from blocktypes.Start import Start
from blocktypes.End import End
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
        self.grid = [[self.get_random_block() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    def get_random_block(self):
        randomNumber = random.randrange(1, 48, 1)
        # Create starting point at the middle position or slightly before (depending on even or uneven amount of rows) if no starting point
        # has been created yet before then
        if (self.amountOfBlocksCreated == ((self.rowsAndColumns * self.rowsAndColumns) - 2)) and self.hasStartingPoint == False:
            block = Start()
            self.hasStartingPoint = True
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
        return block

    # also will need to update this grid after every change later on. can do this by calling draw_grid within while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid continuously)
    # or perhaps this will already be handled within main.py by just refreshing with pygame.display.flip() and perhaps this is the way to do it. unsure yet.
    def draw_grid(self, screen):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                left = elementNumber * self.roomPerBlock
                top = rowNumber * self.roomPerBlock

                if type(element) is Ground:
                    self.load_and_draw_block_img(screen, element, (left, top))
                elif type(element) is Forest:
                    self.load_and_draw_block_img(screen, element, (left, top))
                elif type(element) is Mountain:
                    self.load_and_draw_block_img(screen, element, (left, top))
                elif type(element) is Start:
                    self.load_and_draw_block_img(screen, element, (left, top))
                else: # type is End
                    self.load_and_draw_block_img(screen, element, (left, top))
                elementNumber+=1
            rowNumber+=1

    def load_and_draw_block_img(self, screen, element, posXandYtuple):
        image = pygame.image.load(element.get_image())
        imageScaled = pygame.transform.scale(image, (int(self.roomPerBlock), int(self.roomPerBlock)))
        screen.blit(imageScaled, posXandYtuple)
        self.draw_text(screen, posXandYtuple, f"{element.get_cost()}")

    # can be used to show what path you've taken in the future.
    def draw_green_image(self, screen, posXandYtuple):
        greenImage = pygame.image.load("images/green.jpg")
        greenImageScaled = pygame.transform.scale(greenImage, (int(self.roomPerBlock), int(self.roomPerBlock)))
        screen.blit(greenImageScaled, posXandYtuple)
        # value "0101" to be replaced by future value "totalCost", which is going to be the sum of the costs of traversed blocks
        self.draw_text(screen, posXandYtuple, "0101")

    def draw_text(self, screen, posXandYtuple, text):
        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerBlock / 3)))
        label = myfont.render(f"{text}", 0, Constants.RED)
        screen.blit(label, (posXandYtuple[0] + int(self.roomPerBlock / 2.5), posXandYtuple[1] + int(self.roomPerBlock / 4)))

    def get_room_per_block(self):
        return self.roomPerBlock