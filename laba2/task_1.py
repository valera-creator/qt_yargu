from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Нажата или отпущена")

        self.button = QPushButton("Нажать")
        self.button.pressed.connect(self.make_pressed_btn)
        self.button.released.connect(self.make_released_btn)

        central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.vertical_layout)

        self.text_label = QLabel("Отпущена")
        self.text_label.setAlignment(Qt.AlignCenter)

        self.vertical_layout.addWidget(self.text_label)
        self.vertical_layout.addWidget(self.button)

    def make_pressed_btn(self):
        self.text_label.setText("Нажата")

    def make_released_btn(self):
        self.text_label.setText("Отпущена")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
