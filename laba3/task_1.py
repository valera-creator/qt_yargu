from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QWidget


class Window(QWidget):

    def handle_radio_buttons(self):
        if self.group.checkedId() == 1:
            self.label_text.setText(self.winter_text)
        elif self.group.checkedId() == 2:
            self.label_text.setText(self.spring_text)
        elif self.group.checkedId() == 3:
            self.label_text.setText(self.summer_text)
        elif self.group.checkedId() == 4:
            self.label_text.setText(self.autumn_text)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Времена года")

        self.winter_text = ("Зима укрывает землю пушистым белым снегом. Дни становятся короткими, а мороз рисует узоры "
                            "на окнах. Люди празднуют Новый год и катаются на лыжах или коньках. На улице очень "
                            "холодно!")
        self.spring_text = ("Весна приносит тепло, и снег начинает таять. На деревьях появляются первые зеленые "
                            "листья, а на полях расцветают цветы. Птицы возвращаются из теплых краев, и природа "
                            "постепенно оживает.")
        self.summer_text = ("Лето является самым жарким временем года. Солнце светит ярко, а световой день становится "
                            "очень длинным. Люди любят ездить на море, купаться и наслаждаться долгожданным отпуском.")
        self.autumn_text = ("Осень окрашивает листву деревьев в желтые и красные цвета. Часто идут дожди, и воздух "
                            "становится заметно прохладнее. Животные готовятся к зиме, а люди собирают богатый урожай.")

        self.vertical_layout = QVBoxLayout()

        self.horizontal_layout = QHBoxLayout()
        self.radio_winter = QRadioButton('зима')
        self.radio_spring = QRadioButton('весна')
        self.radio_summer = QRadioButton('лето')
        self.radio_autumn = QRadioButton("осень")

        self.label_text = QLabel(self.winter_text)
        self.radio_winter.setChecked(True)  # активная кнопка

        self.vertical_layout.addWidget(self.label_text)

        self.group = QButtonGroup()
        self.group.addButton(self.radio_winter, id=1)
        self.group.addButton(self.radio_spring, id=2)
        self.group.addButton(self.radio_summer, id=3)
        self.group.addButton(self.radio_autumn, id=4)

        self.horizontal_layout.addWidget(self.radio_winter)
        self.horizontal_layout.addWidget(self.radio_spring)
        self.horizontal_layout.addWidget(self.radio_summer)
        self.horizontal_layout.addWidget(self.radio_autumn)

        self.vertical_layout.addLayout(self.horizontal_layout)

        self.group.buttonClicked.connect(self.handle_radio_buttons)
        self.setLayout(self.vertical_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
