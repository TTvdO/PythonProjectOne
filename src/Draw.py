import pygame
from block_types import *
from block_types.Block import Block
from block_types.Forest import Forest
from block_types.Ground import Ground
from block_types.Mountain import Mountain
from block_types.Start import Start
from block_types.End import End
from Constants import Constants

class Draw:
    def __init__(self, screen, grid, roomPerBlock):
        self.screen = screen
        self.grid = grid
        self.roomPerBlock = roomPerBlock

    # also will need to update this grid after every change later on. can do this by calling draw_grid within while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid continuously)
    # or perhaps this will already be handled within main.py by just refreshing with pygame.display.flip() and perhaps this is the way to do it. unsure yet.
    def draw_grid(self):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                left = elementNumber * self.roomPerBlock
                top = rowNumber * self.roomPerBlock
                self.load_and_draw_block_img(element, (left, top))
                elementNumber+=1
            rowNumber+=1

    def load_and_draw_block_img(self, element, posXandYtuple):
        image = pygame.image.load(element.get_image())
        imageScaled = pygame.transform.scale(image, (int(self.roomPerBlock), int(self.roomPerBlock)))
        self.screen.blit(imageScaled, posXandYtuple)
        self.draw_text(posXandYtuple, f"{element.get_cost()}")

    # can be used to show what path you've taken in the future. (not used yet)
    def draw_green_image(self, posXandYtuple, totalCost):
        greenImage = pygame.image.load(Constants.GREEN_IMAGE)
        greenImageScaled = pygame.transform.scale(greenImage, (int(self.roomPerBlock), int(self.roomPerBlock)))
        self.screen.blit(greenImageScaled, posXandYtuple)
        # value "0101" to be replaced by future value "totalCost", which is going to be the sum of the costs of traversed blocks
        self.draw_text(posXandYtuple, f"{totalCost}")

    def draw_text(self, posXandYtuple, text):
        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerBlock / 3)))
        label = myfont.render(f"{text}", 0, Constants.RED)
        self.screen.blit(label, (posXandYtuple[0] + int(self.roomPerBlock / 2.5), posXandYtuple[1] + int(self.roomPerBlock / 4)))