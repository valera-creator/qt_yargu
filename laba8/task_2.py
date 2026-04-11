from PySide6.QtCore import QPropertyAnimation, QPoint, QParallelAnimationGroup
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.setWindowTitle("Параллельная анимация виджетов")

        self.make_animation()

    def make_animation(self):
        parallel_group_animation = QParallelAnimationGroup(self)

        # создание первой анимации
        first_widget = QWidget(self)
        first_widget.setObjectName("greenSquare")

        firstAnim = QPropertyAnimation(first_widget, b"pos", self)
        firstAnim.setDuration(3000)
        first_trajectory = [
            # пары вида: (доля от анимации, координаты)
            (0, QPoint(0, 0)),
            (0.3, QPoint(self.width() // 3, self.height() // 3)),
            (0.5, QPoint(self.width() // 3 * 2, int(self.height() // 1.2))),
            (0.7, QPoint(int(self.width() // 1.2), self.height() // 6)),
            (1.0, QPoint(0, 0))
        ]
        firstAnim.setKeyValues(first_trajectory)

        # создание второй анимации
        second_widget = QWidget(self)
        second_widget.setObjectName("BlueRect")

        secondAnim = QPropertyAnimation(second_widget, b"pos", self)
        secondAnim.setDuration(3000)
        second_trajectory = [
            # пары вида: (доля от анимации, координаты)
            (0, QPoint(second_widget.x(), self.height() // 2)),
            (0.3, QPoint(self.width() // 3 * 2, self.height() // 3)),
            (0.5, QPoint(0, 0)),
            (0.7, QPoint(self.width() // 6, self.height() // 3 * 2)),
            (1.0, QPoint(second_widget.x(), self.height() // 2))
        ]
        secondAnim.setKeyValues(second_trajectory)

        # добавление анимаций
        parallel_group_animation.addAnimation(firstAnim)
        parallel_group_animation.addAnimation(secondAnim)

        # запуск и зацикливание
        parallel_group_animation.setLoopCount(-1)
        parallel_group_animation.start()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    with open("task_2_style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    app.exec()
