from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QCheckBox, QSpinBox


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продукты")
        self.setMinimumSize(400, 400)
        self.min_size_box = 55
        self.max_products = 100
        self.main_vertical_layout = QVBoxLayout()

        self.products = []  # список картежей вида (цена, название, checkbox с галочкой, spinbox с количеством)
        self.create_product("Молоко", 100)
        self.create_product("Хлеб", 50)
        self.create_product("Сыр", 75)
        self.create_product("Шампанское", 550)

        self.label_cost = QLabel("Текущая стоимость покупки: 0")
        self.main_vertical_layout.addWidget(self.label_cost)

        self.setLayout(self.main_vertical_layout)

    def create_product(self, name, cost):
        horizontal_layout = QHBoxLayout()

        checkbox = QCheckBox(f"{name} ({cost}/шт)")
        checkbox.setMinimumSize(self.min_size_box, self.min_size_box)

        spinbox = QSpinBox()
        spinbox.setRange(0, self.max_products)

        checkbox.clicked.connect(self.clicked_chebox)

        # размещение
        horizontal_layout.addWidget(checkbox)
        horizontal_layout.addWidget(spinbox)
        self.main_vertical_layout.addLayout(horizontal_layout)

        # пересчёт цены после изменения хотя бы одной штуки
        checkbox.stateChanged.connect(self.calculate_total)
        spinbox.valueChanged.connect(self.calculate_total)

        self.products.append((cost, name, checkbox, spinbox))

    def clicked_chebox(self):
        cur_product = self.sender()  # текущий элемент checkbox, с которого было нажато
        value = cur_product.checkState().value == 2  # значение 2 если выбран, 0 если не выбран

        font = cur_product.font()
        font.setBold(value)  # в зависимости от выбранного значение переменная bool True или False
        cur_product.setFont(font)

    def calculate_total(self):
        cur_cost_products = 0
        text = ""
        for elem in self.products:
            cost, name, checkbox, spinbox = elem[0], elem[1], elem[2], elem[3]

            if int(spinbox.value()) != 0 and checkbox.checkState().value == 2:  # если продукт выбран
                text += f"{name}: {cost} * {int(spinbox.value())} = {cost * int(spinbox.value())}\n"

            cur_cost_products += cost * int(checkbox.checkState().value == 2) * int(spinbox.value())
        self.label_cost.setText(f"{text}Текущая стоимость покупки: {cur_cost_products}")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
