from util.types import Dimension

class Config:
    dimension = Dimension(150, 150)
    creature_count: int = 150
    creature_die_age: int = 25
    creature_get_hungry: int = 19
    creature_age_rate: float = 0.1
    cellsize: int = 8
