from node_types.Node import Node
from Constants import Constants

class Ground(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.edge_cost = 1
        self.image = super().transform_image_path(Constants.GROUND_IMAGE)