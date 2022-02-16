from random import random
from entity.entity import Entity

class Tree(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.__extra_factor: float = 0.0

    def add_extra_factor(self, factor):
        self.__extra_factor += factor

    def persistate_factors(self):
        self._base_factor = self._base_factor + self.__extra_factor
        self.__extra_factor = 0.0

    def plant_random(self, threshold=0.99):
        if random() > threshold:
            self._base_factor = 1.0

    def die_random(self, threshold=0.75):
        if random() > threshold:
            self._base_factor = 0.0
