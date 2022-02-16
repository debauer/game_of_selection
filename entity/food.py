from random import random

from ursina import Entity


class Food(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.age = 0

    def has_food(self):
        return self.is_alive()

    def grow_food(self, threshold=0.99):
        if random() > threshold:
            self._base_factor += 0.2

    def spoil_food(self):
        self.age += 1
        if self.age >= int(random() * 10000):
            self._base_factor -= 0.2
