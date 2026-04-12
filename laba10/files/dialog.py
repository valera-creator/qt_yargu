from PySide6.QtCore import QDir, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow, QVBoxLayout, QLabel, QWidget, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_menu()
        layout = QVBoxLayout()
        self.__image = QLabel()
        layout.addWidget(self.__image)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def add_menu(self):
        menuBar = self.menuBar()
        menuBar.resize(100, 20)
        menuDialogs = menuBar.addMenu("Диалоги")
        actionFile = menuDialogs.addAction("Файл-картинка")
        actionFile.triggered.connect(self.clickActionFile)

    @Slot()
    def clickActionFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Открыть картинку", str(QDir.currentPath()),
                                               "Картинки (*.png *.jpg)")
        print(fileName)
        self.__image.setPixmap(QPixmap(fileName[0]))


app = QApplication([])
window = Window()
window.show()
app.exec()
