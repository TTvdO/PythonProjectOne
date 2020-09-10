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
        self.hasStartingPoint = False
        self.hasEndPoint = False
        self.amountOfBlocksCreated = 0

        self.create_in_memory_grid()

    def create_in_memory_grid(self):
        self.grid = [[self.get_random_block() for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]

    def get_random_block(self):
        randomNumber = random.randrange(1, 5, 1)
        # Create starting point at the middle position or slightly before (depending on even or uneven amount of rows) if no starting point
        # has been created yet before then
        if (self.amountOfBlocksCreated >= (self.rowsAndColumns * (self.rowsAndColumns // 2))) and self.hasStartingPoint == False:
            block = Start()
            self.hasStartingPoint = True
        elif randomNumber == 1:
            block = Forest()
        elif randomNumber == 2:
            block = Ground()
        elif randomNumber == 3:
            block = Mountain()
        else:
            if self.hasStartingPoint == False:
                block = Start()
                self.hasStartingPoint = True
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
                #  rect = pygame.Rect(elementNumber * self.roomPerBlock, rowNumber * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)

                if type(element) is Ground:
                    # image = pygame.image.load(element.get_image())
                    # screen.blit(image, (left, top))
                    self.load_and_draw_block_img(screen, element, (left, top))
                elif type(element) is Forest:
                    self.load_and_draw_block_img(screen, element, (left, top))
                elif type(element) is Mountain:
                    self.load_and_draw_block_img(screen, element, (left, top))
                else: # type is Start
                    self.load_and_draw_block_img(screen, element, (left, top))
                    # self.draw_green_image(screen, (left, top))
                elementNumber+=1
            rowNumber+=1

    def load_and_draw_block_img(self, screen, element, posXandYtuple):
        image = pygame.image.load(element.get_image())
        imageScaled = pygame.transform.scale(image, (int(self.roomPerBlock), int(self.roomPerBlock)))
        screen.blit(imageScaled, posXandYtuple)

        # write text
        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerBlock / 3)))
        label = myfont.render(f"{element.get_cost()}", 0, RED)
        screen.blit(label, (posXandYtuple[0] + int(self.roomPerBlock / 2.5), posXandYtuple[1] + int(self.roomPerBlock / 4)))
        # screen.blit(label, (self.roomPerBlock // 5 + int(posXandYtuple[0])), (self.roomPerBlock // 5 + int(posXandYtuple[1])))

    # can be used to show what path you've taken in the future. might be replaced with another way of doing it, but for now
    # just draw a green image over the existing image. will call this method when moving with any movement algorithm
    def draw_green_image(self, screen, posXandYtuple):
        greenImage = pygame.image.load("images/green.jpg")
        greenImageScaled = pygame.transform.scale(greenImage, (int(self.roomPerBlock), int(self.roomPerBlock)))
        screen.blit(greenImageScaled, posXandYtuple)

        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerBlock / 3)))
        label = myfont.render(f"{1}", 0, RED)
        screen.blit(label, (posXandYtuple[0] + int(self.roomPerBlock / 2.5), posXandYtuple[1] + int(self.roomPerBlock / 4)))

    def get_room_per_block(self):
        return self.roomPerBlock