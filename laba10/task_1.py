from PySide6.QtCore import Slot, QDir, QFileInfo, Qt
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Диалог")
        self.setFixedSize(500, 500)
        self.v_layout = QVBoxLayout()

        self.text_label = QLabel()
        self.text_label.setWordWrap(True)
        self.btn = QPushButton("Выбрать файл")
        self.btn.pressed.connect(self.start_dialog)

        self.v_layout.addWidget(self.btn)
        self.v_layout.addWidget(self.text_label)
        self.v_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.setLayout(self.v_layout)

    def set_text_file_to_label(self, file_path):
        file = QFileInfo(file_path)
        abs_path = file.absoluteFilePath()
        base_name = file.baseName()
        is_read = file.isReadable()
        is_write = file.isWritable()
        is_executable = file.isExecutable()
        date_create = file.birthTime()
        date_edit = file.lastModified()

        if file.exists():
            text = (f"Абсолютный путь: {abs_path};\n"
                    f"Базовое имя: {base_name};\n"
                    f"Можно ли файл читать: {'да' if is_read else 'нет'};\n"
                    f"Можно ли в файл писать: {'да' if is_write else 'нет'};\n"
                    f"Является ли файл исполняемым: {'да' if is_executable else 'нет'};\n"
                    f"Когда файл был создан: {date_create.toString('dd.MM.yyyy в HH:mm:ss')};\n"
                    f"Когда файл был изменён: {date_edit.toString('dd.MM.yyyy в HH:mm:ss')}\n")

            self.text_label.setText(text)
        else:
            self.text_label.setText("Файл не выбран или не существует")

    @Slot()
    def start_dialog(self):
        data = QFileDialog.getOpenFileName(self, "путь к csv", str(QDir.currentPath()), "csv (*.csv)")
        file_path, _ = data
        self.set_text_file_to_label(file_path)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
