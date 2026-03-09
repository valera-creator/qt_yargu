from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример прокрутки")
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        layout = QVBoxLayout()
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap("landscape.jpg"))
        scrollArea = QScrollArea()
        scrollArea.setWidget(imageLabel)
        layout.addWidget(scrollArea)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
