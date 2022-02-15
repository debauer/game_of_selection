
import pygame

from entity.cell import Cell

color_about_to_die = (200, 200, 225)
color_alive = (255, 255, 215)
color_background = (10, 10, 40)
color_grid = (30, 30, 60)


class SurfaceLoop:
    def __init__(self, dimx, dimy):
        self.__dimy = dimy
        self.__dimx = dimx
        self.cellsize = 9
        self.__surface = pygame.display.set_mode(
            (dimx * self.cellsize, dimy * self.cellsize)
        )
        self.cells = [
            [Cell(x, y, self.cellsize) for y in range(self.__dimy)]
            for x in range(self.__dimy)
        ]
        self.set_cell_neighbors()
        self.build_trees()
        
    def get_surface(self):
        return self.__surface

    def set_cell_neighbors(self):
        for dimx in range(self.__dimx):
            for dimy in range(self.__dimy):
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
                        index[0] > 0
                        and index[0] < self.__dimx
                        and index[1] > 0
                        and index[1] < self.__dimy
                    ):
                        neightbors.append(self.cells[index[0]][index[1]])
                cell.set_neighbors(neightbors)

    def build_trees(self):
        def forest():
            for dimx in range(self.__dimx):
                for dimy in range(self.__dimy):
                    self.cells[dimx][dimy].try_plant_tree()
        
        def save():
            for dimx in range(self.__dimx):
                for dimy in range(self.__dimy):
                    self.cells[dimx][dimy].persistate()
        
        def die():
            for dimx in range(self.__dimx):
                for dimy in range(self.__dimy):
                    self.cells[dimx][dimy].get_tree().die_random()      
     
        def plant():
            for dimx in range(self.__dimx):
                for dimy in range(self.__dimy):
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
        #for dimx in range(self.__dimx):
        #    for dimy in range(self.__dimy):
        #        food += self.cells[dimx][dimy].has_food()
        #        self.cells[dimx][dimy].tree_loop()

    def draw(self):
        self.__surface.fill(color_grid)
        for dimx in range(self.__dimx):
            for dimy in range(self.__dimy):
                cell = self.cells[dimx][dimy]
                pygame.draw.rect(self.__surface, cell.color(), cell.data())