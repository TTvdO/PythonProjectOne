from block_types.Block import Block
from Constants import Constants

class End(Block):
    def __init__(self):
        super().__init__()
        self.cost = 10
        self.image = super().transform_image_path(Constants.END_IMAGE)