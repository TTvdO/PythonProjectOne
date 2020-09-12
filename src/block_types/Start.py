from block_types.Block import Block
from Constants import Constants

class Start(Block):
    def __init__(self):
        super().__init__()
        self.cost = 0
        self.image = super().transform_image_path(Constants.START_IMAGE)
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image