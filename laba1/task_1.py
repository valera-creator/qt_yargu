from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.setWindowTitle("custom name")

        self.first_font_size = 10

        self.first_label = QLabel(self)
        self.setting_first_label()

        self.second_label = QLabel(self)
        self.setting_second_label()

        self.third_label = QLabel(self)
        self.setting_third_label()

    def setting_first_label(self):
        self.first_label.setGeometry(0, 0, self.width() // 2, self.height() // 4)

        self.first_label.setText("text " * 20)
        self.first_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.first_label.setWordWrap(True)  # разрешить перенос слов

        self.first_label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.first_label.setLineWidth(2)

        self.first_label.setMargin(10)  # отступ внитри рамки

        font_first = QFont("Times", self.first_font_size, italic=True)
        self.first_label.setFont(font_first)

    def setting_second_label(self):
        self.second_label.setGeometry(0, 0, self.width() // 2, self.height() // 4)
        self.second_label.move(0, self.first_label.y() + self.first_label.height() + 10)
        self.second_label.setText("bear " * 4)

        self.second_label.setWordWrap(True)
        self.second_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        font_second = QFont("Times", self.first_font_size * 2)
        self.second_label.setFont(font_second)

        self.second_label.setMargin(10)  # отступ внитри рамки

        self.second_label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.second_label.setLineWidth(2)

    def setting_third_label(self):
        self.third_label.setGeometry(0, 0, self.width() // 2, self.height() // 4)
        self.third_label.move(0, self.second_label.y() + self.second_label.height() + 10)

        image = QPixmap("clocks.png")
        if image.isNull():
            self.third_label.setText("Изображение не найдено!!!")
        else:
            image = image.scaledToHeight(self.third_label.height())
            if image.width() > self.third_label.width():  # если по ширине не влезает
                image = image.scaledToWidth(self.third_label.width())
            self.third_label.setPixmap(image)

        self.third_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.third_label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.third_label.setLineWidth(2)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
