from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class LogLabel(QLabel):
    eventHappened = Signal(str)

    def __init__(self):
        super().__init__()
        self.setText("Пишу свою историю")

    def enterEvent(self, event):
        self.eventHappened.emit("Ко мне пришел курсор!")
    def leaveEvent(self, event):
        self.eventHappened.emit("Курсор ушёл :(")
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.eventHappened.emit("На меня нажали левой кнопкой")
        else:
            self.eventHappened.emit("На меня нажали правой кнопкой")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        label = LogLabel()
        label.eventHappened.connect(self.add_label)
        self.__layout.addWidget(label)
        self.setLayout(self.__layout)

    @Slot(str)
    def add_label(self, message):
        label = QLabel(message)
        self.__layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
