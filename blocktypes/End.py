from blocktypes.Block import Block

class End(Block):
    def __init__(self):
        super().__init__()
        self.cost = 10
        self.image = "images/end.jpg"
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image