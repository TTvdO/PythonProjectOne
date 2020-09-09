from abc import ABCMeta, abstractmethod

class Block(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.cost = 0
        self.image = ""

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_image(self):
        pass