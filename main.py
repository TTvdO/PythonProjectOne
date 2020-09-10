import os, pygame
from Grid import *

# ---------
# to be put in a seperate class for all constants later
SCREEN_WIDTH_AND_HEIGHT = 500
SIZE = SCREEN_WIDTH_AND_HEIGHT, SCREEN_WIDTH_AND_HEIGHT

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
# ---------

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(SIZE)

    SCREEN.fill(WHITE)

    grid = Grid(SCREEN_WIDTH_AND_HEIGHT, 10)
    grid.draw_grid(SCREEN)

    # infinite loop for the program to run in until user exits program
    while 1:
        # monitor events
        for event in pygame.event.get():
            # exit when clicking on the X of the pop-up window
            if event.type == pygame.QUIT: os._exit(1)

            if event.type == pygame.KEYDOWN:
                # want to draw over the existing grid in the future while using the movement algorithm. Criteria:
                # - need to be able to access X and Y coordinates of different blocks, so that you can call this method to paint over specific blocks that you move over
                #       (this is functionality that belongs to movement algorithm implementations and shouldn't be implemented yet)
                grid.draw_green_image(SCREEN, (grid.get_room_per_block(), grid.get_room_per_block()))

        # update screen based on inputs
        pygame.display.flip()

if __name__ == '__main__':
    main()