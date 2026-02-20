import re
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QWidget, QFormLayout, QLineEdit, QCheckBox, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_form = QFormLayout()
        self.make_form_account()

    def validate_email(self):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$"
        email = self.email.text()
        return re.match(pattern, email)

    @Slot()
    def validate_form(self):
        """дописать все проверки"""
        text_error = ""
        if not self.surname.text().strip():
            text_error += "Отсутствует фамилия"
        elif not self.surname.text().strip().isalpha():
            text_error += "Неправильный ввод данных:\nНекорректная фамилия"
        if not self.name.text().strip():
            text_error += "\nОтсутствует имя"
        elif not self.name.text().strip().isalpha():
            text_error += "\nНекорректное имя"
        if not self.patronymic.text().strip():
            text_error += "\nОтсутствует информация про отчество"
        elif not self.patronymic.text().strip().isalpha():
            text_error += "\nНекорректное отчество"
        if not self.email.text().strip():
            text_error += "\nОтсутствует почта"
        elif not self.validate_email():
            text_error += "\nНекорректная почта"
        phone = self.phone.text().strip()
        if not phone:
            text_error += "\nОтсутствует телефон"
        elif len(phone) != 12 or phone[0] != "+" or not phone[1:].isdigit():
            text_error += "\nНекорректный телефон"
        if self.personal_data.checkState().value == 0:
            text_error += "\nВы должны быть согласны с обраткой персональных данных"

        text_error = text_error.lstrip()
        if not text_error:
            self.result_form.setText("Успешно!")
        else:
            self.result_form.setText(text_error)

    def make_form_account(self):
        self.surname = QLineEdit()
        self.layout_form.addRow("Фамилия:", self.surname)

        self.name = QLineEdit()
        self.layout_form.addRow("Имя:", self.name)

        self.patronymic = QLineEdit()
        self.patronymic.setPlaceholderText('При наличии, иначе укажите "нет"')
        self.layout_form.addRow("Отчество:", self.patronymic)

        self.email = QLineEdit()
        self.layout_form.addRow("Почта:", self.email)

        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Формат содержит + и только цифры (11 цифр)")  # подсказка пользователю
        self.layout_form.addRow("Телефон:\n", self.phone)

        self.layout_form.addRow(QLabel("Интересные темы: "))
        self.topics_game = QCheckBox("Игры")
        self.layout_form.addRow(self.topics_game)
        self.topics_swim = QCheckBox("Плавание")
        self.layout_form.addRow(self.topics_swim)
        self.topics_coding = QCheckBox("Программирование")
        self.layout_form.addRow(self.topics_coding)

        self.personal_data = QCheckBox("Согласие на обработку персональных данных")
        self.layout_form.addRow(self.personal_data)

        self.mailing_data = QCheckBox("Согласие на рассылку")
        self.layout_form.addRow(self.mailing_data)

        self.check_button = QPushButton("Проверить данные")
        self.check_button.clicked.connect(self.validate_form)
        self.layout_form.addRow(self.check_button)

        self.result_form = QLabel()
        self.layout_form.addRow(self.result_form)

        self.setLayout(self.layout_form)
