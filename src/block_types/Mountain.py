from block_types.Block import Block
from Constants import Constants

class Mountain(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 5
        self.image = super().transform_image_path(Constants.MOUNTAIN_IMAGE)