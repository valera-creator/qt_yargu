from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QPushButton, QLineEdit, QSpinBox, \
    QDoubleSpinBox, QHBoxLayout, QLabel
from task_2_model import TableModelProduct


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продукты")
        self.setMinimumSize(400, 500)

        self.model_product = TableModelProduct()
        self.main_layout = QVBoxLayout()

        self.view = QTableView()
        self.view.setMinimumWidth(340)
        self.view.setModel(self.model_product)
        self.main_layout.addWidget(self.view)

        self.regex_name = QRegularExpression(r"^[a-zA-Zа-яА-ЯёЁ\s]+$")
        self.validator_name = QRegularExpressionValidator(self.regex_name)
        self.name_input = QLineEdit()
        self.name_input.setValidator(self.validator_name)
        self.name_input.setPlaceholderText("Название продукта (ru/en)")

        self.cnt_input = QSpinBox()
        self.cnt_input.setRange(1, 100000)
        self.cnt_input.setValue(1)
        self.cnt_input.setMinimumWidth(65)

        self.weight_input = QDoubleSpinBox()
        self.weight_input.setRange(0.01, 10000.0)
        self.weight_input.setDecimals(3)
        self.weight_input.setSuffix(" кг")
        self.weight_input.setValue(0.5)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.name_input)
        self.horizontal_layout.addWidget(self.cnt_input)
        self.horizontal_layout.addWidget(self.weight_input)
        self.main_layout.addLayout(self.horizontal_layout)

        self.button = QPushButton("Добавить продукт")
        self.main_layout.addWidget(self.button)
        self.button.clicked.connect(self.action_click)

        self.summ_weight_label = QLabel()
        self.summ_weight_label.setText(f"Общая масса: {self.model_product.get_total_weight()} кг")
        self.main_layout.addWidget(self.summ_weight_label)

        self.err_label = QLabel()
        self.main_layout.addWidget(self.err_label)

        self.setLayout(self.main_layout)

    def action_click(self):
        res = self.model_product.append_data(self.name_input.text(), self.cnt_input.value(), self.weight_input.value())
        if res[0]:
            self.err_label.setText("Продукт успешно был добавлен")
            self.summ_weight_label.setText(f"Общая масса: {self.model_product.get_total_weight()} кг")
        else:
            self.err_label.setText(f"Ошибка добавления: {res[1]}")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
