import pygame

from config.config import Config
from util.color import color_grid
from entity.cell import Cell
from util.types import Dimension

class SurfaceLoop:
    def __init__(self, dim: Dimension):
        self.__dim = dim
        self.cellsize = Config.cellsize
        self.__surface = pygame.display.set_mode(
            (dim.x * self.cellsize, dim.y * self.cellsize)
        )
        self.cells = [
            [Cell(x, y, self.cellsize) for y in range(self.__dim.y)]
            for x in range(self.__dim.x)
        ]
        self.set_cell_neighbors()
        self.build_trees()

    def get_surface(self):
        return self.__surface

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
        def forest():
            for dimx in range(self.__dim.x):
                for dimy in range(self.__dim.y):
                    self.cells[dimx][dimy].try_plant_tree()

        def save():
            for dimx in range(self.__dim.x):
                for dimy in range(self.__dim.y):
                    self.cells[dimx][dimy].persistate()

        def die():
            for dimx in range(self.__dim.x):
                for dimy in range(self.__dim.y):
                    self.cells[dimx][dimy].get_tree().die_random()

        def plant():
            for dimx in range(self.__dim.x):
                for dimy in range(self.__dim.y):
                    self.cells[dimx][dimy].get_tree().plant_random()

        for run in range(6):
            forest()
            save()
        for run in range(3):
            forest()
            save()
            plant()
            die()
        for run in range(3):
            forest()
            save()

    def loop(self):
        food = 0
        # for dim.x in range(self.__dim.x):
        #    for dim.y in range(self.__dim.y):
        #        food += self.cells[dim.x][dim.y].has_food()
        #        self.cells[dim.x][dim.y].tree_loop()

    def draw(self):
        self.__surface.fill(color_grid)
        for dimx in range(self.__dim.x):
            for dimy in range(self.__dim.y):
                cell = self.cells[dimx][dimy]
                pygame.draw.rect(self.__surface, cell.color(), cell.data())
