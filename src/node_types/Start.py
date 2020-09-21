from node_types.Node import Node
from Constants import Constants

class Start(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.edge_cost = 0
        self.image = super().transform_image_path(Constants.START_IMAGE)