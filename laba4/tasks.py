import re
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QTabWidget, QApplication, QLabel, QGridLayout, QWidget, QFormLayout, \
    QLineEdit, QCheckBox, QPushButton
from PySide6.QtGui import QDrag


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$"
    return re.match(pattern, email)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вкладки")

        self.tab = QTabWidget()

        # вкладка с расписанием
        self.university_tab_widget = QWidget()
        self.layout_university = QGridLayout()
        self.make_university_table()
        self.tab.addTab(self.university_tab_widget, "Расписание")

        # вкладка с формой
        self.form_account_widget = QWidget()
        self.layout_form = QFormLayout()
        self.make_form_account()
        self.tab.addTab(self.form_account_widget, "Форма")

        # вкладка с виджетом по клику
        self.widget_click_mouse = QWidget()
        self.make_widget_click_mouse()
        self.tab.addTab(self.widget_click_mouse, "Виджет по клику мыши")

        self.setCentralWidget(self.tab)

    def make_university_table(self):
        # формат таблицы:
        # день недели, номер пары, числитель/знаменатель или нет разницы, пара первой группы, пара второй группы

        # если две пары не "-", то разные пары у первой и второй группы
        # если две пары одинаковые (не "-"), то объединённая
        # если один элемент "-", то пары нет у одной конкретной группы
        # если два элемента "-", то пар нет у обоих групп

        table = [
            ["День недели", "Номер пары", "Числ/Знам", "ИВТ-21", "ИВТ-22"],
            ["Понедельник", "1", "Числитель", "-", "-"],
            ["Понедельник", "1", "Знаменатель", "-", "Англ яз пр 306"],
            ["Понедельник", "2", "Одинаково", "Диффуры пр 226", "Комплан пр 214"],
            ["Понедельник", "3", "Одинаково", "Питон ЭВМ пр 216", "Диффуры пр 226"],
            ["Понедельник", "4", "Одинаково", "-", "Питон ЭВМ пр 216"],

            [*[" "] * 5],  # пустая строка

            ["Вторник", "1", "Одинаково", "Диффуры лекция 312", "Диффуры лекция 312"],
            ["Вторник", "2", "Одинаково", "Питон ЭВМ лекция 220", "Питон ЭВМ лекция 220"],
            ["Вторник", "3", "Одинаково", "Комплан пр 219", "Тестирование пр 213"],
            ["Вторник", "4", "Одинаково", "Физика пр 203", "-"],
            ["Вторник", "5", "Числитель", "Физика пр 203", "-"],
            ["Вторник", "5", "Знаменатель", "-", "-"]
        ]

        for i in range(len(table)):
            for j in range(3):
                # первые 3 столбца
                self.layout_university.addWidget(QLabel(table[i][j], alignment=Qt.AlignCenter), i, j, 1, 1)

            # если двух пар нет, в каждой колонке по "-"
            if table[i][3] == "-" and table[i][4] == "-":
                self.layout_university.addWidget(QLabel("-", alignment=Qt.AlignCenter), i, 3)
                self.layout_university.addWidget(QLabel("-", alignment=Qt.AlignCenter), i, 4)

            # две пары объединены
            elif table[i][3] == table[i][4]:
                # i-ая строка, 3-столбец, 1 - сколько строк, 2 - сколько столбцов займет запись
                self.layout_university.addWidget(QLabel(table[i][3], alignment=Qt.AlignCenter), i, 3, 1, 2)
            # пары не равны
            elif table[i][3] != table[i][4]:
                self.layout_university.addWidget(QLabel(table[i][3], alignment=Qt.AlignCenter), i, 3, 1, 1)
                self.layout_university.addWidget(QLabel(table[i][4], alignment=Qt.AlignCenter), i, 4, 1, 1)

        self.layout_university.setColumnMinimumWidth(3, 140)
        self.layout_university.setColumnMinimumWidth(4, 140)

        self.university_tab_widget.setLayout(self.layout_university)  # для того, чтобы создать вкладку нужен QWidget

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
        elif not validate_email(self.email.text()):
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
        self.form_account_widget.setLayout(self.layout_form)

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

    def make_widget_click_mouse(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
