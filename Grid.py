import pygame

WHITE = 255, 255, 255

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns

        self.create_in_memory_grid()

        # unused for now
        # self.blockWidthAndHeight = self.roomPerBlock * 0.9
        # self.blockMarginLeft = self.roomPerBlock * 0.05
        # self.blockMarginRight = self.roomPerBlock * 0.05
    
    def create_in_memory_grid(self):
        pass

    # TOCHANGE: should be based off of an existing grid that you can use in memory. not just a drawing based on nothing
    # also will need to update this grid after every change later on. can do this by calling draw_grid at the end of the while loop in main, but there should be a better way
    # to refresh only the parts of the grid that changed (without refreshing the entirety of the grid)
    def draw_grid(self, screen):
        for column in range(self.rowsAndColumns):
            for row in range(self.rowsAndColumns):
                rect = pygame.Rect(row * self.roomPerBlock, column * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def get_screen():
        return screen