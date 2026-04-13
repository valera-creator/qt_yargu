from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox


class DeleteDialog(QDialog):
    def __init__(self, cur_path):
        super().__init__()
        self.setWindowTitle("Удаление каталога")

        self.layout = QVBoxLayout()
        self.label = QLabel(f"Вы уверены, что хотите удалить {cur_path}?")
        self.label.setWordWrap(True)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
