import pygame

WHITE = 255, 255, 255

class Grid:
    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        self.roomPerBlock = self.screenWidthAndHeight / self.rowsAndColumns
        self.blockWidthAndHeight = self.roomPerBlock * 0.9
        self.blockMarginLeft = self.roomPerBlock * 0.05
        self.blockMarginRight = self.roomPerBlock * 0.05

        # self.draw_grid_old()

    def initialize_variables(self):
        pass

    def draw_grid(self):
        pass

    def draw_grid_old(self, screen):
        # voor elke kolom, tot en met 240 pixels
        for column in range(self.screenWidthAndHeight):
            # door de row van deze kolom heengaan, tot en met 320 pixels
            for row in range(self.screenWidthAndHeight):
                # voor elk stukje van deze row een vierkant tekenen met als linkerbegin de 
                rect = pygame.Rect(column * self.blockWidthAndHeight, row * self.blockWidthAndHeight, self.blockWidthAndHeight, self.blockWidthAndHeight)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def draw_grid_older(self, SCREEN, GRID_BLOCK_SIZE):
        # voor elke kolom, tot en met 240 pixels
        for column in range(self.screenWidthAndHeight):
            # door de row van deze kolom heengaan, tot en met 320 pixels
            for row in range(self.screenWidthAndHeight):
                # voor elk stukje van deze row een vierkant tekenen met als linkerbegin de 
                rect = pygame.Rect(column * GRID_BLOCK_SIZE, row * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

    def get_screen():
        return screen