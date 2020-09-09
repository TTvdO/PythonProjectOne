from blocktypes.Block import Block

class Forest(Block):
    def __init__(self):
        super().__init__()
        self.cost = 3
        self.image = "images/forest.png"
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image