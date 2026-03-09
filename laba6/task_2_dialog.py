from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QLineEdit


class CustomDialog(QDialog):
    def __init__(self, title="Взаимодействие с заметкой", note=None):
        super().__init__()

        self.setWindowTitle(title)
        self.setMinimumWidth(280)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.reject)

        self.line_edit = QLineEdit()
        if note is None:
            self.line_edit.setPlaceholderText("Введите текст заметки")
        else:
            self.line_edit.setText(note)

        self.label_err = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.buttonBox)
        self.layout.addWidget(self.label_err)

        self.setLayout(self.layout)

    def on_accept(self):
        """проверка, что заметка не пустая"""
        text = self.line_edit.text()
        text = "".join(text.split())
        text = text.replace("ㅤ", "")
        if not text:
            self.label_err.setText("Ошибка: заметка не может быть пустой")
            return  # Не закрываем диалог
        else:
            self.accept()

    def get_text(self):
        """Возвращает состояние чекбокса"""
        return self.line_edit.text().strip()
