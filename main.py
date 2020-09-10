import os, pygame
from Grid import *
from Constants import Constants

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(Constants.SIZE)

    SCREEN.fill(Constants.WHITE)

    grid = Grid(Constants.SCREEN_WIDTH_AND_HEIGHT, 10)
    grid.draw_grid(SCREEN)

    # infinite loop for the program to run in until user exits program
    while 1:
        # monitor events
        for event in pygame.event.get():
            # exit when clicking on the X of the pop-up window
            if event.type == pygame.QUIT: os._exit(1)

        # update screen based on inputs
        pygame.display.flip()

if __name__ == '__main__':
    main()