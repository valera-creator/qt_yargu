from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QCheckBox, QWidget


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Привет!")
        self.setMinimumWidth(250)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.apply_checkbox = QCheckBox("Соглашаюсь")

        self.layout = QVBoxLayout()
        self.message = QLabel("Сделайте выбор")
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.apply_checkbox)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

    def get_checkbox_state(self):
        """Возвращает состояние чекбокса"""
        return self.apply_checkbox.isChecked()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Согласие")
        self.setMinimumWidth(250)

        self.v_layout = QVBoxLayout()

        self.button = QPushButton("Открыть диалог")
        self.button.clicked.connect(self.button_clicked)
        self.v_layout.addWidget(self.button)

        self.res_label = QLabel()
        self.res_label.setWordWrap(True)
        self.v_layout.addWidget(self.res_label)

        self.widget = QWidget()
        self.widget.setLayout(self.v_layout)
        self.setCentralWidget(self.widget)
        self.setLayout(self.v_layout)

    def button_clicked(self):
        dlg = CustomDialog()
        if dlg.exec():
            is_checked = dlg.get_checkbox_state()
            if is_checked:
                self.res_label.setText("Чекбокс был выбран")
            else:
                self.res_label.setText("Чекбокс не был выбран")
        else:
            self.res_label.setText("Окно было закрыто без нажатия на \"ОК\"")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
