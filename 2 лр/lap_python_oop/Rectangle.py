from lap_python_oop.FigureColor import FigureColor
from lap_python_oop.GeometricFigure import GeometricFigure
class Rectangle(GeometricFigure):
    # конструктор
    def __init__(self,width,height,color):
        self.width=width
        self.height=height
        # создание объекта класса Цвет фигуры для хранения цвета
        self.c=FigureColor()
        self.c.colorpr=color
    # переопределяем метод для вычесления площади
    def square (self):
       return self.width*self.height
    # название фишуры задаем в виде поля данных класса и возвращаем методом класса
    FIGURE_TYPE='Прямоугольник'
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    # метод возвращает основные параметры фигуры в виде строки
    def __repr__(self):
        return '{0} {1} цвета шириной {2} и высотой {3} площадью {4}'.format(
        Rectangle.get_figure_type(),
        self.c.colorpr,
        self.width,
        self.height,
        self.square()
        )







