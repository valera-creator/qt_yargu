from task_1_model import MyModel
from PySide6.QtWidgets import QApplication, QListView, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")

        self.model = MyModel()
        self.main_layout = QVBoxLayout()

        self.view = QListView()
        self.view.setMinimumWidth(370)
        self.view.setModel(self.model)
        self.view.clicked.connect(self.delete_elem)
        self.main_layout.addWidget(self.view)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите сюда текст заметки")
        self.main_layout.addWidget(self.line_edit)

        self.button = QPushButton("Добавить заметку")
        self.main_layout.addWidget(self.button)
        self.button.clicked.connect(self.receive_text_to_model)

        self.label_result = QLabel()
        self.main_layout.addWidget(self.label_result)

        self.setLayout(self.main_layout)

    def receive_text_to_model(self):
        text = self.line_edit.text()
        if self.model.append_data(text):
            self.label_result.setText("Заметка успешно добавлена")
            self.line_edit.clear()
        else:
            self.label_result.setText("Ошибка добавления заметки: некорректный текст")

    def delete_elem(self, modelIndex):
        index_elem = modelIndex.row()
        res = self.model.removeRow(index_elem)
        if res:
            self.label_result.setText("Заметка успешно удалена")
        else:
            self.label_result.setText("Ошибка: заметка не была удалена")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    with open("task_1_style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    app.exec()
