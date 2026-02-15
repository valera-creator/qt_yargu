from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, \
    QLineEdit


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")

        # кнопки
        self.button_plus = QPushButton("+")
        self.button_plus.clicked.connect(self.make_plus)

        self.button_minus = QPushButton("-")
        self.button_minus.clicked.connect(self.make_minus)

        self.button_mul = QPushButton("*")
        self.button_mul.clicked.connect(self.make_mul)

        self.button_div = QPushButton(":")
        self.button_div.clicked.connect(self.make_div)

        self.button_degree = QPushButton("^")
        self.button_degree.clicked.connect(self.make_degree)

        # поля ввода целых чисел
        self.numLineEdit1 = QLineEdit()
        self.numLineEdit1.setPlaceholderText("Введите первое целое число")
        self.numLineEdit1.setFocus()  # курсор сюда
        self.numLineEdit1.setValidator(QIntValidator())

        self.numLineEdit2 = QLineEdit()
        self.numLineEdit2.setPlaceholderText("Введите второе целое число")
        self.numLineEdit2.setValidator(QIntValidator())

        # привязка к окну вертикального layout
        central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.vertical_layout)

        # label для текстового вывода
        self.text_label = QLabel(self)
        self.text_label.setAlignment(Qt.AlignCenter)

        # в горизонтальный layout две кнопки
        horizontal_layout_operation = QHBoxLayout()
        horizontal_layout_operation.addWidget(self.button_plus)
        horizontal_layout_operation.addWidget(self.button_minus)
        horizontal_layout_operation.addWidget(self.button_mul)
        horizontal_layout_operation.addWidget(self.button_div)

        # объединение в горизонтальный layout поле чисел
        horizontal_layout_nums = QHBoxLayout()
        horizontal_layout_nums.addWidget(self.numLineEdit1)
        horizontal_layout_nums.addWidget(self.numLineEdit2)

        # в вертикальный layout текст и горизонтальный layout
        self.vertical_layout.addWidget(self.text_label)
        self.vertical_layout.addLayout(horizontal_layout_nums)
        self.vertical_layout.addLayout(horizontal_layout_operation)
        self.vertical_layout.addWidget(self.button_degree)

    def check_correct(self, first, second):
        if not first:
            self.text_label.setText("поле ввода первого числа пустое")
            return False
        elif not second:
            self.text_label.setText("поле ввода второго числа пустое")
            return False
        try:
            first, second = int(first), int(second)
            return True
        except ValueError:
            self.text_label.setText("некорректный ввод, попробуйте еще раз")
            return False

    def make_plus(self):
        first_num = self.numLineEdit1.text()
        second_num = self.numLineEdit2.text()
        if self.check_correct(first_num, second_num):
            res = int(first_num) + int(second_num)
            if int(second_num) < 0:
                self.text_label.setText(f"Результат: {first_num} + ({second_num}) = {res}")
            else:
                self.text_label.setText(f"Результат: {first_num} + {second_num} = {res}")

    def make_minus(self):
        first_num = self.numLineEdit1.text()
        second_num = self.numLineEdit2.text()
        if self.check_correct(first_num, second_num):
            res = int(first_num) - int(second_num)
            if int(second_num) < 0:
                self.text_label.setText(f"Результат: {first_num} - ({second_num}) = {res}")
            else:
                self.text_label.setText(f"Результат: {first_num} - {second_num} = {res}")

    def make_mul(self):
        first_num = self.numLineEdit1.text()
        second_num = self.numLineEdit2.text()
        if self.check_correct(first_num, second_num):
            res = int(first_num) * int(second_num)
            if int(second_num) < 0:
                self.text_label.setText(f"Результат: {first_num} * ({second_num}) = {res}")
            else:
                self.text_label.setText(f"Результат: {first_num} * {second_num} = {res}")

    def make_div(self):
        first_num = self.numLineEdit1.text()
        second_num = self.numLineEdit2.text()
        if self.check_correct(first_num, second_num):
            second_num = int(second_num)
            if second_num == 0:
                self.text_label.setText("Ошибка: деление на 0")
                return
            else:
                res = round(int(first_num) / int(second_num), 3)
                if second_num < 0:
                    self.text_label.setText(f"Результат: {first_num} / ({second_num}) = {res}")
                else:
                    self.text_label.setText(f"Результат: {first_num} / {second_num} = {res}")

    def make_degree(self):
        first_num = self.numLineEdit1.text()
        second_num = self.numLineEdit2.text()
        if self.check_correct(first_num, second_num):
            res = round(int(first_num) ** int(second_num), 3)
            self.text_label.setText(f"Результат: {first_num}<sup>{second_num}</sup> = {res}")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
