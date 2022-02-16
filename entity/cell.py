from typing import List

from entity.food import Food
from entity.tree import Tree


class Cell:
    __tree_threshold = 0.95
    __neighbors: List["Cell"] = []

    def __init__(self, posx, posy, cellsize):
        self.__posy = posy
        self.__posx = posx
        self.__cellsize = cellsize
        self.__tree = Tree()
        self.__food = Food()
        self._loop_count = 0

    def set_neighbors(self, neighbors: List["Cell"]):
        self.__neighbors = neighbors

    def get_tree(self):
        return self.__tree

    def is_tree(self):
        return self.__tree.is_alive()

    def chop_wood(self):
        self.__tree.die_random(0.99)
        return not self.is_tree()

    def make_poo(self):
        self.__tree.plant_random(0.997)

    def has_food(self):
        return self.__food.has_food()

    def color(self):
        if self.is_tree():
            return (10, 120, 10)
        if self.has_food():
            return (200, 140, 100)
        return (250, 235, 220)

    def try_plant_tree(self):
        for neightbor in self.__neighbors:
            if neightbor.is_tree():
                self.__tree.add_extra_factor(0.085)

    def tree_loop(self):
        if self._loop_count > 1:
            self.__tree.die_random(0.9999)
            self.__tree.plant_random(0.9999)
            self._loop_count = 0
        self._loop_count += 1

    def food_loop(self, food_count):
        if self._loop_count > 1:
            self.__food.grow_food(0.999)
            self.__food.spoil_food()
            self._loop_count = 0
        self._loop_count += 1

    def persistate(self):
        self.__tree.persistate_factors()

    def data(self):
        return (
            self.__posx * self.__cellsize,
            self.__posy * self.__cellsize,
            self.__cellsize - 1,
            self.__cellsize - 1,
        )
