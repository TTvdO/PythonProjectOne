from abc import ABCMeta, abstractmethod

class Block(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.cost = 0
        # image path is based on the location of loading the file. For now it's only being loaded within Grid.py, so the paths within Constants.py are fine
        # in the future, change it
        self.image = ""

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_image(self):
        pass