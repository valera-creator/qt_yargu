from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример формы")
        button1 = QPushButton("One")
        lineEdit1 = QLineEdit()
        button2 = QPushButton("Two")
        lineEdit2 = QLineEdit()
        button3 = QPushButton("Three")
        lineEdit3 = QLineEdit()
        layout = QFormLayout()
        layout.addRow(button1, lineEdit1)
        layout.addRow(button2, lineEdit2)
        layout.addRow(button3, lineEdit3)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
