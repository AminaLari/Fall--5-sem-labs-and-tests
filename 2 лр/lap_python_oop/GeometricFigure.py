from abc import ABC,abstractmethod
class GeometricFigure(ABC):
    # абстрактный метод для вычисления площади фигуры
    @abstractmethod
    def square(self):
        pass