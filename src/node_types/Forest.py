from node_types.Node import Node
from Constants import Constants

class Forest(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.edge_cost = 3
        self.image = super().transform_image_path(Constants.FOREST_IMAGE)