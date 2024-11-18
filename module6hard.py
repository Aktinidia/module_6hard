import math
class Figure:
    sides_count = 0

    def __init__(self, *sides, color, filled=False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b,):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_values and valid_types

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def set_sides(self, *sides):
        if len(sides) == self.sides_count and self.__is_valid_sides(*sides):
            self.__sides = sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length, filled=False):
        __radius = self.lenght / (2*math.pi)

    def get_square(self):
        return math.pi * sqr(__radius)