from blocktypes.Block import Block
from Constants import Constants

class End(Block):
    def __init__(self):
        super().__init__()
        self.cost = 10
        self.image = Constants.END_IMAGE
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image