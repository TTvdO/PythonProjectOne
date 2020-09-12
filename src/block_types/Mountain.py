from block_types.Block import Block
from Constants import Constants

class Mountain(Block):
    def __init__(self):
        super().__init__()
        self.cost = 5
        self.image = super().transform_image_path(Constants.MOUNTAIN_IMAGE)
    
    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_image(self):
        return self.image