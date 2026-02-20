from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QGridLayout, QWidget


class University(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_university = QGridLayout()
        self.make_university_table()

    def make_university_table(self):
        # формат таблицы:
        # день недели, номер пары, числитель/знаменатель или нет разницы, пара первой группы, пара второй группы

        # если две пары не "-", то разные пары у первой и второй группы
        # если две пары одинаковые (не "-"), то объединённая
        # если один элемент "-", то пары нет у одной конкретной группы
        # если два элемента "-", то пар нет у обоих групп

        table = [
            ["День недели", "Номер пары", "Числ/Знам", "ИВТ-21", "ИВТ-22"],  # заголовок

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

        self.setLayout(self.layout_university)  # для того, чтобы создать вкладку нужен QWidget
