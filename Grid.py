import pygame

WHITE = 255, 255, 255

class Grid:
    roomPerBlock = 0
    blockWidthAndHeight = 0
    blockMargin = 0

    def __init__(self, screenWidthAndHeight, rowsAndColumns):
        self.screenWidthAndHeight = screenWidthAndHeight
        self.rowsAndColumns = rowsAndColumns
        roomPerBlock = screenWidthAndHeight / rowsAndColumns
        blockWidthAndHeight = roomPerBlock * 0.9
        blockMargin = roomPerBlock * 0.1
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

    def draw_grid_older(self, SCREEN, SCREEN_WIDTH_AND_HEIGHT, GRID_BLOCK_SIZE, WHITE):
        # voor elke kolom, tot en met 240 pixels
        for column in range(SCREEN_WIDTH_AND_HEIGHT):
            # door de row van deze kolom heengaan, tot en met 320 pixels
            for row in range(SCREEN_WIDTH_AND_HEIGHT):
                # voor elk stukje van deze row een vierkant tekenen met als linkerbegin de 
                rect = pygame.Rect(column * GRID_BLOCK_SIZE, row * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
        # return SCREEN

    def get_screen():
        return screen