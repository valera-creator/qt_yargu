from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QPen, QRadialGradient, QBrush, QColor
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.size_window = 600
        self.setFixedSize(self.size_window, self.size_window)
        self.setWindowTitle("Рисование фигур")

    def paintEvent(self, arg__0):
        painter = QPainter(self)
        margin_shapes = 10

        # треугольник
        pen_triangle = QPen()
        pen_triangle.setWidth(self.size_window // 85)
        pen_triangle.setColor(Qt.green)
        pen_triangle.setStyle(Qt.DotLine)
        painter.setPen(pen_triangle)
        painter.setBrush(Qt.cyan)

        x_left_triangle = self.width() // 3
        y_down_triangle = int(self.height() // 4.5)
        triangle_points = [
            QPoint(x_left_triangle + x_left_triangle // 2, 0),
            QPoint(x_left_triangle, y_down_triangle),
            QPoint(x_left_triangle * 2, y_down_triangle)
        ]
        painter.drawPolygon(triangle_points)

        # квадрат
        pen_square = QPen()
        pen_square.setWidth(self.size_window // 100)
        pen_square.setColor(Qt.red)
        pen_square.setStyle(Qt.DashDotLine)
        painter.setPen(pen_square)
        painter.setBrush(QColor("#FFA500"))

        square_size = min(self.width(), self.height()) // 3
        painter.drawRect(x_left_triangle, y_down_triangle + margin_shapes, square_size, square_size)

        # эллипс
        pen_ellipse = QPen()
        pen_ellipse.setWidth(self.size_window // 120)
        pen_ellipse.setColor(QColor("#00FF00"))
        painter.setPen(pen_ellipse)

        radius = square_size // 2
        y_ellips = (y_down_triangle + margin_shapes) + square_size // 2
        x_ellips = x_left_triangle - radius - margin_shapes // 4

        radial_gradient = QRadialGradient(x_ellips, y_ellips, radius)
        radial_gradient.setColorAt(0.0, Qt.white)
        radial_gradient.setColorAt(0.5, Qt.blue)
        radial_gradient.setColorAt(1.0, Qt.black)
        painter.setBrush(QBrush(radial_gradient))

        painter.drawEllipse(QPoint(x_ellips, y_ellips), radius - margin_shapes, radius)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
