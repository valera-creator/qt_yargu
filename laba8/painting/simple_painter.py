from PySide6.QtCore import Qt, QLineF
from PySide6.QtGui import QFont, QPainter, QPen, QRadialGradient, QBrush
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.setWindowTitle("Рисование фигур")

    def paintEvent(self, arg__0):
        painter = QPainter(self)
        painter.setPen(Qt.green)
        painter.drawLine(QLineF(50.0, 10.0, 10.0, 90.0))
        painter.drawLine(QLineF(50.0, 10.0, 90.0, 90.0))
        painter.drawLine(QLineF(10.0, 90.0, 90.0, 90.0))

        pen = QPen()
        pen.setStyle(Qt.DashDotLine)
        pen.setWidth(3)
        pen.setBrush(Qt.red)
        painter.setPen(pen)

        radial_gradient = QRadialGradient(100, 100, 50)
        radial_gradient.setColorAt(0.0, Qt.white)
        radial_gradient.setColorAt(0.2, Qt.green)
        radial_gradient.setColorAt(1.0, Qt.black)
        painter.setBrush(QBrush(radial_gradient))

        painter.drawRect(90, 90, 150, 150)

        painter.setPen(Qt.blue)
        painter.setFont(QFont("Arial", 30))
        painter.drawText(self.rect(), Qt.AlignCenter, "Qt")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
