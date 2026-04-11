from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QFont, QPainter, QPen, QPainterPath, QColor, QLinearGradient
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.setWindowTitle("Рисование пути")

    def paintEvent(self, arg__0):
        path = QPainterPath()
        path.addRect(20, 20, 60, 60)
        path.moveTo(0, 0)
        path.cubicTo(99, 0, 50, 50, 99, 99)
        path.cubicTo(0, 99, 50, 50, 0, 0)
        painter = QPainter(self)
        painter.fillRect(0, 0, 100, 100, Qt.white)
        painter.setPen(QPen(QColor(79, 106, 25), 1, Qt.SolidLine,
                            Qt.FlatCap, Qt.MiterJoin))
        painter.setBrush(QColor(122, 163, 39))
        painter.drawPath(path)

        myPath = QPainterPath()
        font = QFont("Times", 24, QFont.Bold)
        myPath.addText(QPointF(150, 150), font, "Qt")
        gradient = QLinearGradient(QPointF(150, 150), QPointF(200, 200))
        gradient.setColorAt(0.0, Qt.yellow)
        gradient.setColorAt(1.0, Qt.green)
        painter.setBrush(gradient)
        painter.setPen(QPen())
        painter.drawPath(myPath)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
