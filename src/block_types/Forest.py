from block_types.Block import Block
from Constants import Constants

class Forest(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cost = 3
        self.image = super().transform_image_path(Constants.FOREST_IMAGE)