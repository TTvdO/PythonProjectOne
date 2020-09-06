import os, pygame
from Tile import *
from Grid import *

# ---------
# to be put in a seperate class for all constants later
SCREEN_WIDTH_AND_HEIGHT = 500
SIZE = SCREEN_WIDTH_AND_HEIGHT, SCREEN_WIDTH_AND_HEIGHT

GRID_BLOCK_SIZE = 50
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
        grid = Grid(SCREEN_WIDTH_AND_HEIGHT, 10)
        grid.draw_grid_old(SCREEN)
        # grid.draw_grid_newer(SCREEN, GRID_BLOCK_SIZE)
        # draw_grid(SCREEN)

        # monitor events
        for event in pygame.event.get():
            # exit when clicking on the X of the pop-up window
            if event.type == pygame.QUIT: os._exit(1)
        
        # update screen based on inputs
        pygame.display.flip()

def draw_grid(SCREEN):
    # voor elke kolom, tot en met 240 pixels
    for column in range(SCREEN_WIDTH_AND_HEIGHT):
        # door de row van deze kolom heengaan, tot en met 320 pixels
        for row in range(SCREEN_WIDTH_AND_HEIGHT):
            # voor elk stukje van deze row een vierkant tekenen met als linkerbegin de 
            rect = pygame.Rect(column * GRID_BLOCK_SIZE, row * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == '__main__':
    main()