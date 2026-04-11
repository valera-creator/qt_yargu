from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1000)
        self.setMinimumHeight(500)
        self.setWindowTitle("Анимация виджетов")
        button = QPushButton('Я еду по экспоненте', self)
        anim = QPropertyAnimation(button, b"pos", self)
        anim.setDuration(5000)
        anim.setStartValue(QPoint(0, 0))
        anim.setEndValue(QPoint(100, 250))
        anim.setEasingCurve(QEasingCurve.InExpo)
        anim.start()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
