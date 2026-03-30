from PySide6.QtCore import Qt, Slot
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

    def get_text(self):
        login = self.field("login")
        password = self.field("password")
        surname = self.field("surname").strip()
        name = self.field("name").strip()
        patronymic = self.field("patronymic").strip() if self.field("patronymic").strip() else "не выбрано"
        topic_forest = "да" if self.field("topic_forest") else "нет"
        topic_coding = "да" if self.field("topic_coding") else "нет"
        topic_fish = "да" if self.field("topic_fish") else "нет"
        approval = "да" if self.field("approval") else "нет"

        s = (
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
        return s


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

    @Slot()
    def start_wizard(self):
        wizard = Wizard()
        if wizard.exec():
            self.result_label.setText(wizard.get_text())
        else:
            self.result_label.setText("Итог: текущая регистрация не завершилась")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
