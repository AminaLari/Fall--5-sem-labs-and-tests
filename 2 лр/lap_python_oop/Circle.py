import math
from lap_python_oop.GeometricFigure import GeometricFigure
from lap_python_oop.FigureColor import FigureColor

class Circle(GeometricFigure):
    def __init__(self,radius,color):
        self.radius=radius
        self.c=FigureColor()
        self.c.colorpr=color
    def square(self):
        x=math.pow(self.radius,2)* math.pi
        return int(x)
    FIGURE_TYPE='Круг'
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    def __repr__(self):
        return '{0} {1} цвета радиусом {2} и площадью {3}'.format(
            Circle.get_figure_type(),
            self.c.colorpr,
            self.radius,
            self.square()
        )

