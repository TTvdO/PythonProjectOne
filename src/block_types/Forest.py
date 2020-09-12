from block_types.Block import Block
from Constants import Constants

class Forest(Block):
    def __init__(self):
        super().__init__()
        self.cost = 3
        self.image = super().transform_image_path(Constants.FOREST_IMAGE)