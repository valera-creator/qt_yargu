from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QTreeView


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        treeView = QTreeView()
        model = QFileSystemModel()
        model.setRootPath(QDir.homePath())
        treeView.setModel(model)
        treeView.setRootIndex(model.index(QDir.currentPath()))
        self.setCentralWidget(treeView)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()