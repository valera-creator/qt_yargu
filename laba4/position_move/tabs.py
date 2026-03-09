from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTabWidget, QApplication, QVBoxLayout, QLabel, QScrollArea, QPushButton, QLineEdit, \
    QFormLayout, QWidget


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap("landscape.jpg"))
        scrollArea = QScrollArea()
        scrollArea.setWidget(imageLabel)
        self.addTab(scrollArea, "Прокрутка")

        secondTab = QWidget()
        button1 = QPushButton("One")
        lineEdit1 = QLineEdit()
        button2 = QPushButton("Two")
        lineEdit2 = QLineEdit()
        button3 = QPushButton("Three")
        lineEdit3 = QLineEdit()
        layout = QFormLayout()
        layout.addRow(button1, lineEdit1)
        layout.addRow(button2, lineEdit2)
        layout.addRow(button3, lineEdit3)
        secondTab.setLayout(layout)
        self.addTab(secondTab, "Пример формы")

        self.tabBar().setMovable(True)


if __name__ == "__main__":
    app = QApplication([])
    address_widget = TabWidget()
    address_widget.show()
    app.exec()
