from blocktypes.Block import Block

class Mountain(Block):
    def __init__(self):
        super().__init__()
        self.cost = 5
        self.image = "../images/tile.jpg"
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image