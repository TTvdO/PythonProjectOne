import os, pygame
from Tile import *

# ---------
# to be put in a seperate class for all constants later
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT

GRID_BLOCK_SIZE = 20
GRID_BLOCK_MARGIN = 5

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
# ---------

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(SIZE)

    SCREEN.fill(BLACK)

    # infinite loop for the program to run in until user exits program
    while 1:
        # draw the grid first, with x amount of rows and columns and with different type of terrain in the future, with their own amount of points to move over
        draw_grid(SCREEN)

        # monitor events
        for event in pygame.event.get():
            # exit when clicking on the X of the pop-up window
            if event.type == pygame.QUIT: os._exit(1)
        
        # update screen based on inputs
        pygame.display.flip()

def draw_grid(SCREEN):
    for row in range(SCREEN_WIDTH):
        for column in range(SCREEN_HEIGHT):
            rect = pygame.Rect(row * GRID_BLOCK_SIZE, column * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == '__main__':
    main()