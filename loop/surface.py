from typing import List

from ursina import Entity, color

from config.config import Config
from entity.cell import Cell
from util.types import Dimension
from random import randrange


class SurfaceLoop:
    def __init__(self, dim: Dimension):
        self.__dim = dim
        self.cellsize = Config.cellsize
        self.trees: List[Entity] = []
        # self.cells = [
        #    [Cell(x, y, self.cellsize) for y in range(self.__dim.y)]
        #    for x in range(self.__dim.x)
        # ]
        # self.set_cell_neighbors()
        self.build_trees()

    def set_cell_neighbors(self):
        for dimx in range(self.__dim.x):
            for dimy in range(self.__dim.y):
                cell = self.cells[dimx][dimy]
                neightbors = []
                neightbors_index = [
                    (dimx - 1, dimy),
                    (dimx + 1, dimy),
                    (dimx, dimy - 1),
                    (dimx, dimy + 1),
                    (dimx - 1, dimy - 1),
                    (dimx + 1, dimy - 1),
                    (dimx - 1, dimy + 1),
                    (dimx + 1, dimy + 1),
                ]

                for index in neightbors_index:
                    if (
                        index[0] >= 0
                        and index[0] < self.__dim.x
                        and index[1] >= 0
                        and index[1] < self.__dim.y
                    ):
                        neightbors.append(self.cells[index[0]][index[1]])

                cell.set_neighbors(neightbors)

    def build_trees(self):
        for _ in range(10):
            self.trees.append(
                Entity(
                    model="cube",
                    color=color.green,
                    scale=(1, 1, 3),
                    position=(
                        randrange(0, self.__dim.x),
                        randrange(0, self.__dim.y),
                        0,
                    ),
                )
            )

        # def forest():
        #    for dimx in range(self.__dim.x):
        #        for dimy in range(self.__dim.y):
        #            self.cells[dimx][dimy].try_plant_tree()


#
# def save():
#    for dimx in range(self.__dim.x):
#        for dimy in range(self.__dim.y):
#            self.cells[dimx][dimy].persistate()
#
# def die():
#    for dimx in range(self.__dim.x):
#        for dimy in range(self.__dim.y):
#            self.cells[dimx][dimy].get_tree().die_random()
#
# def plant():
#    for dimx in range(self.__dim.x):
#        for dimy in range(self.__dim.y):
#            self.cells[dimx][dimy].get_tree().plant_random()
#
# for run in range(6):
#    forest()
#    save()
# for run in range(3):
#    forest()
#    save()
#    plant()
#    die()
# for run in range(3):
#    forest()
#    save()
