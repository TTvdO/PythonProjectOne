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

    def draw_grid(self):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                left = elementNumber * self.roomPerBlock
                top = rowNumber * self.roomPerBlock
                self.draw_block_image(element.get_image(), Constants.RED, (left, top), element.get_block_cost())
                elementNumber+=1
            rowNumber+=1

    def draw_block_image(self, imageUrl, textColor, posXandYtuple, blockCost):
        self.draw_image(imageUrl, posXandYtuple)
        self.draw_text(textColor, posXandYtuple, f"{blockCost}")

    def draw_colored_image(self, imageUrl, textColor, posXandYtuple, blockCost, totalCost):
        self.draw_image(imageUrl, posXandYtuple)
        self.draw_text(textColor, posXandYtuple, f"{totalCost}")
        self.draw_text(textColor, (posXandYtuple[0] - int(self.roomPerBlock / 8), posXandYtuple[1] + int(self.roomPerBlock / 3)), f"({blockCost})")

    def draw_image(self, imageUrl, posXandYtuple):
        image = pygame.image.load(imageUrl)
        imageScaled = pygame.transform.scale(image, (int(self.roomPerBlock), int(self.roomPerBlock)))
        self.screen.blit(imageScaled, posXandYtuple)

    def draw_text(self, color, posXandYtuple, text):
        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerBlock / 3)))
        label = myfont.render(f"{text}", 0, color)
        self.screen.blit(label, (posXandYtuple[0] + int(self.roomPerBlock / 2.5), posXandYtuple[1] + int(self.roomPerBlock / 4)))