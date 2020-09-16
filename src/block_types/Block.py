from abc import ABCMeta, abstractmethod
import os

class Block(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.block_cost = 0
        self.positional_cost = 0
        self.image = ""

    # instead of specifying a route to the image ("/images/...") where successful loading depends on the location within the code the file is being opened, 
    # transform the image path to an absolute one (C//Users//....) that can be used anywhere within the code successfully
    def transform_image_path(self, file):
        return os.path.realpath(file)
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_block_cost(self):
        return self.block_cost

    def set_block_cost(self, cost):
        self.block_cost = cost

    def get_positional_cost(self):
        return self.positional_cost

    def set_positional_cost(self, cost):
        self.positional_cost = cost

    def get_image(self):
        return self.image