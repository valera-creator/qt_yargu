from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QWizard, QWizardPage, QLabel, QVBoxLayout, QPushButton, \
    QWidget, QLineEdit, QHBoxLayout, QCheckBox


def check_empty(text):
    text = "".join(text.split())
    text = text.replace("ㅤ", "")
    return True if text else False


class Wizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addPage(LoginPasswordPage())
        self.addPage(FIOPage())
        self.addPage(Themes())


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


class FIOPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("2 этап")
        max_length_line_edit = 40

        self.v_layout = QVBoxLayout()

        self.regex_fio = QRegularExpression(r"^[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё\s\-]*$")
        self.validator = QRegularExpressionValidator(self.regex_fio)

        self.surname_label = QLabel("Фамилия")
        self.surname_label.setMinimumWidth(60)
        self.surname_line_edit = QLineEdit()
        self.surname_line_edit.setPlaceholderText("Фамилия (с большой буквы)")
        self.surname_line_edit.setMaxLength(max_length_line_edit)
        self.surname_line_edit.setValidator(self.validator)

        self.surname_h_layout = QHBoxLayout()
        self.surname_h_layout.addWidget(self.surname_label)
        self.surname_h_layout.addWidget(self.surname_line_edit)
        self.v_layout.addLayout(self.surname_h_layout)

        self.name_label = QLabel("Имя")
        self.name_label.setMinimumWidth(60)
        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText("Имя (с большой буквы)")
        self.name_line_edit.setMaxLength(max_length_line_edit)
        self.name_line_edit.setValidator(self.validator)

        self.name_h_layout = QHBoxLayout()
        self.name_h_layout.addWidget(self.name_label)
        self.name_h_layout.addWidget(self.name_line_edit)
        self.v_layout.addLayout(self.name_h_layout)

        self.patronymic_label = QLabel("Отчество")
        self.patronymic_label.setMinimumWidth(60)
        self.patronymic_line_edit = QLineEdit()
        self.patronymic_line_edit.setPlaceholderText("Отчество (с большой буквы)")
        self.patronymic_line_edit.setMaxLength(max_length_line_edit)
        self.patronymic_line_edit.setValidator(self.validator)

        self.patronymic_h_layout = QHBoxLayout()
        self.patronymic_h_layout.addWidget(self.patronymic_label)
        self.patronymic_h_layout.addWidget(self.patronymic_line_edit)
        self.v_layout.addLayout(self.patronymic_h_layout)

        # добавление регистрационных полей, чтобы в главном окне получить значения
        self.registerField("surname", self.surname_line_edit, "text")
        self.registerField("name", self.name_line_edit, "text")
        self.registerField("patronymic", self.patronymic_line_edit, "text")

        # подключение отслеживание сигналов при изменении в полях ввода
        self.surname_line_edit.textChanged.connect(self.on_text_changed)
        self.name_line_edit.textChanged.connect(self.on_text_changed)
        self.patronymic_line_edit.textChanged.connect(self.on_text_changed)

        self.setLayout(self.v_layout)

    def on_text_changed(self):
        """сообщает Wizard, что нужно перепроверить isComplete(), вызывается после каждого изменения в полях ввода"""
        self.completeChanged.emit()

    def isComplete(self):
        """проверка, что поля фамилии и имени не пустые"""
        return check_empty(self.surname_line_edit.text()) and check_empty(self.name_line_edit.text())


class Themes(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("3 этап")

        self.label_text_hobbies = QLabel("Выберите увлечения")

        self.topics_forest = QCheckBox("Лесные походы")
        self.topics_coding = QCheckBox("Программирование")
        self.topics_fish = QCheckBox("Рыбалка")
        self.label_text_approval = QLabel("Выберите согласие/несогласие")
        self.approval = QCheckBox("Согласие на рассылку")

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label_text_hobbies)
        self.v_layout.addWidget(self.topics_forest)
        self.v_layout.addWidget(self.topics_coding)
        self.v_layout.addWidget(self.topics_fish)

        self.v_layout.addWidget(self.label_text_approval)
        self.v_layout.addWidget(self.approval)

        self.registerField("topic_forest", self.topics_forest, "checked")
        self.registerField("topic_coding", self.topics_coding, "checked")
        self.registerField("topic_fish", self.topics_fish, "checked")
        self.registerField("approval", self.approval, "checked")

        self.setLayout(self.v_layout)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setMinimumSize(350, 350)

        self.central_widget = QWidget()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.btn_start_wizard = QPushButton("Зарегистрироваться")
        self.btn_start_wizard.clicked.connect(self.start_wizard)
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.layout.addWidget(self.btn_start_wizard)
        self.layout.addWidget(self.result_label)
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def start_wizard(self):
        wizard = Wizard()
        if wizard.exec():
            login = wizard.field("login")
            password = wizard.field("password")
            surname = wizard.field("surname").strip()
            name = wizard.field("name").strip()
            patronymic = wizard.field("patronymic").strip() if wizard.field("patronymic").strip() else "не выбрано"
            topic_forest = "да" if wizard.field("topic_forest") else "нет"
            topic_coding = "да" if wizard.field("topic_coding") else "нет"
            topic_fish = "да" if wizard.field("topic_fish") else "нет"
            approval = "да" if wizard.field("approval") else "нет"

            self.result_label.setText(
                f"Вы ввели и выбрали:\n"
                f"Логин: {login};\n"
                f"Пароль: {password};\n"
                f"Фамилия: {surname};\n"
                f"Имя: {name};\n"
                f"Отчество: {patronymic};\n"
                f"Лесные походы: {topic_forest};\n"
                f"Программирование: {topic_coding};\n"
                f"Рыбалка: {topic_fish};\n"
                f"Согласие с рассылкой: {approval}"
            )
        else:
            self.result_label.setText("Итог: регистрация не завершилась")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
