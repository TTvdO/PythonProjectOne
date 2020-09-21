from node_types.Node import Node
from Constants import Constants

class Barricade(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.traversable = False
        self.image = super().transform_image_path(Constants.BARRICADE_IMAGE)