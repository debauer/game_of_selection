from random import random, randrange
from typing import List

import numpy as np
from ursina import Entity, color

from config.config import Config


class Trees():
    neightbors = [
                    (- 1,   0),
                    (+ 1,   0),
                    (  0, - 1),
                    (  0, + 1),
                    (- 1, - 1),
                    (+ 1, - 1),
                    (- 1, + 1),
                    (+ 1, + 1),
                ]
    
    
    def __init__(self):
        self.dim = Config.dimension
        self.trees: List[Entity] = []
        self.trees: List[Entity] = []
        self.pattern = np.zeros(self.dim)
        self.pattern_temp = np.zeros(self.dim)
        
        self.random_tree()
        for _ in range(7):
            self.search_neightbors()
        for _ in range(2):
            self.search_neightbors()
            self.random_tree()
            self.random_die()
        for _ in range(10):
            self.search_neightbors()
        self.random_die()
        self.plant_trees()
        
    def search_neightbors(self):
        print("search_neightbors")
        for x, value in enumerate(self.pattern):
            for z, value_inner in enumerate(value):
                for index in self.neightbors:
                    if (
                        index[0]+x >= 0
                        and index[0]+x < self.dim.x
                        and index[1]+z >= 0
                        and index[1]+z < self.dim.z
                    ):
                        if self.pattern[index[0]+x][index[1]+z] > 0.995:
                            self.pattern_temp[x][z] += 0.085
        self.pattern = np.add(self.pattern, self.pattern_temp)
        self.pattern_temp = np.zeros(self.dim)
        
    def random_tree(self):
        print("random_tree")
        for x, value in enumerate(self.pattern):
            for z, value_inner in enumerate(value):
                if random() > 0.99:
                    self.pattern[x][z] = 1.0

    def random_die(self):
        print("random_die")
        for x, value in enumerate(self.pattern):
            for z, value_inner in enumerate(value):
                if random() > 0.5:
                    self.pattern[x][z] = 0.0

    def plant_trees(self):
        print("plant_trees")
        for x, value in enumerate(self.pattern):
            for z, value_inner in enumerate(value):
                if value_inner > 0.995:
                    self.trees.append(Tree(x-self.dim.x/2,z-self.dim.z/2))
        
    for x in range(10):
        print(x)
        
class (Entity):
    def __init__(self, x, z, **kwargs):
        self.dim = Config.dimension
        super().__init__(model='cube', color=color.brown, scale=(0.7,2,0.7), position=(x,1,z),**kwargs)
        self.krone = Entity(model='cube', color=color.green, scale=(2,0.6,2), position=(0,0.7,0))
        self.krone.parent = self