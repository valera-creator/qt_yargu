from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout

from task_3_check_empty import check_empty


class LoginPasswordPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("1 этап")
        self.v_layout = QVBoxLayout()
        max_length_line_edit = 40

        self.login_label = QLabel("Логин")
        self.login_label.setMinimumWidth(60)
        self.login_line_edit = QLineEdit()
        self.login_line_edit.setPlaceholderText("Логин")
        self.login_line_edit.setMaxLength(max_length_line_edit)

        self.login_h_layout = QHBoxLayout()
        self.login_h_layout.addWidget(self.login_label)
        self.login_h_layout.addWidget(self.login_line_edit)

        self.password_label = QLabel("Пароль")
        self.password_label.setMinimumWidth(60)
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setPlaceholderText("Пароль")
        self.password_line_edit.setMaxLength(max_length_line_edit)

        self.password_h_layout = QHBoxLayout()
        self.password_h_layout.addWidget(self.password_label)
        self.password_h_layout.addWidget(self.password_line_edit)

        # подключение отслеживание сигналов при изменении в полях ввода
        self.login_line_edit.textChanged.connect(self.on_text_changed)
        self.password_line_edit.textChanged.connect(self.on_text_changed)

        # добавление регистрационных полей, чтобы в главном окне получить значения
        self.registerField("login", self.login_line_edit, "text")
        self.registerField("password", self.password_line_edit, "text")

        self.v_layout.addLayout(self.login_h_layout)
        self.v_layout.addLayout(self.password_h_layout)

        self.setLayout(self.v_layout)

    def on_text_changed(self):
        """сообщает Wizard, что нужно перепроверить isComplete(), вызывается после каждого изменения в полях ввода"""
        self.completeChanged.emit()

    def isComplete(self):
        """проверка, что поля логина и пароля не пустые"""
        return check_empty(self.login_line_edit.text()) and check_empty(self.password_line_edit.text())
