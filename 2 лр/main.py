from lap_python_oop.Rectangle import Rectangle
from lap_python_oop.Circle import Circle
from lap_python_oop.Square import Square
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    rect= Rectangle(14,14,"синего")
    c=Circle(14,"зелёного")
    sq=Square(14,"красного")
    print(rect)
    print('\n')
    print(c)
    print('\n')
    print(sq)

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(350, 250)
    w.move(300, 300)
    w.setWindowTitle('Новое окошко')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
