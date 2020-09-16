from block_types.Block import Block
from Constants import Constants

class Start(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.block_cost = 0
        self.image = super().transform_image_path(Constants.START_IMAGE)