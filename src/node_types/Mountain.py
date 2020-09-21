from node_types.Node import Node
from Constants import Constants

class Mountain(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.edge_cost = 5
        self.image = super().transform_image_path(Constants.MOUNTAIN_IMAGE)