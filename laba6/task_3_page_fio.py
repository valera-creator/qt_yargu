from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QWizardPage

from task_3_check_empty import check_empty


class FIOPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("2 этап")
        max_length_line_edit = 40

        self.v_layout = QVBoxLayout()

        self.regex_fio = QRegularExpression(r"^[A-ZА-ЯЁ][A-Za-zА-Яа-яЁё\s\-]*$")
        self.validator = QRegularExpressionValidator(self.regex_fio)

        self.surname_label = QLabel("Фамилия")
        self.surname_label.setMinimumWidth(60)
        self.surname_line_edit = QLineEdit()
        self.surname_line_edit.setPlaceholderText("Фамилия (с большой буквы)")
        self.surname_line_edit.setMaxLength(max_length_line_edit)
        self.surname_line_edit.setValidator(self.validator)

        self.surname_h_layout = QHBoxLayout()
        self.surname_h_layout.addWidget(self.surname_label)
        self.surname_h_layout.addWidget(self.surname_line_edit)
        self.v_layout.addLayout(self.surname_h_layout)

        self.name_label = QLabel("Имя")
        self.name_label.setMinimumWidth(60)
        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText("Имя (с большой буквы)")
        self.name_line_edit.setMaxLength(max_length_line_edit)
        self.name_line_edit.setValidator(self.validator)

        self.name_h_layout = QHBoxLayout()
        self.name_h_layout.addWidget(self.name_label)
        self.name_h_layout.addWidget(self.name_line_edit)
        self.v_layout.addLayout(self.name_h_layout)

        self.patronymic_label = QLabel("Отчество")
        self.patronymic_label.setMinimumWidth(60)
        self.patronymic_line_edit = QLineEdit()
        self.patronymic_line_edit.setPlaceholderText("Отчество (с большой буквы)")
        self.patronymic_line_edit.setMaxLength(max_length_line_edit)
        self.patronymic_line_edit.setValidator(self.validator)

        self.patronymic_h_layout = QHBoxLayout()
        self.patronymic_h_layout.addWidget(self.patronymic_label)
        self.patronymic_h_layout.addWidget(self.patronymic_line_edit)
        self.v_layout.addLayout(self.patronymic_h_layout)

        # добавление регистрационных полей, чтобы в главном окне получить значения
        self.registerField("surname", self.surname_line_edit, "text")
        self.registerField("name", self.name_line_edit, "text")
        self.registerField("patronymic", self.patronymic_line_edit, "text")

        # подключение отслеживание сигналов при изменении в полях ввода
        self.surname_line_edit.textChanged.connect(self.on_text_changed)
        self.name_line_edit.textChanged.connect(self.on_text_changed)
        self.patronymic_line_edit.textChanged.connect(self.on_text_changed)

        self.setLayout(self.v_layout)

    def on_text_changed(self):
        """сообщает Wizard, что нужно перепроверить isComplete(), вызывается после каждого изменения в полях ввода"""
        self.completeChanged.emit()

    def isComplete(self):
        """проверка, что поля фамилии и имени не пустые"""
        return check_empty(self.surname_line_edit.text()) and check_empty(self.name_line_edit.text())
