from PySide6.QtWidgets import QWizardPage, QLabel, QCheckBox, QVBoxLayout


class Themes(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("3 этап")

        self.label_text_hobbies = QLabel("Выберите увлечения")

        self.topics_forest = QCheckBox("Лесные походы")
        self.topics_coding = QCheckBox("Программирование")
        self.topics_fish = QCheckBox("Рыбалка")
        self.label_text_approval = QLabel("Выберите согласие/несогласие")
        self.approval = QCheckBox("Согласие на рассылку")

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label_text_hobbies)
        self.v_layout.addWidget(self.topics_forest)
        self.v_layout.addWidget(self.topics_coding)
        self.v_layout.addWidget(self.topics_fish)

        self.v_layout.addWidget(self.label_text_approval)
        self.v_layout.addWidget(self.approval)

        self.registerField("topic_forest", self.topics_forest, "checked")
        self.registerField("topic_coding", self.topics_coding, "checked")
        self.registerField("topic_fish", self.topics_fish, "checked")
        self.registerField("approval", self.approval, "checked")

        self.setLayout(self.v_layout)
