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
        """Проверка при движении курсора с перетаскиваемым объектом"""
        if event.position().y() >= self.height() / 2:
            widget = event.source()
            if (event.position().y() + widget.height() <= self.height() and 0 <= event.position().x() and
                    event.position().x() + widget.width() <= self.width()):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if event.position().y() < self.height() / 2:  # если клик в верхней половине
            self.create_widget(event.position().x(), event.position().y())

    def dropEvent(self, event):
        pos = event.position()
        widget = event.source()

        # целиком за экран кнопку не убрать + в нижней половине экрана
        if (event.position().y() < self.height() / 2 and not (
                event.position().y() + widget.height() <= self.height() and 0 <= event.position().x() and
                event.position().x() + widget.width() <= self.width())):
            event.ignore()
        else:
            widget.move(pos.x(), pos.y())
