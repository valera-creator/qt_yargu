from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QWidget, QPushButton


class DragButton(QPushButton):
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec(Qt.MoveAction)


class Mouse(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)  # перетаскивание
        self.all_widgets = []

    def create_widget(self, x, y):
        btn = DragButton(f"Кнопка № {len(self.all_widgets) + 1}", self)
        btn.move(x, y)
        btn.show()  # отображение в процессе создания и добавления новых кнопок
        self.all_widgets.append(btn)

    def dragEnterEvent(self, event):
        """одноразовая проверка, что разрешено захватить виджет"""
        event.accept()

    def dragMoveEvent(self, event):
        """многоразовая проверка при смещении курсора, что разрешено захватить виджет"""
        event.accept()

    def mousePressEvent(self, event):
        if event.position().y() < self.height() / 2:  # если клик в верхней половине
            self.create_widget(event.position().x(), event.position().y())

    def dropEvent(self, event):
        pos = event.position()
        widget = event.source()

        # целиком за экран кнопку не убрать, поскольку на 2 делю widget.height() и widget.width()
        if (event.position().y() < self.height() / 2 or event.position().y() > self.height() - widget.height() / 2 or
                event.position().x() < 0 or event.position().x() > self.width() - widget.width() / 2):
            event.ignore()
        else:
            widget.move(pos.x(), pos.y())
