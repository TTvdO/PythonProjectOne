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
    
    def draw_grid(self):
        # TOCHANGE: i.p.v. op basis v.d. screenWidthAndHeight loopen, overgaan naar op basis v.d. opgegeven rowsAndColumns loopen
        for column in range(self.rowsAndColumns):
            # TOCHANGE: i.p.v. op basis v.d. screenWidthAndHeight loopen, overgaan naar op basis v.d. opgegeven rowsAndColumns loopen
            for row in range(self.rowsAndColumns):
                # hmm
                rect = pygame.Rect(row * self.roomPerBlock, column * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def draw_grid_old(self, screen):
        # TOCHANGE: i.p.v. op basis v.d. screenWidthAndHeight loopen, overgaan naar op basis v.d. opgegeven rowsAndColumns loopen
        for column in range(self.rowsAndColumns):
            # TOCHANGE: i.p.v. op basis v.d. screenWidthAndHeight loopen, overgaan naar op basis v.d. opgegeven rowsAndColumns loopen
            for row in range(self.rowsAndColumns):
                # hmm
                rect = pygame.Rect(row * self.roomPerBlock, column * self.roomPerBlock, self.roomPerBlock, self.roomPerBlock)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def draw_grid_older(self, SCREEN, GRID_BLOCK_SIZE):
        for column in range(self.screenWidthAndHeight):
            for row in range(self.screenWidthAndHeight):
                rect = pygame.Rect(column * GRID_BLOCK_SIZE, row * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

    def draw_grid_newer(self, SCREEN, GRID_BLOCK_SIZE):
        for column in range(self.rowsAndColumns):
            for row in range(self.rowsAndColumns):
                rect = pygame.Rect(row * GRID_BLOCK_SIZE, column * GRID_BLOCK_SIZE, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

    def get_screen():
        return screen