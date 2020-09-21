import os, pygame
from Grid import *
from Constants import Constants
from Draw import Draw
from traversal_algorithms.BreadthFirstSearch import BreadthFirstSearch
from traversal_algorithms.Dijkstra import Dijkstra
import queue
import time
from Run import Run

def main():
    TO_RUN = Constants.DIJKSTRA

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

    # bfs = BreadthFirstSearch(grid, draw)

    # startOfTimer = time.perf_counter()
    # bfs.move()
    # endOfTimer = time.perf_counter()

    # print(f"the algorithm took {endOfTimer - startOfTimer:0.4f} seconds")
    # print(f"shortest path's cost: {bfs.get_lowest_cost()}")

    # time.sleep(50)

if __name__ == '__main__':
    main()