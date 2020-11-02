from abc import ABCMeta, abstractmethod
import os
from Constants import Constants

class Node(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edge_cost = 0
        self.positional_cost = 0
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.image = ""
        self.visited = False
        self.predecessor_node = None

    def __lt__(self, other):
        # you want to change what this method does based on which algorithm is being ran.
        # so, put a getter in main method, use that getter in this method to get which constant is being used
        # then if constant_getter == Constants.ASTAR: ............
        # else: return self.edge_cost <= other.edge_cost
        # TODO: define how the comparison is done if algorithm used is AStar
        if Constants.TO_RUN == Constants.ASTAR:
            return self.h_cost <= other.h_cost
        else: # if DFS or Dijkstra are being ran, compare edge costs
            return self.edge_cost <= other.edge_cost

    # instead of specifying a route to the image ("/images/...") where successful loading depends on the location within the code the file is being opened, 
    # transform the image path to an absolute one (C//Users//....) that can be used anywhere within the code successfully
    def transform_image_path(self, file):
        return os.path.realpath(file)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_edge_cost(self):
        return self.edge_cost

    def set_edge_cost(self, cost):
        self.edge_cost = cost

    def get_current_positional_cost(self):
        return self.positional_cost

    def set_current_positional_cost(self, cost):
        self.positional_cost = cost

    def get_g_cost(self):
        return self.g_cost

    def set_g_cost(self, cost):
        self.g_cost = cost

    def get_h_cost(self):
        return self.h_cost

    def set_h_cost(self, cost):
        self.h_cost = cost

    def get_current_f_cost(self):
        return self.f_cost

    def set_f_cost(self, cost):
        self.f_cost = cost

    def get_image(self):
        return self.image

    def get_predecessor_node(self):
        return self.predecessor_node
    
    def set_predecessor_node(self, node):
        self.predecessor_node = node

    def get_visited(self):
        return self.visited
    
    def set_visited(self, trueOrFalse):
        self.visited = trueOrFalse