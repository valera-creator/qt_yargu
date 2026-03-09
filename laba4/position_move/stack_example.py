from PySide6.QtWidgets import QApplication, QWidget, QStackedLayout, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример стека")
        firstPageWidget = QLabel('First')
        secondPageWidget = QLabel('Second')
        thirdPageWidget = QLabel('Third')
        stackedLayout = QStackedLayout()
        stackedLayout.setStackingMode(QStackedLayout.StackAll)
        stackedLayout.addWidget(firstPageWidget)
        stackedLayout.addWidget(secondPageWidget)
        stackedLayout.addWidget(thirdPageWidget)
        self.setLayout(stackedLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
