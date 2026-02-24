import re
from PySide6.QtCore import Slot, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
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
        if not self.name.text().strip():
            text_error += "\nОтсутствует имя"
        if not self.patronymic.text().strip():
            text_error += "\nОтсутствует информация про отчество"
        if not self.email.text().strip():
            text_error += "\nОтсутствует почта"
        elif not self.validate_email():
            text_error += "\nНекорректная почта"
        phone = self.phone.text().strip()
        if not phone:
            text_error += "\nОтсутствует телефон"
        else:
            pattern_phone = r"^(?:\+7|8)\d{10}$"
            if not re.match(pattern_phone, phone):
                text_error += "\nНекорректный телефон (введён не до конца)"
        if self.personal_data.checkState().value == 0:
            text_error += "\nВы должны быть согласны с обраткой персональных данных"

        text_error = text_error.lstrip()
        if not text_error:
            self.result_form.setText("Успешно!")
        else:
            self.result_form.setText(text_error)

    def make_form_account(self):
        surname_regex = QRegularExpression(r"^[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё\s\-]*$")
        self.surname = QLineEdit()
        self.surname.setPlaceholderText("Фамилия (с заглавной буквы)")
        self.surname.setValidator(QRegularExpressionValidator(surname_regex))
        self.layout_form.addRow("Фамилия:", self.surname)

        name_regex = QRegularExpression(r"^[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё\s\-]*$")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Имя (с заглавной буквы)")
        self.name.setValidator(QRegularExpressionValidator(name_regex))
        self.layout_form.addRow("Имя:", self.name)

        patronymic_regex = QRegularExpression(r"^(?:[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё\s\-]*|Нет)$")
        self.patronymic = QLineEdit()
        self.patronymic.setPlaceholderText('Отчество (с заглавной буквы) При наличии, иначе укажите "Нет"')
        self.patronymic.setValidator(QRegularExpressionValidator(patronymic_regex))
        self.layout_form.addRow("Отчество:", self.patronymic)

        email_regex = QRegularExpression(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$")
        self.email = QLineEdit()
        self.email.setPlaceholderText("Почта")
        self.email.setValidator(QRegularExpressionValidator(email_regex))
        self.layout_form.addRow("Почта:", self.email)

        phone_regex = QRegularExpression(r"^(?:\+7|8)\d{10}$")
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("+79991234567 или 89991234567")
        self.phone.setValidator(QRegularExpressionValidator(phone_regex))
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
