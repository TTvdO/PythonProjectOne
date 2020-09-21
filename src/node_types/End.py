from node_types.Node import Node
from Constants import Constants

class End(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.edge_cost = 10
        self.image = super().transform_image_path(Constants.END_IMAGE)