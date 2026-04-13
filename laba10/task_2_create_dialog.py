from PySide6.QtCore import QFileInfo, QDir
from PySide6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QLabel, QDialogButtonBox
import re


class CreateDialog(QDialog):
    def __init__(self, parent_path):
        super().__init__()
        self.setWindowTitle("Создание каталога")
        self.setMinimumSize(300, 150)
        self.parent_path = parent_path
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(f"Создать папку в {self.parent_path}")
        self.label.setWordWrap(True)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Имя новой папки (без слешей)")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.reject)

        self.label_err = QLabel()
        self.label_err.setWordWrap(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.buttonBox)
        self.layout.addWidget(self.label_err)

    def name_new_directory(self):
        """Возвращает путь к новой директории"""
        return self.line_edit.text().strip()

    def check_exists(self):
        path = QFileInfo(self.parent_path).absoluteFilePath()
        return QFileInfo(path + QDir.separator() + self.line_edit.text()).exists()

    def on_accept(self):
        """проверка, директория является корректной"""
        text = self.line_edit.text()
        text = "".join(text.split())
        text = text.replace("ㅤ", "")
        forbidden = '<\\:?/"|*>'

        if not text:
            self.label_err.setText("Ошибка: введена пустая директория")
            return  # Не закрываем диалог
        elif re.search(r'[<>:"/\\|?*]', text):
            self.label_err.setText(f"Ошибка: введенная директория содержит запрещенные символы: {forbidden}")
            return  # Не закрываем диалог
        elif self.check_exists():
            self.label_err.setText("Ошибка: введенная директория уже существует")
            return
        else:
            self.accept()
