from blocktypes.Block import Block
from Constants import Constants

class Ground(Block):
    def __init__(self):
        super().__init__()
        self.cost = 1
        self.image = Constants.GROUND_IMAGE
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image