from abc import ABCMeta, abstractmethod
import os

class Block(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        # self.x = x
        # self.y = y
        self.cost = 0
        self.image = ""

    # instead of specifying a route to the image ("/images/...") where successful loading depends on the location within the code the file is being opened, 
    # transform the image path to an absolute one (C//Users//....) that can be used anywhere within the code successfully
    def transform_image_path(self, file):
        return os.path.realpath(file)
    
    # def get_x(self):
    #     return self.x

    # def get_y(self):
    #     return self.y

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def set_cost(self):
        pass

    @abstractmethod
    def get_image(self):
        pass