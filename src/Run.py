from traversal_algorithms.BreadthFirstSearch import BreadthFirstSearch
from traversal_algorithms.Dijkstra import Dijkstra
from traversal_algorithms.AStar import AStar
import time

class Run:
    def __init__(self, grid, draw):
        self.grid = grid
        self.draw = draw

    def run_bfs(self):
        bfs = BreadthFirstSearch(self.grid, self.draw)

        startOfTimer = time.perf_counter()
        bfs.move()
        endOfTimer = time.perf_counter()

        print(f"the algorithm took {endOfTimer - startOfTimer:0.4f} seconds")
        print(f"shortest path's cost: {bfs.get_lowest_cost()}")

        time.sleep(50)

    def run_dijkstra(self):
        dijkstra = Dijkstra(self.grid, self.draw)

        startOfTimer = time.perf_counter()
        dijkstra.move()
        endOfTimer = time.perf_counter()

        print(f"the algorithm took {endOfTimer - startOfTimer:0.4f} seconds")
        print(f"shortest path's cost: {dijkstra.get_lowest_cost()}")

        time.sleep(50)

    def run_astar(self):
        astar = AStar(self.grid, self.draw)

        startOfTimer = time.perf_counter()
        astar.move()
        endOfTimer = time.perf_counter()

        print(f"the algorithm took {endOfTimer - startOfTimer:0.4f} seconds")
        print(f"shortest path's cost: {astar.get_lowest_cost()}")

        time.sleep(50)