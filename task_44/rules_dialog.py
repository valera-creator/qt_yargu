from PySide6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout, QScrollArea


class RulesDialog(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Правила")
        self.layout = QVBoxLayout()

        self.label_text = QLabel()
        self.label_text.setWordWrap(True)
        self.label_text.setText(text)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.label_text)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
