from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Счётчик")
        self.value = 0

        self.button_plus = QPushButton("+1")
        self.button_plus.clicked.connect(self.make_plus)

        self.button_clear = QPushButton("Очистить")
        self.button_clear.clicked.connect(self.clear_value)

        # привязка к окну вертикального layout
        central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.vertical_layout)

        self.text_label = QLabel(f"Счётчик: {self.value}", self)
        self.text_label.setAlignment(Qt.AlignCenter)

        # в горизонтальный layout две кнопки
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.button_plus)
        self.horizontal_layout.addWidget(self.button_clear)

        # в вертикальный layout текст и горизонтальный layout
        self.vertical_layout.addWidget(self.text_label)
        self.vertical_layout.addLayout(self.horizontal_layout)

    def make_plus(self):
        self.value += 1
        self.text_label.setText(f"Счётчик: {self.value}")

    def clear_value(self):
        self.value = 0
        self.text_label.setText(f"Счётчик: {self.value}")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
