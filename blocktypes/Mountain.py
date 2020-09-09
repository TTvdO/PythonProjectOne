from blocktypes.Block import Block

class Mountain(Block):
    def __init__(self):
        super().__init__()
        self.cost = 5
        # image path is based on the location of loading the file. quite confusing, but the file is loaded within Grid.py, so teh path images/mountain.jpg is correct from there.
        self.image = "images/mountain.jpg"
    
    def get_cost(self):
        return self.cost

    def get_image(self):
        return self.image