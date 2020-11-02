class Constants:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    RANDOM = 122, 155, 188

    SCREEN_WIDTH_AND_HEIGHT = 500
    SCREEN = SCREEN_WIDTH_AND_HEIGHT, SCREEN_WIDTH_AND_HEIGHT

    # all image URLs get transformed within Node.py, so that the path is similar to "C//Users//...." instead of the format below
    END_IMAGE = "src/images/end.jpg"
    FOREST_IMAGE = "src/images/forest.jpg"
    GROUND_IMAGE = "src/images/ground.jpg"
    MOUNTAIN_IMAGE = "src/images/mountain.jpg"
    START_IMAGE = "src/images/start.png"

    GREEN_IMAGE = "src/images/green.jpg"
    RED_IMAGE = "src/images/red.jpg"
    BLACK_IMAGE = "src/images/black.jpg"

    BFS = "BFS"
    DIJKSTRA = "DIJKSTRA"
    ASTAR = "ASTAR"

    # CHANGE THIS TO_RUN VARIABLE TO CHANGE THE ALGORITHM BEING USED. 
    # OPTIONS:
    # -BFS
    # -DIJKSTRA
    # -ASTAR
    TO_RUN = BFS

    def __init__(self):
        pass

    def get_to_run(self):
        return TO_RUN