import os, pygame
from Grid import *
from Constants import Constants
from Draw import Draw
import queue
import time
from Run import Run

def main():
    # CHANGE THIS VARIABLE TO CHANGE THE ALGORITHM BEING RAN. OPTIONS:
    # -Constants.BFS
    # -Constants.DIJKSTRA
    # -Constants.ASTAR
    TO_RUN = Constants.ASTAR

    pygame.init()
    
    SCREEN = pygame.display.set_mode(Constants.SCREEN)
    SCREEN.fill(Constants.WHITE)

    grid = Grid(Constants.SCREEN_WIDTH_AND_HEIGHT, 10)
    draw = Draw(SCREEN, grid.get_grid(), grid.get_room_per_node())
    draw.draw_grid()
    pygame.display.flip()

    run = Run(grid, draw)

    if TO_RUN == Constants.BFS:
        run.run_bfs()
    elif TO_RUN == Constants.DIJKSTRA:
        run.run_dijkstra()
    elif TO_RUN == Constants.ASTAR:
        run.run_astar()

if __name__ == '__main__':
    main()