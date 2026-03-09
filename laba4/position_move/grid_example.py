from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QTextEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример таблицы")
        layout = QGridLayout()
        layout.addWidget(QLabel('Первая ячейка'), 0, 0)
        layout.addWidget(QLabel('Вторая ячейка'), 0, 1)
        layout.addWidget(QLabel('Длиииииииинный текст на две ячейки'), 1, 0, 1, 2)
        layout.addWidget(QLabel('Нижняя левая'), 2, 0)
        layout.addWidget(QLabel('Нижняя правая'), 2, 1)
        # layout = QGridLayout()
        # for i in range(4):
        #     label = QLabel(f"Line {i + 1}:")
        #     line_edit = QLineEdit()
        #     layout.addWidget(label, i, 0)
        #     layout.addWidget(line_edit, i, 1)
        # small_editor = QTextEdit()
        # small_editor.setPlainText("Этот виджет занимает около 2/3 сетки.")
        # layout.addWidget(small_editor, 0, 3, 4, 1)
        #
        # layout.setColumnStretch(1, 10)
        # layout.setColumnStretch(2, 5)
        # layout.setColumnStretch(3, 20)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
