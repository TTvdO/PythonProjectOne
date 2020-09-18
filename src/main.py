import os, pygame
from Grid import *
from Constants import Constants
from Draw import Draw
from traversal_algorithms.Dijkstra import Dijkstra
import queue
import time

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(Constants.SCREEN)
    SCREEN.fill(Constants.WHITE)

    grid = Grid(Constants.SCREEN_WIDTH_AND_HEIGHT, 10)
    draw = Draw(SCREEN, grid.get_grid(), grid.get_room_per_block())
    draw.draw_grid()
    pygame.display.flip()

    dijkstra = Dijkstra(grid, draw)

    startOfTimer = time.perf_counter()
    dijkstra.move()
    endOfTimer = time.perf_counter()

    print(f"the algorithm took {endOfTimer - startOfTimer:0.4f} seconds")
    print(f"shortest path's cost: {dijkstra.get_lowest_cost()}")

    time.sleep(50)

if __name__ == '__main__':
    main()