from lap_python_oop.Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,side,color):
        self.side=side
        super().__init__(self.side,self.side,color)
    FIGURE_TYPE='Квадрат'
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    def __repr__(self):
        return '{0} {1} цвета со стороной {2}  и площадью {3}'.format(
            Square.get_figure_type(),
            self.c.colorpr,
            self.side,
            self.square()
        )
