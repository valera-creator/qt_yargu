from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QCheckBox, QSpinBox


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продукты")
        self.setMinimumSize(300, 300)
        self.min_size_box = 120

        self.vertical_layout = QVBoxLayout()

        self.create_milk()
        self.create_bread()
        self.create_cheese()

        self.label_cost = QLabel("Текущая стоимость покупки: 0")
        self.vertical_layout.addWidget(self.label_cost)

        self.setLayout(self.vertical_layout)

    def create_milk(self):
        self.milk_horizontal_layout = QHBoxLayout()
        self.milk_cost = 100
        self.milk_checkbox = QCheckBox(f"Молоко ({self.milk_cost}/шт)")
        self.milk_checkbox.setMinimumSize(self.min_size_box, self.min_size_box)
        self.milk_spinbox = QSpinBox()
        self.milk_spinbox.setRange(0, 100)

        self.milk_checkbox.clicked.connect(self.clicked_milk)

        # размещение
        self.milk_horizontal_layout.addWidget(self.milk_checkbox)
        self.milk_horizontal_layout.addWidget(self.milk_spinbox)
        self.vertical_layout.addLayout(self.milk_horizontal_layout)

        # пересчёт цены после изменения хотя бы одной штуки
        self.milk_checkbox.stateChanged.connect(self.calculate_total)
        self.milk_spinbox.valueChanged.connect(self.calculate_total)

    def create_bread(self):
        self.bread_layout = QHBoxLayout()
        self.bread_cost = 50
        self.bread_checkbox = QCheckBox(f"Хлеб ({self.bread_cost}/шт)")
        self.bread_checkbox.setMinimumSize(self.min_size_box, self.min_size_box)
        self.bread_spinbox = QSpinBox()
        self.bread_spinbox.setRange(0, 100)

        self.bread_checkbox.clicked.connect(self.clicked_bread)

        # размещение
        self.bread_layout.addWidget(self.bread_checkbox)
        self.bread_layout.addWidget(self.bread_spinbox)
        self.vertical_layout.addLayout(self.bread_layout)

        # пересчёт цены после изменения хотя бы одной штуки
        self.bread_checkbox.stateChanged.connect(self.calculate_total)
        self.bread_spinbox.valueChanged.connect(self.calculate_total)

    def create_cheese(self):
        self.cheese_layout = QHBoxLayout()
        self.cheese_cost = 75
        self.cheese_checkbox = QCheckBox(f"Сыр ({self.cheese_cost}/шт)")
        self.cheese_checkbox.setMinimumSize(self.min_size_box, self.min_size_box)
        self.cheese_spinbox = QSpinBox()
        self.cheese_spinbox.setRange(0, 100)

        self.cheese_checkbox.clicked.connect(self.clicked_cheese)

        # размещение
        self.cheese_layout.addWidget(self.cheese_checkbox)
        self.cheese_layout.addWidget(self.cheese_spinbox)
        self.vertical_layout.addLayout(self.cheese_layout)

        # пересчёт цены после изменения хотя бы одной штуки
        self.cheese_checkbox.stateChanged.connect(self.calculate_total)
        self.cheese_spinbox.valueChanged.connect(self.calculate_total)

    def clicked_milk(self):
        value = self.milk_checkbox.checkState().value == 2  # значение 2 если выбран, 0 если не выбран
        font = self.milk_checkbox.font()
        font.setBold(value)  # в зависимости от выбранного значение переменная bool True или False
        self.milk_checkbox.setFont(font)

    def clicked_bread(self):
        value = self.bread_checkbox.checkState().value == 2  # значение 2 если выбран, 0 если не выбран
        font = self.bread_checkbox.font()
        font.setBold(value)  # в зависимости от выбранного значение переменная bool True или False
        self.bread_checkbox.setFont(font)

    def clicked_cheese(self):
        value = self.cheese_checkbox.checkState().value == 2  # значение 2 если выбран, 0 если не выбран
        font = self.cheese_checkbox.font()
        font.setBold(value)  # в зависимости от выбранного значение переменная bool True или False
        self.cheese_checkbox.setFont(font)

    def calculate_total(self):
        all_cost_milk = self.milk_cost * int(self.milk_checkbox.checkState().value == 2) * int(
            self.milk_spinbox.value())
        all_cost_bread = self.bread_cost * int(self.bread_checkbox.checkState().value == 2) * int(
            self.bread_spinbox.value())
        all_cost_cheese = self.cheese_cost * int(self.cheese_checkbox.checkState().value == 2) * int(
            self.cheese_spinbox.value())

        cur_cost = all_cost_milk + all_cost_bread + all_cost_cheese

        self.label_cost.setText(f"Текущая стоимость покупки: {cur_cost}")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
