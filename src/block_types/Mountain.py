from block_types.Block import Block
from Constants import Constants

class Mountain(Block):
    def __init__(self):
        super().__init__()
        self.cost = 5
        self.image = super().transform_image_path(Constants.MOUNTAIN_IMAGE)