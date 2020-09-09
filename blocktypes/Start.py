from blocktypes.Block import Block

class Start(Block):
    def __init__(self):
        super().__init__()
        self.cost = 0
        self.image = "empty"
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image