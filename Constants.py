class Constants:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    RANDOM = 122, 155, 188

    SCREEN_WIDTH_AND_HEIGHT = 500
    SCREEN = SCREEN_WIDTH_AND_HEIGHT, SCREEN_WIDTH_AND_HEIGHT

    # based on which file the image is loaded in. Currently grid.py has the responsibility for this. In the future this will be changed
    END_IMAGE = "images/end.jpg"
    FOREST_IMAGE = "images/forest.jpg"
    GROUND_IMAGE = "images/ground.jpg"
    MOUNTAIN_IMAGE = "images/mountain.jpg"
    START_IMAGE = "images/start.jpg"

    def __init__(self):
        pass