import pygame

WHITE = 255, 255, 255

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns
        # self.grid = [[]]

        self.create_in_memory_grid()

        # unused for now
        # self.blockWidthAndHeight = self.roomPerBlock * 0.9
        # self.blockMarginLeft = self.roomPerBlock * 0.05
        # self.blockMarginRight = self.roomPerBlock * 0.05
    
    def create_in_memory_grid(self):
        # TOBECOME: instead of storing 0's in this grid, will be filled with classes. Can load the classes from a file or make it randomly generate integers that represent the classes
        # probably better to do the first option or think about other options
        self.grid = [[0 for x in range(self.rowsAndColumns)] for y in range(self.rowsAndColumns)]
        # print(self.grid)
        pass

    # TOCHANGE: should be based off of an existing grid that you can use in memory. not just a drawing based on nothing
    # also will need to update this grid after every change later on. can do this by calling draw_grid at the end of the while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid)
    def draw_grid(self, screen):
        # TOBECOME: for column in [columns of in_memory grid here]
        for column in range(self.rowsAndColumns):
            # TOBECOME: for row in [rows of in_memory grid here]
            for row in range(self.rowsAndColumns):
                # here the grid contents will be different, and you'll be looping through the in memory grid
                # you'll be able to do stuff here based on the type of class stored within the grid. (if type X, paint color blue. if type Y, paint color green)
                # and remember that this is just for visualization purposes, the actual logic will be done by using the in memory grid
                if self.grid[row][column] == 0:
                    rect = pygame.Rect(row * self.roomPerBlock, column * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                    pygame.draw.rect(screen, WHITE, rect, 1)

    # def draw_grid(self, screen):
    #     # TOBECOME: for column in [columns of in_memory grid here]
    #     for column in range(self.rowsAndColumns):
    #         # TOBECOME: for row in [rows of in_memory grid here]
    #         for row in range(self.rowsAndColumns):
    #             # here the grid contents will be different, and you'll be looping through the in memory grid
    #             # you'll be able to do stuff here based on the type of class stored within the grid. (if type X, paint color blue. if type Y, paint color green)
    #             # and remember that this is just for visualization purposes, the actual logic will be done by using the in memory grid
    #             rect = pygame.Rect(row * self.roomPerBlock, column * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
    #             pygame.draw.rect(screen, WHITE, rect, 1)

    def get_screen():
        return screen