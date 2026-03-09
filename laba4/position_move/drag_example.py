from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag


class DragButton(QPushButton):
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec(Qt.MoveAction)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.layout = QHBoxLayout()
        for l in ['A', 'B', 'C', 'D']:
            btn = DragButton(l)
            self.layout.addWidget(btn)
        self.setLayout(self.layout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        for n in range(self.layout.count()):
            w = self.layout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2:
                self.layout.insertWidget(n-1, widget)
                break
        e.accept()


app = QApplication([])
w = Window()
w.show()
app.exec()
