from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

import rc_images
# pyside6-rcc images.qrc -o rc_images.py

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        toolBar = QToolBar()
        self.addToolBar(toolBar)
        plusIcon = QIcon(QPixmap(":/img/plus.png"))
        minusIcon = QIcon(QPixmap(":/img/minus.png"))
        incAction = toolBar.addAction(plusIcon, "Increase")
        incAction.triggered.connect(self.increase)
        previousAction = toolBar.addAction(minusIcon, "Decrease")
        previousAction.triggered.connect(self.decrease)

    def increase(self):
        print('You have selected inc')

    def decrease(self):
        print('You have selected dec')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
