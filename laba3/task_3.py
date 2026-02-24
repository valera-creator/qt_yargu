from PySide6.QtCore import QDate, Qt, QDateTime
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QDateTimeEdit, QVBoxLayout, QTextEdit
import datetime


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дата рождения")
        self.setMinimumSize(350, 350)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.setLayout(self.vertical_layout)

        self.label_text = QLabel("Выберите дату рождения")

        self.dateTimeEdit = QDateTimeEdit(QDate.currentDate(), self)
        self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-365 * 120))
        self.dateTimeEdit.setMaximumDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("yyyy.MM.dd hh:mm:ss")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.dateTimeChanged.connect(self.calculate_diff)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        self.vertical_layout.addWidget(self.label_text)
        self.vertical_layout.addWidget(self.dateTimeEdit)
        self.vertical_layout.addWidget(self.textEdit)

    def calculate_diff(self):
        cur_datetime = datetime.datetime.today()
        user_datetime = self.dateTimeEdit.dateTime().toPython()  # конверт в формат datetime

        years = cur_datetime.year - user_datetime.year
        # если дня рождения еще не было
        if (cur_datetime.month, cur_datetime.day) < (user_datetime.month, user_datetime.day):
            years -= 1

        diff = cur_datetime - user_datetime
        text = (f"Сейчас лет: {years}\nСейчас часов: {int(diff.total_seconds() // 3600)}\n"
                f"Сейчас секунд: {int(diff.total_seconds())}")
        self.textEdit.setText(text)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
