from PySide6.QtCore import QDir, Slot, QFileInfo
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QTreeView, QFileSystemModel, QMenu
from task_2_create_dialog import CreateDialog
from task_2_delete_dialog import DeleteDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Файловая система")
        self.setFixedSize(600, 500)

        self.treeView = QTreeView()
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.homePath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(QDir.currentPath()))

        self.setCentralWidget(self.treeView)

    def contextMenuEvent(self, e):
        context = QMenu(self)

        # пересчет на координаты окна в виджете, где клик
        click_pos = self.treeView.viewport().mapFromGlobal(e.globalPos())
        # элемент в модели по координатам
        index = self.treeView.indexAt(click_pos)
        # абсолютный путь к файлу для проверки, чтобы потом проверить, что пользователь выбрал именно папку
        path = self.model.fileInfo(index).absoluteFilePath()

        if index.isValid() and QFileInfo(path).isDir():
            create = QAction("Создать", self)
            create.triggered.connect(lambda: self.create_directory(index))
            context.addAction(create)

            delete = QAction("Удалить", self)
            delete.triggered.connect(lambda: self.delete_directory(index))
            context.addAction(delete)
        context.exec(e.globalPos())

    @Slot()
    def create_directory(self, index):
        parent_path = self.model.fileInfo(index).absoluteFilePath()
        basename = self.model.fileInfo(index).baseName()
        dlg = CreateDialog(basename)
        if dlg.exec():
            directory = dlg.name_new_directory()
            dir_obj = QDir(parent_path)
            if dir_obj.mkdir(directory):
                self.statusBar().showMessage("Папка успешно создана", 3000)
            else:
                self.statusBar().showMessage("Ошибка создания папки", 3000)

    @Slot()
    def delete_directory(self, index):
        parent_path = self.model.fileInfo(index).absoluteFilePath()
        basename = self.model.fileInfo(index).baseName()
        dlg = DeleteDialog(basename)
        if dlg.exec():
            dir_obj = QDir(parent_path)
            if dir_obj.removeRecursively():
                self.statusBar().showMessage("Папка успешно удалена", 3000)
            else:
                self.statusBar().showMessage("Ошибка удаления папки", 3000)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
