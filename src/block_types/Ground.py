from block_types.Block import Block
from Constants import Constants

class Ground(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.block_cost = 1
        self.image = super().transform_image_path(Constants.GROUND_IMAGE)