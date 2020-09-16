from block_types.Block import Block
from Constants import Constants

class End(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.block_cost = 10
        self.image = super().transform_image_path(Constants.END_IMAGE)