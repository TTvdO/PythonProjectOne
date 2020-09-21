import pygame
from node_types import *
from node_types.Node import Node
from node_types.Forest import Forest
from node_types.Ground import Ground
from node_types.Mountain import Mountain
from node_types.Start import Start
from node_types.End import End
from Constants import Constants

class Draw:
    def __init__(self, screen, grid, roomPerNode):
        self.screen = screen
        self.grid = grid
        self.roomPerNode = roomPerNode

    def draw_grid(self):
        rowNumber = 0
        for row in self.grid:
            elementNumber = 0
            for element in row:
                left = elementNumber * self.roomPerNode
                top = rowNumber * self.roomPerNode
                self.draw_node_image(element.get_image(), Constants.RED, (left, top), element.get_edge_cost())
                elementNumber+=1
            rowNumber+=1

    def draw_node_image(self, imageUrl, textColor, posXandYtuple, edgeCost):
        self.draw_image(imageUrl, posXandYtuple)
        self.draw_text(textColor, posXandYtuple, f"{edgeCost}")

    def draw_colored_image(self, imageUrl, textColor, posXandYtuple, edgeCost, totalCost):
        self.draw_image(imageUrl, posXandYtuple)
        self.draw_text(textColor, posXandYtuple, f"{totalCost}")
        self.draw_text(textColor, (posXandYtuple[0] - int(self.roomPerNode / 8), posXandYtuple[1] + int(self.roomPerNode / 3)), f"({edgeCost})")

    def draw_colored_image_astar(self, imageUrl, textColor, posXandYtuple, gCost, hCost, fCost):
        self.draw_image(imageUrl, posXandYtuple)
        self.draw_text(textColor, (posXandYtuple[0], posXandYtuple[1] + int(self.roomPerNode / 4)), f"{fCost}")
        self.draw_text(textColor, (posXandYtuple[0] - int(self.roomPerNode / 3), posXandYtuple[1] - int(self.roomPerNode / 5)), f"({gCost})")
        self.draw_text(textColor, (posXandYtuple[0] + int(self.roomPerNode / 6), posXandYtuple[1] - int(self.roomPerNode / 5)), f"({hCost})")

    def draw_image(self, imageUrl, posXandYtuple):
        image = pygame.image.load(imageUrl)
        imageScaled = pygame.transform.scale(image, (int(self.roomPerNode), int(self.roomPerNode)))
        self.screen.blit(imageScaled, posXandYtuple)

    def draw_text(self, color, posXandYtuple, text):
        myfont = pygame.font.SysFont("Comic Sans MS", (int(self.roomPerNode / 3)))
        label = myfont.render(f"{text}", 0, color)
        self.screen.blit(label, (posXandYtuple[0] + int(self.roomPerNode / 2.5), posXandYtuple[1] + int(self.roomPerNode / 4)))