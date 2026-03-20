from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWizard, QLabel, QVBoxLayout, QPushButton, QWidget

from task_3_page_login_password import LoginPasswordPage
from task_3_page_fio import FIOPage
from task_3_page_themes import Themes


class Wizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addPage(LoginPasswordPage())
        self.addPage(FIOPage())
        self.addPage(Themes())


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
            self.result_label.setText("Итог: текущая регистрация не завершилась")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
