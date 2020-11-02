import os, pygame
from Grid import *
from Constants import Constants
from Draw import Draw
import queue
import time
from Run import Run

def main():
    # CHANGE THE Constants.TO_RUN VARIABLE TO CHANGE THE ALGORITHM BEING RAN. OPTIONS:
    # BFS
    # DIJKSTRA
    # ASTAR
    algorithmToRun = Constants.TO_RUN

    pygame.init()
    
    SCREEN = pygame.display.set_mode(Constants.SCREEN)
    SCREEN.fill(Constants.WHITE)

    grid = Grid(Constants.SCREEN_WIDTH_AND_HEIGHT, 10)
    draw = Draw(SCREEN, grid.get_grid(), grid.get_room_per_node())
    draw.draw_grid()
    pygame.display.flip()

    run = Run(grid, draw)

    if algorithmToRun == Constants.BFS:
        run.run_bfs()
    elif algorithmToRun == Constants.DIJKSTRA:
        run.run_dijkstra()
    elif algorithmToRun == Constants.ASTAR:
        run.run_astar()
    else:
        run.run_bfs()

if __name__ == '__main__':
    main()