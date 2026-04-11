from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSequentialAnimationGroup
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1000)
        self.setMinimumHeight(600)
        self.setWindowTitle("Последовательная анимация виджетов")
        firstButton = QPushButton('Сначала еду я', self)
        firstAnim = QPropertyAnimation(firstButton, b"pos", self)
        firstAnim.setDuration(1000)
        firstAnim.setStartValue(QPoint(0, 0))
        firstAnim.setEndValue(QPoint(100, 250))
        firstAnim.setEasingCurve(QEasingCurve.InExpo)

        secondButton = QPushButton('А потом еду я', self)
        secondButton.move(QPoint(100, 250))
        secondAnim = QPropertyAnimation(secondButton, b"pos", self)
        secondAnim.setDuration(3000)
        secondAnim.setStartValue(QPoint(100, 250))
        secondAnim.setEndValue(QPoint(500, 500))
        secondAnim.setEasingCurve(QEasingCurve.OutBounce)

        sequenceAnim = QSequentialAnimationGroup(self)
        sequenceAnim.addAnimation(firstAnim)
        sequenceAnim.addAnimation(secondAnim)
        sequenceAnim.start()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
