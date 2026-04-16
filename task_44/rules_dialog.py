from PySide6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout


class RulesDialog(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Правила")

        self.label_text = QLabel()
        self.label_text.setWordWrap(True)

        self.label_text.setText(text)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_text)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
